import random
from datetime import datetime
from func import *

# JSON 파일에서 데이터 로드 및 랜덤 질문 선택
messages = load_messages_from_json('messages.json')
random_message = random.choice(messages)

current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

prompt = f"""
    다음 데이터를 기반으로 쉽게 대답할 수 있는 질문과 답을 알려줘. 
    데이터에 포함된 날짜 정보와 현재 시간({current_time})을 비교해서, 
    1. 데이터가 어제에 해당하면 "어제"라는 표현을 사용한 질문을 만들고, 오늘에 해당하면 "오늘"이라는 표현을 사용해 질문을 만들어.
    2. 만약 전날에 "내일 무엇을 해야 하는지"에 대한 정보가 있으면, 이를 바탕으로 "오늘 무엇을 해야 하는지"라는 질문을 만들어.
    반환 형식은 "질문,정답" 형식이어야 해.
"""

res = chat_with_gpt(prompt, str(random_message))

question, answer = res.split(',')

print(question)
user_input = input("You: ")
print(f"답안: {answer}")

result, similarity = evaluate_answer(answer, user_input)

if result:
    print('맞았습니다')
    # messages.remove(random_message)
    # save_messages_to_json(messages, 'messages.json')
else:
    print('틀렸습니다')

print(f"유사도:{similarity}")
