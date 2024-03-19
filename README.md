## Blog Entry Generator

- This is a blog entry generator app built in Python using LLama 2 LLM, StreamLit for the web development and LangChain for the management of the LLama2 model.

#### Instalation
- To install the app in your computer, first, you need to download the ![LLama2 model](https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/blob/main/llama-2-7b-chat.ggmlv3.q8_0.bin) by clicking in the download link, and storing it on a folder called `models` in the root of your project.

    - Then you need to run this command to install the dependencies:
        - `pip install -r requirements.txt`
        - I suggest you to create a `python venv` and install the dependecies on it.

    - Finally, to run the app just write:
        `streamlit run app.py`

#### Usage
- To use the application you just need to provide a topic, a number of words and a blog style. All of this inputs you can change them on the `app.py` file.