# ChatBot com Langchain e ChatGroq / ChatBot with Langchain and ChatGroq

Este projeto implementa um chatbot utilizando a biblioteca Langchain e o modelo de linguagem da Groq. Este projeto foi inspirado no tutorial do site da [Langchain](https://python.langchain.com/docs/tutorials/chatbot/). O objetivo principal deste projeto foi aprender e entender como funcionam os fluxos de linguagem, a integração com modelos de IA e o gerenciamento do histórico de conversa. O chatbot foi implementado com o modelo ChatGroq, que permite traduzir as respostas para o idioma que o usuário utilizar, e, caso o idioma seja desconhecido, o chatbot responderá em português (pt-br).

This project implements a chatbot using the Langchain library and the Groq language model. This project was inspired by the tutorial on the [Langchain](https://python.langchain.com/docs/tutorials/chatbot/) website. The main goal of this project was to learn and understand how language flows work, how to integrate with AI models, and how to manage conversation history. The chatbot was implemented with the ChatGroq model, which allows translating responses into the language used by the user, and in case the language is unknown, the chatbot will respond in Portuguese (pt-br).

## Requisitos / Requirements

Para rodar o projeto, você precisará de:

To run the project, you will need:

- Python 3.7 ou superior / Python 3.7+ 
- [dotenv](https://pypi.org/project/python-dotenv/) para gerenciamento de variáveis de ambiente / for environment variable management
- [Langchain](https://pypi.org/project/langchain/) para construção de fluxos de linguagem / for building language flows
- [langchain-groq](https://github.com/langchain-ai/langchain-groq) para integração com o modelo de linguagem Groq / for integrating with the Groq language model
- [Groq AI API Key](https://www.groq.com/) (necessária para usar o modelo de linguagem) / required to use the language model


## Instalação / Installation

1. Clone o repositório / Clone the repository:

    ```bash
    git clone https://github.com/seu-usuario/chatbot-langchain.git
    cd chatbot-langchain
    ```

2. Crie e ative o ambiente virtual / Create and activate the virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows use: venv\Scripts\activate
    ```

3. Instale as dependências / Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Configure sua chave de API no arquivo `.env` / Set your API key in the `.env` file:

    ```env
    AI_API_KEY=sua_chave_de_api_aqui
    ```

## Como Usar / How to Use

1. Execute o chatbot / Run the chatbot:

    ```bash
    python bot.py
    ```

2. Interaja com o bot no terminal e digite `exit` para sair / Interact with the bot in the terminal and type `exit` to exit.
