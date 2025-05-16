import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_google_firestore import FirestoreChatMessageHistory
from google.cloud import firestore
from dotenv import load_dotenv
load_dotenv()

#connection to firestore variables
PROJECT_ID = "langchain-242f5"
SESSION_ID = "user123"
COLLECTION_NAME = "chat_history"

#connection to our specific firestore project
client = firestore.Client(project=PROJECT_ID)

#intializing firestore chat history
print("Initializing firestore...")
chat_history = FirestoreChatMessageHistory(
    client=client,
    session_id=SESSION_ID,
    collection=COLLECTION_NAME
)
print("firestore initilized.")

#getting our google api key from .env file
google_api_key = os.getenv("GOOGLE_API_KEY")

#initializing our llm
llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    google_api_key=google_api_key,
    temperature=0.7
)

chat_history.add_message(SystemMessage("You a helpful AI assitant(you give very short answers)"))

while True:
    query = input("You: ")

    if (query == "exit"):
        break
    
    chat_history.add_message(HumanMessage(content=query))

    response = llm.invoke(chat_history.messages)
    chat_history.add_message(AIMessage(content=response.content))

    print(f"AI: ", response.content)

