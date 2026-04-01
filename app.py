from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# 🔍 DEBUG
print("GOOGLE API KEY:", os.getenv("GOOGLE_API_KEY"))
print("LANGCHAIN API KEY:", os.getenv("LANGCHAIN_API_KEY"))

# ✅ LangSmith Tracing
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_PROJECT"] = "gemini-demo"

# ✅ Gemini API
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")

# Prompt Template
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    ("user", "Question: {question}")
])

# UI
st.title('Langchain Demo With GEMINI API')
input_text = st.text_input("Search the topic u want")

# LLM
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

# Parser
output_parser = StrOutputParser()

# Chain
chain = prompt | llm | output_parser

# Run
if input_text:
    result = chain.invoke(
        {"question": input_text},
        config={"run_name": "gemini-run"}   # optional but helpful
    )
    st.write(result)