from fastapi import FastAPI
from pydantic import BaseModel
from app.chatbot.chatbot_core import chatbot_response

app = FastAPI()

class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
def chat_api(req: ChatRequest):
    response_text = chatbot_response(req.message)
    return {"response": response_text}
# backend main placeholder
