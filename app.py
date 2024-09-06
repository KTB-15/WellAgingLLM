from fastapi import FastAPI
from models import *
from services import *

app = FastAPI()

@app.post("/getuserinfo/")
async def getuserinfo(user_info: UserRequest):
    result = getUserInfo(user_info.prompt, user_info.user_input)
    return result

@app.post("/makeqna/")
async def makeqna(chat_history: QuestionRequest):
    result = makeQnA(chat_history)
    return result

@app.post("/evaluateanswer")
async def evaluateanswer(sentences: SentenceRequest):
    result = evaluate_answer(sentences.message, sentences.user_input)
    return result