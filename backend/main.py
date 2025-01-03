from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import requests

PRIVATE_KEY = 'your-private-key'

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class User(BaseModel):
    usernmae: str


@app.post('/authenticate')
async def authenticate(user: User):
    response = requests.put(
        'https://api.chatengine.io/user/me/',
        data={
            'username': user.username,
            'secret': user.username,
            'first_name': user.username,
        },
        headers={
            'Project-KEY': PRIVATE_KEY
        }
    )
