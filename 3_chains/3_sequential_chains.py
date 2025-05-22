import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableLambda
from dotenv import load_dotenv
load_dotenv()

google_api_key = os.getenv("GOOGLE_API_KEY")

model = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    google_api_key=google_api_key,
    temperature=0.7
)

#foootball facts prompt template
football_facts_prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", "you are an expert that tell unknown facts about {topic}"), 
        ("human", "tell me {factCount}")
    ]
)

#translate football facts prompt template
translate_prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a language translator that translate text to {language}"),
        ("human", "translate this text {text}")
    ]
)

prepare_translation = RunnableLambda(lambda text: {"text": text, "language": "swahili"})


#creating a chain using langchain and displaying only the content using string output parser function
chain = football_facts_prompt_template | model | StrOutputParser() | prepare_translation | translate_prompt_template | model | StrOutputParser()

#adding values to the chain and printing the results
results = chain.invoke({"topic": "Animals", "factCount": 2})
print(results)
