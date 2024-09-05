import os, json, warnings
from openai import OpenAI
from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer, util
warnings.filterwarnings("ignore", category=FutureWarning)

load_dotenv()
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

# 유사도 검사 모델
model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

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

# GPT에게 질문을 만들어 달라고 요청하는 함수
def generate_question_from_data(data):
    messages = (
        '제공되는 데이터를 기반으로 쉽게 대답할 수 있는 질문과 답을 만들어서 리스트 형식으로 알려줘. '
        '질문을 그대로 쓰지말고 쉽게 답할 수 있도록 변형시켜줘.'
        '예를 들어, "매일 판교를 가고 있다"라는 데이터에서, "매일 어디를 가고 있나요?"라는 문제를 만들 수 있지. '
        '또한 "점심에 돈가스를 먹었다"라는 데이터가 있으면 "점심에 먹은 음식이 무엇인가요?"와 같은 질문을 낼 수 있어. '
        '반환 형식은 다음과 같아야 해:\n'
        '["질문","정답"]'
    )
    response = chat_with_gpt(messages, data)
    # 응답이 리스트 형식의 문자열로 반환되었을 때 이를 파싱
    try:
        # 응답을 JSON 형식으로 파싱 시도
        question_answer_list = json.loads(response)
        return question_answer_list
    except json.JSONDecodeError:
        print("응답을 JSON으로 파싱하는 데 실패했습니다. eval()로 처리합니다.")

        # JSON으로 파싱이 실패하면 eval로 처리
        try:
            question_answer_list = eval(response)
            return question_answer_list
        except:
            print("응답을 리스트로 변환하는 데 실패했습니다.")
            return None

def evaluate_answer(message, user_input):
    # 두 문장의 임베딩 계산
    embedding1 = model.encode([message], convert_to_tensor=True)
    embedding2 = model.encode([user_input], convert_to_tensor=True)

    # 두 임베딩 사이의 코사인 유사도 계산
    similarity = util.pytorch_cos_sim(embedding1, embedding2)

    response = "맞았습니다" if similarity.item()*100>80 else "틀렸습니다"

    return response, similarity.item()*100