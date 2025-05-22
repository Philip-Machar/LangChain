import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
from dotenv import load_dotenv
load_dotenv()

google_api_key = os.getenv("GOOGLE_API_KEY")

llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    google_api_key=google_api_key,
    temperature=0.7
)

#prompt template
prompt_template = ChatPromptTemplate(
    [
        ("system", "you are an expert that tell unknown facts about {topic}"), 
        ("human", "tell me {factCount}")
    ]
)

#creating a chain using langchain and displaying only the content using string output parser function
chain = prompt_template | llm | StrOutputParser()

#adding values to the chain and printing the results
results = chain.invoke({"topic": "Animals", "factCount": 2})
print(results)
