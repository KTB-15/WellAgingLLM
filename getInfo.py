from func import *

qna = []
role_message = [
    {"role": "system", "content": "너는 어르신에게서 정보를 얻는 친근한 지인인거야. 감정 줄이고 사무적으로 대답해줘. 되묻지말고 2문장 이상 말하지 마"}
]
questions = [
    "아까 어떤 음식을 먹었나요?",
    "무엇을 할 예정인가요?",
    "최근 기억에 남는 일이 있나요?"
]


print("세가지 질문을 할게요.")

# 질문을 하나씩 진행하는 루프
for i, question in enumerate(questions):
    print(f"{question}")

    # 사용자 입력 받기
    user_input = input("You: ")

    # GPT 응답 생성
    response = chat_with_gpt(role_message,user_input)

    # 사용자 메시지를 대화 기록에 추가
    qna.append({"Q": question, "A": user_input})

    # GPT의 응답 출력
    print(f"GPT: {response}")

print("대화를 종료합니다. 감사합니다.")

save_messages_to_json(qna, 'messages.json')

