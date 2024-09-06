import json
from func import chat_with_gpt


def getUserInfo(prompt,user_input):
    # gpt 응답 및 prompt에 대화 내용 저장
    res = chat_with_gpt(prompt, user_input)

    return {
        'statusCode':200,
        'body':json.dumps({'messages':res})
    }


if __name__=="__main__":
    prompt = """
        너는 어르신에게서 일상 정보를 얻는 친근한 지인이야.
        질문과 대답을 토대로 퀴즈를 만들거라서 확실한 질문으로 부탁해.
        모든 대답은 2문장 이하로 말하고, 유의미한 대답을 받으면 새로운 주제로 넘어가서 물어봐.
        한 가지 주제에 대해 연속으로 두 번 이상의 질문은 하지 않도록 해.
        이미 주제에 대해 유의미한 답변을 받았으면 새로운 주제를 다뤄.
        예를 들어, 식사에 대해 유의미한 대답을 받으면 다음으로 취미, 일정, 기념일 등의 주제로 넘어가.
        현재까지의 대화: 안녕하세요! 식사하셨나요? / 
    """

    res = getUserInfo(prompt)
    print(res)





