import fitz  # PyMuPDF
import os

def extrair_texto_de_pdfs(pasta_pdf):
    textos = []
    for nome_arquivo in os.listdir(pasta_pdf):
        if nome_arquivo.endswith(".pdf"):
            caminho = os.path.join(pasta_pdf, nome_arquivo)
            doc = fitz.open(caminho)
            texto = ""
            for pagina in doc:
                texto += pagina.get_text()
            textos.append((nome_arquivo, texto))
    return textos

# Simulação de uso
if __name__ == "__main__":
    textos_extraidos = extrair_texto_de_pdfs("../pdfs")
    for nome, texto in textos_extraidos:
        print(f"\n--- {nome} ---\n{texto[:300]}...")  # Mostra os primeiros 300 caracteres
