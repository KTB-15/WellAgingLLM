from typing import List
from pydantic import BaseModel

class UserRequest(BaseModel):
    prompt: str
    user_input: str

class ChatItem(BaseModel):
    Q: str
    A: str

class QuestionRequest(BaseModel):
    chat_history: List[ChatItem]

class SentenceRequest(BaseModel):
    message: str
    user_input: str