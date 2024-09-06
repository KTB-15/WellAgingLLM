import os, json, warnings, torch
from openai import OpenAI
from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer,util
warnings.filterwarnings("ignore", category=FutureWarning)

load_dotenv()
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

# 유사도 검사 모델
model = SentenceTransformer('paraphrase-albert-small-v2')

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

# JSON 파일로 저장하는 함수
def save_messages_to_json(messages, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(messages, f, ensure_ascii=False, indent=4)

# JSON 파일에서 데이터 로드
def load_messages_from_json(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)

def evaluate_answer(message, user_input):
    # 두 문장의 임베딩 계산
    embedding1 = model.encode([message], convert_to_tensor=True)
    embedding2 = model.encode([user_input], convert_to_tensor=True)

    # 두 임베딩 사이의 코사인 유사도 계산
    similarity = util.pytorch_cos_sim(embedding1, embedding2)

    response = "맞았습니다" if similarity.item()*100>80 else "틀렸습니다"

    return response, similarity.item()*100