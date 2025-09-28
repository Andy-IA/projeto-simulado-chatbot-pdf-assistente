# 🤖 Chatbot PDF Assistente — IA Generativa com Busca Vetorial

Este projeto simula a criação de um chatbot inteligente capaz de responder perguntas com base no conteúdo de arquivos PDF. Utilizando conceitos de IA generativa, embeddings e busca vetorial, o sistema foi estruturado para compreender e responder de forma contextualizada, como se estivesse operando em um ambiente de nuvem com Azure Foundry.

---

## 📊 Objetivo

- Carregar arquivos PDF com conteúdo relevante.
- Indexar os textos com embeddings e busca vetorial.
- Gerar respostas contextualizadas com IA generativa.
- Criar um chat interativo para perguntas e respostas.
- Simular o uso de Azure Foundry para fins didáticos.

---

## 🧪 Processo

1. **Entrada de dados simulada**  
   Frases representativas foram inseridas no arquivo `inputs/exemplo.txt`, simulando trechos extraídos de PDFs acadêmicos.

2. **Extração de texto dos PDFs**  
   Utilizamos bibliotecas como `PyMuPDF` para simular a leitura dos documentos.

3. **Geração de embeddings**  
   Os textos foram vetorizados com modelos simulados, como se estivessem sendo processados por serviços de IA na nuvem.

4. **Busca vetorial**  
   Implementamos uma estrutura de busca que simula o uso de FAISS ou ChromaDB para encontrar trechos relevantes.

5. **Resposta com IA generativa**  
   As respostas foram geradas com base nos textos indexados, simulando o uso de modelos como GPT em ambiente cloud.

6. **Interface de chat (simulada)**  
   O sistema foi estruturado para funcionar como um chatbot interativo, com possibilidade de integração via Streamlit.

---

## 📸 Prints

> ⚠️ Como este projeto é uma simulação, os prints abaixo representam o que seria visto em um ambiente real.

- 📄 Visualização dos PDFs carregados
- 🧠 Vetorização dos textos com embeddings
- 💬 Interface de chat respondendo perguntas com base nos documentos

---

## 💡 Insights

- A busca vetorial é extremamente eficiente para encontrar informações específicas em grandes volumes de texto.
- Embeddings permitem que o sistema compreenda o contexto sem depender de palavras exatas.
- A IA generativa pode ser personalizada para responder com base em conhecimento proprietário.

---

## 🚀 Possibilidades Futuras

- Integração com APIs reais de IA (OpenAI, Azure, Hugging Face)
- Deploy em nuvem com Azure Foundry ou Streamlit Cloud
- Suporte a múltiplos formatos de documentos (PDF, DOCX, TXT)
- Treinamento com base em TCCs, artigos científicos ou manuais técnicos

---

## 📂 Estrutura do Projeto

chatbot-pdf-assistente/
├── inputs/
│   └── exemplo.txt
├── pdfs/
│   ├── artigo1.pdf
│   └── artigo2.pdf
├── src/
│   ├── extrair_texto.py
│   ├── gerar_embeddings.py
│   ├── buscar_resposta.py
│   └── app_chat.py
├── README.md


---

## 👨‍💻 Observação

Projeto desenvolvido com simulação do uso de IA generativa e infraestrutura de nuvem (Azure Foundry), devido à ausência de acesso à plataforma. Todos os passos foram reproduzidos localmente com foco educacional e demonstrativo.


