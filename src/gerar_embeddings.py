from sklearn.feature_extraction.text import TfidfVectorizer

def gerar_embeddings(textos):
    corpus = [texto for _, texto in textos]
    vectorizer = TfidfVectorizer()
    matriz = vectorizer.fit_transform(corpus)
    return matriz, vectorizer

# Simulação de uso
if __name__ == "__main__":
    from extrair_texto import extrair_texto_de_pdfs
    textos = extrair_texto_de_pdfs("../pdfs")
    matriz, vectorizer = gerar_embeddings(textos)
    print("Embeddings gerados com sucesso (simulado).")
