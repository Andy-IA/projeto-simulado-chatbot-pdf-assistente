import streamlit as st
from extrair_texto import extrair_texto_de_pdfs
from gerar_embeddings import gerar_embeddings
from buscar_resposta import buscar_resposta

st.title("📚 Chatbot PDF Assistente")

# Carregamento e preparação
textos = extrair_texto_de_pdfs("pdfs")
matriz, vectorizer = gerar_embeddings(textos)

# Interface de chat
pergunta = st.text_input("Digite sua pergunta sobre os PDFs:")
if pergunta:
    resposta = buscar_resposta(pergunta, textos, matriz, vectorizer)
    st.write(resposta)
