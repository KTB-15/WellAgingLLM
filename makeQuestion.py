import random
from func import *

# JSON 파일에서 데이터 로드 및 랜덤 질문 선택
messages = load_messages_from_json('messages.json')
random_message = random.choice(messages)

question = generate_question_from_data(str(random_message))
print(question[0])
user_input = input("You: ")

print(f"답안: {question[1]}")

similarity, result = evaluate_answer(question[1], user_input)
print(result)
print(f"유사도:{similarity}")
