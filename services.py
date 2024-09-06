import json

import numpy as np
from func import *

def getUserInfo(prompt,user_input):
    # gpt 응답 및 prompt에 대화 내용 저장
    res = chat_with_gpt(prompt, user_input)

    return {'body':res}


def makeQnA(chat_history):
    prompt = """
        당신은 어르신과 대화하며 정보를 수집하는 역할입니다. 
        주어진 전체 대화 기록을 바탕으로 **세 개의 간단하고 답하기 쉬운 질문과 그에 대한 명확한 정답**을 생성하세요.

        지침:
        1. 전체 대화 기록을 분석하여 주요 주제와 정보를 파악하세요.
        2. 파악한 정보를 바탕으로 질문을 생성할 때, 최근에 다룬 주제와 연관된 문맥을 반영하세요.
        3. 질문은 한 문장으로, 하나의 주제에 대해서만 물어보세요.
        4. **정답은 반드시 '-다'로 끝나는 문장으로 작성하세요.**
        5. 정답은 대화 기록에서 찾을 수 있는 정보를 사용하되, 명확하고 간결하게 표현하세요.
        6. 질문과 정답은 **쉼표**나 **기타 구두점** 없이 순수한 텍스트로만 작성하세요.
        7. 시간 관련 표현(예: "어제", "오늘")은 사용하지 마세요.

        출력 형식은 **JSON** 형식으로 반환하세요:
        [
            {"Q": "첫 번째 질문", "A": "첫 번째 정답"},
            {"Q": "두 번째 질문", "A": "두 번째 정답"},
            {"Q": "세 번째 질문", "A": "세 번째 정답"}
        ]

        **추가 설명이나 다른 텍스트는 절대 포함하지 마세요.**
    """

    res = chat_with_gpt(prompt, str(chat_history))
    response = json.loads(res)


    return response


def evaluate_answer(message, user_input):
    # 두 문장의 임베딩 계산
    embedding1 = get_embedding(message)
    embedding2 = get_embedding(user_input)

    # 두 임베딩 사이의 코사인 유사도 계산
    dot_product = np.dot(embedding1, embedding2)
    norm1 = np.linalg.norm(embedding1)
    norm2 = np.linalg.norm(embedding2)

    similarity = dot_product / (norm1 * norm2)


    response = "맞았습니다" if similarity.item()*100>87 else "틀렸습니다"

    return {
        'similarity': round(similarity.item()*100,2),
        'result': response
    }