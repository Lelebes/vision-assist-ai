# 👁️ Vision-Assist AI: Leitor de Telas Inteligente

## 📌 O Problema

Sistemas operacionais e sites complexos possuem falhas de acessibilidade. Pessoas com deficiência visual muitas vezes dependem de leitores de tela robóticos que não conseguem interpretar o contexto de imagens ou interfaces desorganizadas.

## 💡 A Solução

Um script em Python que roda em segundo plano. Ao pressionar um atalho global (`Ctrl + Alt + Espaço`), o sistema captura a tela atual e utiliza a IA do Google (Gemini 2.5 Flash) para analisar o conteúdo visual e descrevê-lo de forma inteligente em voz alta para o usuário.

## 🛠️ Tecnologias Utilizadas

- **Python 3:** Lógica principal e orquestração.
- **Google Gemini API:** Visão computacional e processamento de linguagem natural.
- **keyboard:** Escuta passiva de atalhos em segundo plano.
- **pyttsx3:** Sintetização de voz offline (Text-to-Speech).
- **PyInstaller:** Empacotamento para executável standalone.

## 🚀 Como Executar Localmente

1. Clone o repositório.
2. Instale as dependências: `pip install -r requirements.txt` _(Obs: crie esse arquivo depois listando as bibliotecas)_.
3. Insira sua Google API Key no arquivo `captura.py`.
4. Execute `python captura.py`.

## 📦 Download do Executável

_(No futuro, você colocará aqui o link da aba Releases do GitHub onde a pessoa pode baixar o .exe diretamente)_
