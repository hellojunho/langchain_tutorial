import streamlit as st
import openai
import os
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("OPEN_AI_API_KEY")

# OpenAI API 인증 정보
openai.api_key = api_key


# 모델 선택 사이드바
model_name = st.sidebar.selectbox(
    "ChatGPT 모델 선택",
    ["gpt-4-0125-preview", "gpt-4-turbo-preview" , "gpt-4-1106-preview", "gpt-3.5-turbo-0125", "gpt-3.5-turbo", "gpt-3.5-turbo-1106"],
    index=0
)

# 사용자 입력 받기
user_input = st.text_input("메시지를 입력하세요:")

if st.button("전송"):
    if user_input.strip() == "":
        st.warning("메시지를 입력해주세요.")
    else:
        # ChatGPT에 사용자 입력 전달
        response = openai.ChatCompletion.create(
            model=model_name,
            messages=[
                {"role": "system", "content": "도움이 되는 어시스턴트입니다."},
                {"role": "user", "content": user_input}
            ]
        )
        # 챗봇 응답 출력
        st.text(response.choices[0].message["content"])