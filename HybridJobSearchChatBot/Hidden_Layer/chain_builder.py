from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

def build_chain(llm):
    prompt=ChatPromptTemplate.from_template("User: {question}\nAI:")
    output_parser=StrOutputParser()
    return prompt | llm | output_parser
