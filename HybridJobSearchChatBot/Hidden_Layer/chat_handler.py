def chat_with_bot(chain, full_prompt):
    return chain.invoke({"question": full_prompt})
