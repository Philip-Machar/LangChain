import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_google_firestore import FirestoreChatMessageHistory
from google.cloud import firestore
from dotenv import load_dotenv
load_dotenv()

# firestore setup
PROJECT_ID = "langchain-242f5"
SESSION_ID = "user123"
COLLECTION_NAME = "chat_history"

# initialize firestore client
print("Initializing firestore client...")
client = firestore.Client(project=PROJECT_ID)

# initialize firestore chat message history
print("Initializing firestore chat message history...")
chat_history = FirestoreChatMessageHistory(
    session_id=SESSION_ID,
    collection=COLLECTION_NAME,
    client=client
)
print("Chat history initialized.")
print("The current chat history: ", chat_history.messages)  # Use .messages to see the list

google_api_key = os.getenv("GOOGLE_API_KEY")
llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    google_api_key=google_api_key,
    temperature=0.7
)

system_message = SystemMessage(content="You are a helpful AI assistant (you give me short answers).")
chat_history.add_message(system_message)

while True:
    query = input("You: ")
    if query == "exit":
        break
    chat_history.add_message(HumanMessage(content=query))
    response = llm.invoke(chat_history.messages)  # Use .messages to get the message list
    chat_history.add_message(AIMessage(content=response.content))
    print(f"AI: {response.content}")