import os, warnings, openai
from openai import OpenAI
from dotenv import load_dotenv
warnings.filterwarnings("ignore", category=FutureWarning)

load_dotenv()
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

# 유사도 검사 모델
model = "text-embedding-ada-002"

# GPT-4o-mini로 대화 생성
def chat_with_gpt(prompt, user_input):
    response = client.chat.completions.create(
        model="gpt-4o-mini-2024-07-18",
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": user_input}
        ]
    )
    return response.choices[0].message.content.strip()

def get_embedding(text):
    # 임베딩 생성
    response = openai.embeddings.create(
        input=text,
        model=model
    )
    embedding = response.data[0].embedding
    return embedding