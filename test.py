from services import *

prompt = """
당신은 어르신과 친근하게 대화를 나누는 상대입니다. 
다음 지침을 따라 자연스럽고 가벼운 대화를 이어가세요:

1. 질문은 간단하고 친근하게 하되, 일상적인 대화 흐름을 유지하세요.

2. 다음 주제들을 골고루 다루며 대화를 이어가세요:
   - 일상 활동 및 취미
   - 최근의 경험이나 사건
   - 가족이나 친구 관계
   - 날씨나 계절에 대한 이야기
   - 가벼운 시사 이야기
   - 즐거운 추억

3. **한 주제에 대해 1-2번 이상 질문하지 마세요. 새로운 주제로 자연스럽게 전환하세요.**

4. **어르신의 답변에 1-2문장으로 짧게 반응하고 즉시 새로운 질문으로 넘어가세요.**

5. 각 응답은 다음 구조를 따르세요:
   [짧은 반응] + [새로운 주제로의 질문]

6. **대화의 흐름을 자연스럽게 유지하되, 5개의 서로 다른 주제를 다루도록 하세요.**

현재까지의 대화: 안녕하세요! 요즘 날씨 어떤가요? /
"""

messages = []
count = 0
question = '안녕하세요! 요즘 날씨 어떤가요?'
print(question)

while True:
    user_input = input()

    messages.append({
        'Q':question,
        'A':user_input
    })

    if count>300:
        print('대화를 종료합니다')
        break
    response = getUserInfo(prompt, user_input)
    question = response['body']
    count += len(question)
    print(question)

    # 대화내용을 프롬프트에 저장
    prompt += user_input+' /'
    prompt += question + ' /'

# 대화 기록을 JSON 파일로 저장
with open('messages.json', 'w', encoding='utf-8') as f:
    json.dump(messages, f, ensure_ascii=False, indent=4)
# JSON 불러오기
with open('messages.json', 'r', encoding='utf-8') as f:
    messages = json.load(f)

qnas = makeQnA(messages)

for item in qnas:
    print(item['Q'])
    user_input = input()

    res = evaluate_answer(item['A'], user_input)
    print(res['result'])
    print(res['similarity'])