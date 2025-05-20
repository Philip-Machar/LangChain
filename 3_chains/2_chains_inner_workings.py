import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
from langchain.schema.runnable import RunnableLambda, RunnableSequence
from dotenv import load_dotenv
load_dotenv()

google_api_key = os.getenv("GOOGLE_API_KEY")

model = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    google_api_key=google_api_key,
    temperature=0.7
)

promt_template = ChatPromptTemplate.from_messages(
    [
        ("system", "you are an expert in facts about {topic}"),
        ("human", "tell me {factCount} facts")
    ]
)

#create individual tasks
format_prompt = RunnableLambda(lambda x: promt_template.format_prompt(**x))
invoke_model = RunnableLambda(lambda x: model.invoke(x.to_messages()))
parse_output = RunnableLambda(lambda x: x.content)

#create the chain
chain = RunnableSequence(first=format_prompt, middle=[invoke_model], last=parse_output)

#run the chain
response = chain.invoke({"topic": "soccer", "factCount": 2})

print(response)

