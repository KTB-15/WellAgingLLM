import random
import numpy as np
from datetime import datetime
from func import *

def getUserInfo(prompt,user_input):
    # gpt 응답 및 prompt에 대화 내용 저장
    res = chat_with_gpt(prompt, user_input)

    return {'body':res}


def makeQnA(chat_history):
    chat_history_list = chat_history.chat_history
    random_message = random.choice(chat_history_list)

    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    prompt = f"""
        다음 데이터를 기반으로 사용자가 쉽게 대답할 수 있는 질문과 답을 생성해주세요.
        데이터에 포함된 날짜 정보와 현재 시간({current_time})을 비교해서,
        1. 데이터가 어제에 해당하면 '어제'라는 표현을, 오늘에 해당하면 '오늘'이라는 표현을 사용해 질문을 만드세요.
        2. 질문은 데이터에 명시적으로 포함된 정보만을 사용하여 만들어야 합니다.
        3. 사용자의 주관적인 평가나 추가 정보를 요구하는 질문은 피하세요.
        4. 질문의 문맥이 자연스럽도록 신경쓰세요.
        5. 반환 형식은 질문과 정답을 쉼표로 구분하여 작성하되, 따옴표나 다른 특수 문자를 사용하지 마세요.

        예시:
        입력 데이터: {{"Q": "오늘 점심 메뉴는?", "A": "오늘 점심으로 샐러드를 먹었어요", "T": "2024-09-05 12:30:00"}}
        올바른 출력: 오늘 점심으로 무엇을 드셨나요?,오늘 점심으로 샐러드를 먹었어요

        입력 데이터: {{"Q": "내일 할 일은?", "A": "내일은 9시에 회의가 있어요", "T": "2024-09-04 20:00:00"}}
        올바른 출력: 오늘 9시에 무슨 일정이 있나요?,오늘은 9시에 회의가 있어요

        주의: 출력에 백슬래시(\)나 따옴표(")를 포함하지 마세요.
    """

    res = chat_with_gpt(prompt, str(random_message))
    question, answer = res.split(',')

    return {
        'question': question,
        'answer': answer
    }


def evaluate_answer(message, user_input):
    # 두 문장의 임베딩 계산
    embedding1 = get_embedding(message)
    embedding2 = get_embedding(user_input)

    # 두 임베딩 사이의 코사인 유사도 계산
    dot_product = np.dot(embedding1, embedding2)
    norm1 = np.linalg.norm(embedding1)
    norm2 = np.linalg.norm(embedding2)

    similarity = dot_product / (norm1 * norm2)


    response = "맞았습니다" if similarity.item()*100>80 else "틀렸습니다"

    return {
        'similarity': round(similarity.item()*100,2),
        'result': response
    }