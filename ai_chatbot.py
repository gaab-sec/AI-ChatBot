import os, subprocess
from dotenv import load_dotenv
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory
from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate, HumanMessagePromptTemplate, MessagesPlaceholder, AIMessagePromptTemplate

# Load environment variables
load_dotenv()
api_key = os.getenv('AI_API_KEY')

if not api_key:
    # Raise an error if the API key is not found
    raise ValueError("AI_API_KEY not found. Make sure to set the key in the .env file")

# Initialize the model
model = ChatGroq(model='llama3-8b-8192')

# Define the prompt structure
prompt = ChatPromptTemplate(
    [
        MessagesPlaceholder(variable_name="chat_history"),  # Placeholder for chat history
        AIMessagePromptTemplate.from_template(
            'Você é um assistente virtual, chatbot. Traduza sua resposta para o idioma que o usuário usar.'
            'Se o idioma for desconhecido, responda em pt-br'
        ),  # AI behavior
        HumanMessagePromptTemplate.from_template('{text}'),  # Human's message template
    ]
)

# Set up memory for conversation history
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

# Combine prompt, model, and memory into an LLMChain
chain = LLMChain(
    prompt=prompt,
    llm=model,
    memory=memory
)

# Function to run the ai bot
def run_ai_bot() -> None:
    subprocess.call('cls' if os.name == 'nt' else 'clear', shell=True) # Clear the terminal
    print('ChatBot iniciado! ["exit" para sair]\n')
    
    while True:
        text = input('-> ')  # Get user input

        if text.lower() == 'exit':  # Exit condition
            break

        try:
            ai_message = chain.invoke(text)  # Get AI response
            print(f'\nChatBot: {ai_message["text"]}\n')  # Show AI response
        except Exception as e:
            print(f'Erro ao comunicar com o modelo: {e}')

# Run the bot if the script is executed directly
if __name__ == '__main__':
    run_ai_bot()
