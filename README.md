# Confused-GPT ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
## Introducing Confused GPT that will give mind bending questions to your questions. Easy to use and very educative. I am using langchain python library and model apis from hugging face.

# Installation
Use any python IDE of choice and run the following installation commands in the terminal to get the libraries up and running:

COLAB : ``` !pip -q install langchain huggingface_hub transformers sentence_transformers accelerate bitsandbytes ```   

VSCODE : ``` pip install langchain huggingface_hub transformers sentence_transformers accelerate bitsandbytes ```

# Usage
<ul>
<li> Head over to <a href = "https://huggingface.co/login">Hugging Face</a> and create an account</li>
<li> Open the setting after you have verified your mails</li>
<li> Find Access Tokens in settings and create your token</li>
<li> Use this token in place of the text YOUR HUGGING FACE KEY HERE</li>
<li> Then use <a href = "https://huggingface.co/models?pipeline_tag=text2text-generation&sort=trending"> this page </a> to swap the models used in code with others</li>
</ul>

# For Your Help
In case you observe the model taking long time to respond to your request, swap a model with a smaller version like swap google/flan-xxl with google/flan-small (please refer to the page mentioned above to get accurate names of the APIs). This code works better with higher bandwidth.
