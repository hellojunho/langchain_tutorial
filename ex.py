from dotenv import load_dotenv
load_dotenv()
import os

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

api_key = os.getenv("OPEN_AI_API_KEY")

llm = ChatOpenAI(openai_api_key=api_key)

# print(llm.invoke("2024년 청년 지원 정책에 대하여 알려줘"))

prompt = ChatPromptTemplate.from_messages([
    ("system", "넌 청년을 행복하게 하기 위한 정부정책 안내 컨설턴트야."),
    ("user", "{input}")
])

chain = prompt | llm # pipe 연산자
print(chain.invoke({"input": "2024년 청년 지원 정책에 대해 알려줘"}))