import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv

load_dotenv()

google_api_key = os.getenv("GOOGLE_API_KEY")

llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    google_api_key=google_api_key,
    temperature=0.7
)

chat_history = []

system_message = SystemMessage(content="You are a helpful ai assistant(you give me short answers)")
chat_history.append(system_message)

while True:
    querry = input("You: ")

    if querry == "exit":
        break

    chat_history.append(HumanMessage(content=querry))

    response = llm.invoke(chat_history)
    chat_history.append(AIMessage(content=response.content))

    print(input(f"AI: {response.content}"))

    




