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
            다음 데이터를 기반으로 쉽게 대답할 수 있는 질문과 답을 알려줘.
            데이터에 포함된 날짜 정보와 현재 시간({current_time})을 비교해서,
            1. 데이터가 어제에 해당하면 "어제"라는 표현을 사용한 질문을 만들고, 오늘에 해당하면 "오늘"이라는 표현을 사용해 질문을 만들어.
            2. 만약 전날에 "내일 무엇을 해야 하는지"에 대한 정보가 있으면, 이를 바탕으로 "오늘 무엇을 해야 하는지"라는 질문을 만들어.
            3. 1,2번을 만족하면서 질문의 문맥이 자연스럽도록 신경쓰면서 \는 넣지마 
            반환 형식은 "질문,정답" 형식이어야 해.
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