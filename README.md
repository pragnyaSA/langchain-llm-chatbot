# LangChain LLM Chatbot

A simple AI chatbot built using LangChain, Google Gemini API, and Llama2 (Ollama) with a Streamlit interface.

## Features
- AI chatbot using LangChain
- Supports Google Gemini API
- Supports Llama2 using Ollama
- Streamlit user interface
- Environment variable support using .env

## Technologies Used
- Python
- LangChain
- Google Gemini API
- Ollama (Llama2)
- Streamlit
- python-dotenv

## 📊 LangSmith Monitoring & Token Analysis

This project integrates **LangSmith** for advanced observability and debugging.

###  What is Monitored?

- Input Tokens
- Output Tokens
- Total Token Usage
- Latency
- Prompt & Response Logs
- Chain Execution Steps

## Project Structure
langchain-llm-chatbot
│
├── app.py
├── requirements.txt
├── .gitignore
└── README.md

## Installation

1. Clone the repository
git clone https://github.com/yourusername/langchain-llm-chatbot.git

2. Go to the project folder
cd langchain-llm-chatbot

3. Install dependencies
pip install -r requirements.txt

## Environment Variables

Create a `.env` file and add:

GOOGLE_API_KEY=your_key  
LANGCHAIN_API_KEY=your_key

## Run the Project

streamlit run app.py

streamlit run localama.py

Then open the URL shown in the terminal to use the chatbot.
