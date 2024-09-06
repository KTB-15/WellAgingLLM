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

    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    prompt = """
    당신은 어르신과 대화하며 정보를 수집하는 역할입니다. 
    주어진 전체 대화 기록을 바탕으로 하나의 간단하고 답하기 쉬운 질문과 그에 대한 명확한 정답을 생성하세요.

    지침:
    1. 전체 대화 기록을 분석하여 주요 주제와 정보를 파악하세요.
    2. 파악한 정보를 바탕으로 간단하고 답하기 쉬운 질문을 만드세요.
    3. 질문은 한 문장으로, 하나의 주제에 대해서만 물어보세요.
    4. 정답은 대화 기록에서 찾을 수 있는 정보를 사용하되, 명확하고 간결하게 표현하세요.
    5. 정답은 '-다'로 끝나는 문장으로 작성하세요.
    6. 시간 관련 표현(예: "어제", "오늘")은 사용하지 마세요.

    출력 형식:
    질문: [생성된 간단한 질문]
    정답: [명확한 정보 전달 형식의 정답]

    이 형식을 정확히 따라주세요. 추가 설명이나 다른 텍스트는 포함하지 마세요.
    """

    res = chat_with_gpt(prompt, str(chat_history_list))
    # question, answer = res.split(',')

    return {
        # 'question': question,
        # 'answer': answer
        'res': res
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