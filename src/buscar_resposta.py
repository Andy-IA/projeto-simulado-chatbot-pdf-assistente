from sklearn.metrics.pairwise import cosine_similarity

def buscar_resposta(pergunta, textos, matriz, vectorizer):
    pergunta_vetorizada = vectorizer.transform([pergunta])
    similaridades = cosine_similarity(pergunta_vetorizada, matriz).flatten()
    indice_mais_similar = similaridades.argmax()
    nome_arquivo, texto = textos[indice_mais_similar]
    return f"Resposta baseada em {nome_arquivo}:\n\n{texto[:500]}..."

# Simulação de uso
if __name__ == "__main__":
    from extrair_texto import extrair_texto_de_pdfs
    from gerar_embeddings import gerar_embeddings

    textos = extrair_texto_de_pdfs("../pdfs")
    matriz, vectorizer = gerar_embeddings(textos)

    pergunta = "O que é engenharia de software moderna?"
    resposta = buscar_resposta(pergunta, textos, matriz, vectorizer)
    print(resposta)
