import tempfile
import streamlit as st
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings

def process_pdf(uploaded_file):
    retriever = None
    with st.spinner("📄 Processing PDF..."):
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
            tmp.write(uploaded_file.read())
            tmp_path = tmp.name

        loader=PyPDFLoader(tmp_path)
        docs=loader.load()

        splitter=RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
        chunks=splitter.split_documents(docs)

        embeddings=HuggingFaceEmbeddings()
        vectorstore=FAISS.from_documents(chunks, embeddings)
        retriever=vectorstore.as_retriever(search_type="similarity", k=3)

    st.success("✅ PDF processed and ready for questions!")
    return retriever
