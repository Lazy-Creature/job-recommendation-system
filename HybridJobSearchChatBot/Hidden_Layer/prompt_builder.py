import streamlit as st
from .dataset_handler import load_dataset, find_relevant_jobs

df_jobs=load_dataset()

def build_context_prompt(user_input, retriever=None):
    prompt=""

    # Add past messages
    for entry in st.session_state.history:
        role="User" if entry["role"] == "user" else "AI"
        prompt+=f"{role}: {entry['content']}\n"

    # Add PDF context
    resume_text= ""
    if retriever:
        docs=retriever.get_relevant_documents(user_input)
        context="\n".join([doc.page_content for doc in docs])
        if context.strip():
            prompt+=f"\nUse the following context to assist:\n{context}\n"
            resume_text=context  # store for job matching

    # If asking about jobs, add job matches
    if "job" in user_input.lower() and resume_text:
        jobs=find_relevant_jobs(resume_text, df_jobs)
        if jobs:
            job_list="\n".join([f"{j[1]} at {j[2]} ({j[3]}) - Skills: {j[4]}" for j in jobs])
            prompt+=f"\nBased on the resume, here are relevant jobs from the dataset:\n{job_list}\n"

    # Add current question
    prompt+=f"User: {user_input}\nAI:"
    return prompt
