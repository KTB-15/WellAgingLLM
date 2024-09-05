from func import *


role_message = [
    {"role": "system", "content": "이전의 대화 내용을 토대로 질문을 만들어서 옳게 말하는지 판단하는거야"}
]

messages = load_messages_from_json('message.json')
