import os
import json
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

# GPT-4o-mini로 대화 생성
def chat_with_gpt(messages,prompt):
    response = client.chat.completions.create(
        model="gpt-4o-mini-2024-07-18",
        messages=[
            {"role": "system", "content": messages},
            {"role": "system", "content": prompt}
        ]
    )
    return response.choices[0].message.content.strip()

# JSON 파일로 저장하는 함수
def save_messages_to_json(messages, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(messages, f, ensure_ascii=False, indent=4)

# JSON 파일에서 데이터 로드
def load_messages_from_json(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)