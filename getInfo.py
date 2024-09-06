from func import *
from datetime import datetime




qna = load_messages_from_json('messages.json')
prompt = [
    {"role": "system", "content": '너는 어르신에게서 일상 정보를 얻는 친근한 지인이야.'
        '질문과 대답을 토대로 퀴즈를 만들거라서 확실한 질문으로 부탁해.'
        '모든 대답은 2문장 이하로 말하고, 유의미한 대답을 받으면 새로운 주제로 넘어가서 물어봐.'
        '한 가지 주제에 대해 연속으로 두 번 이상의 질문은 하지 않도록 해.'
        '이미 주제에 대해 유의미한 답변을 받았으면 새로운 주제를 다뤄.'
        '예를 들어, 식사에 대해 유의미한 대답을 받으면 다음으로 취미, 일정, 기념일 등의 주제로 넘어가.'
        '현재까지의 대화: 안녕하세요! 식사하셨나요?'
     }
]

total_char = 0

print('안녕하세요! 식사하셨나요?')

while True:
    # 사용자 입력 받기
    user_input = input("You: ")
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    prompt[0]["content"] += user_input
    # 사용자 메시지를 대화 기록에 추가
    qna.append({
        "Q": question,
        "A": user_input,
        "T": current_time
    })

    # GPT 응답 생성
    question = chat_with_gpt(prompt, user_input)
    prompt[0]["content"] += question

    # GPT의 응답 출력
    print(f"GPT: {question}")

    # 응답 글자수가 300개를 넘으면 종료
    total_char += len(question)
    if total_char > 300:
        print('대화를 종료합니다')
        break

# 대화 내용을 JSON 파일로 저장
save_messages_to_json(qna, 'messages.json')