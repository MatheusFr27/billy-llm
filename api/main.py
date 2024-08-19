from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from pydantic import BaseModel
from ollama import AsyncClient, Message
from typing import Union
from os import getenv

load_dotenv()

app = FastAPI()

app.add_middleware(
  CORSMiddleware,
  allow_origins=["*"],
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)

class Request(BaseModel):
    messages: list[Message]

class LlmRequest(BaseModel):
    messages: list[object]
    functions: Union[list[object] | None]
    stream: bool

@app.get("/")
def read_root():
    return {"message": "Ok"}


@app.post("/send-message")
async def send_message(messages: Request):
    file = open('instrutions.md')

    messages_chat: list[Message] = [
        {
            "content": file.read(),
            "role": "system",
        }
    ]

    for message in messages.messages:
        new_message: Message = {
            "content": message.get('content'),
            "role": message.get('role'),
        }
        messages_chat.append(new_message)
    
    # tools: list[object] = [
    #     {
    #     'type': 'function',
    #     'function': {
    #       'name': 'criar_usuario',
    #       'description': 'Cria um novo usuário',
    #       'parameters': {
    #         'type': 'object',
    #         'properties': {
    #           'name': {
    #             'type': 'string',
    #             'description': 'nome do usuário',
    #           },
    #         },
    #         'required': ['name'],
    #       },
    #     },
    #   },
    # ]

    response = await AsyncClient(host=getenv('OLLAMA_URL')).chat(model=getenv('MODEL_LLM'), messages=messages_chat, options={ "temperature": 0.5 })
    
    messages_chat.append(response['message'])
    messages_chat.pop(0)

    return {"messages": messages_chat}