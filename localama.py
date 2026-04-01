from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_ollama import OllamaLLM
import streamlit as st
import os
from dotenv import load_dotenv

# Load env
load_dotenv()

os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_PROJECT"] = "llama-demo"

# Prompt
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    ("user", "Question: {question}")
])

# UI
st.title("LangChain Demo with Llama2")
input_text = st.text_input("Search the topic you want")

# Llama2 model
llm = OllamaLLM(model="llama2")

# Parser
output_parser = StrOutputParser()

# Chain
chain = prompt | llm | output_parser

if input_text:
    result = chain.invoke(
        {"question": input_text},
        config={"run_name": "llama2-run"}  # helps in tracing
    )
    st.write(result)