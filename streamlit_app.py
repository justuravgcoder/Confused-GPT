import os
import streamlit as st
from langchain import PromptTemplate, HuggingFaceHub, LLMChain

os.environ['HUGGINGFACEHUB_API_TOKEN'] = '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'
template = """Question: {question}
Answer:"""
prompt = PromptTemplate(template=template, input_variables=["question"])
llm_chain = LLMChain(prompt=prompt,llm=HuggingFaceHub(repo_id="stanfordnlp/SteamSHP-flan-t5-xl",model_kwargs={"temperature":0, "max_length":64}))

st.header('Welcome to the GPT that will make you question yourself :wave:')
question = st.text_input('Let it confuse you!')
if prompt:
    st.write(llm_chain.run(question))
else:
    st.write('Network Error')
