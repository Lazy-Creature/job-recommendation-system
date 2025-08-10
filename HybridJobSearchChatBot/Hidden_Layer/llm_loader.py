import os
import streamlit as st
from dotenv import load_dotenv
from langchain_groq import ChatGroq

def load_llm():
    load_dotenv()
    api_key=os.getenv("GROQ_API_KEY")

    if not api_key:
        st.error("Please set your GROQ_API_KEY in the .env file.")
        st.stop()

    return ChatGroq(api_key=api_key, model="llama3-8b-8192")
