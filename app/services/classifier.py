import os
from decouple import config
from fastapi import FastAPI
from langchain_groq import ChatGroq
from langserve import add_routes
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

os.environ['GROQ_API_KEY'] = config('GROQ_API_KEY')

def classifier():
    model = ChatGroq()
    
    translate_prompt = ChatPromptTemplate.from_template(
        'Traduza o texto a seguir para o idioma {language}: {text}'
    )
    translate_chain = translate_prompt | model | StrOutputParser()
    return translate_chain
