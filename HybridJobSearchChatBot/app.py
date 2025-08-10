import streamlit as st
from Hidden_Layer import load_llm, build_chain, build_context_prompt, chat_with_bot, process_pdf

def main():
    st.set_page_config(page_title="🤖 Hybrid Chatbot", page_icon="📄")
    st.title("🤖 Chat with AI ")
    st.caption("Ask anything! + Job finder, Upload a PDF to answer from your own docs. ")

    llm=load_llm()
    chain=build_chain(llm)

    if "history" not in st.session_state:
        st.session_state.history = []

    uploaded_file=st.file_uploader("📄 Upload PDF for RAG", type="pdf")
    retriever=None

    if uploaded_file:
        retriever=process_pdf(uploaded_file)

    for entry in st.session_state.history:
        with st.chat_message(entry["role"]):
            st.markdown(entry["content"])

    user_input=st.chat_input("Ask your question:")

    if user_input:
        st.chat_message("user").markdown(user_input)
        full_prompt=build_context_prompt(user_input, retriever)

        with st.spinner("💬 Thinking..."):
            response=chat_with_bot(chain, full_prompt)

        st.chat_message("ai").markdown(response)

        st.session_state.history.append({"role": "user", "content": user_input})
        st.session_state.history.append({"role": "ai", "content": response})

    if st.button("🗑️ Clear Chat"):
        st.session_state.history = []
        st.rerun()

if __name__ == "__main__":
    main()
