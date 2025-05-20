import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
load_dotenv()

google_api_key = os.getenv("GOOGLE_API_KEY")

llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    google_api_key=google_api_key,
    temperature=0.7
)

#converting prompt template into a form langchain can understand
prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", "you are a comedian who tells jokes about {topic}"), 
        ("human", "tell me a joke about {joke}")
    ]
)

#populating the variables in the prompt and assigning the final prompt with everythig done to variable prompt
prompt = prompt_template.invoke({"topic": "animals", "joke": "elephant"})

#assigning ai response to results variable
results = llm.invoke(prompt)

#printing the ai response(content has the message itself)
print(results.content)
