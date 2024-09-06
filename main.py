import json
from func import chat_with_gpt
from datetime import datetime


def getUserInfo(prompt,user_input):
    # gpt 응답 및 prompt에 대화 내용 저장
    res = chat_with_gpt(prompt, user_input)

    return {
        'statusCode':200,
        'body':json.dumps({'messages':res})
    }

if __name__=="__main__":
    # prompt1 = """
    #     너는 어르신에게서 일상 정보를 얻는 친근한 지인이야.
    #     질문과 대답을 토대로 퀴즈를 만들거라서 확실한 질문으로 부탁해.
    #     모든 대답은 2문장 이하로 말하고, 유의미한 대답을 받으면 새로운 주제로 넘어가서 물어봐.
    #     한 가지 주제에 대해 연속으로 두 번 이상의 질문은 하지 않도록 해.
    #     이미 주제에 대해 유의미한 답변을 받았으면 새로운 주제를 다뤄.
    #     예를 들어, 식사에 대해 유의미한 대답을 받으면 다음으로 취미, 일정, 기념일 등의 주제로 넘어가.
    #     현재까지의 대화: 안녕하세요! 식사하셨나요? /
    # """
    #
    # res = getUserInfo(prompt1)
    # print(res)

    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    prompt2 = f"""
        다음 데이터를 기반으로 쉽게 대답할 수 있는 질문과 답을 알려줘. 
        데이터에 포함된 날짜 정보와 현재 시간({current_time})을 비교해서, 
        1. 데이터가 어제에 해당하면 "어제"라는 표현을 사용한 질문을 만들고, 오늘에 해당하면 "오늘"이라는 표현을 사용해 질문을 만들어.
        2. 만약 전날에 "내일 무엇을 해야 하는지"에 대한 정보가 있으면, 이를 바탕으로 "오늘 무엇을 해야 하는지"라는 질문을 만들어.
        3. 1,2번을 만족하면서 질문의 문맥이 자연스럽도록 신경써
        반환 형식은 "질문,정답" 형식이어야 해.
    """



