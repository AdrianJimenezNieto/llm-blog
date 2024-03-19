import streamlit as st
from langchain.prompts import PromptTemplate
from langchain_community.llms import CTransformers

## Function to get response from LLama2 model

def getLlamaResponse(input_text, no_words, blog_style):

    ## LLama2 model calling
    llm = CTransformers(model="models\llama-2-7b-chat.ggmlv3.q8_0.bin", 
                        model_type= "llama",
                        config= {"max_new_tokens":256, 
                                "temperature": 0.01})
    
    ## Prompt Template
    template = """
                Write a blog for {blog_style} job profile for a topic {input_text} within {no_words}.
                """
    
    # prompt template
    prompt = PromptTemplate(input_variables=["blog_style", "input_text", "no_words"],
                            template= template)
    
    ## Generate the response from the Llama2 model
    response = llm(prompt.format(blog_style=blog_style, input_text= input_text, no_words= no_words))

    print(response)
    return response


st.set_page_config(page_title="Generate Blogs",
                    page_icon="🤖",
                    layout="centered",
                    initial_sidebar_state="collapsed")

# Header
st.header("Generate Blogs 🤖")

# Text Input
input_text = st.text_input("Introduce the Blog topic")

## Creating 2 more columns for 2 additional fields
col1, col2 = st.columns([5,5])

with col1:
    no_words = st.text_input("Number of Words")
with col2:
    blog_style = st.selectbox("Write the blog for...",
                            ("Researchers", "Data Scientists", "Common People"), 
                            index=0)

# Submit button
submit = st.button("Generar!")

## Final Response
if submit:
    st.write(getLlamaResponse(input_text, no_words,blog_style))