from fastapi import FastAPI
from google import genai
from pydantic import BaseModel


app = FastAPI()

client = genai.Client(api_key="AIzaSyCqK6zl54EIAGHgwmgYa_rJPXNXYX-ahfM")


class UserReq(BaseModel):
    message: str


@app.post("/")
def api(body: UserReq) -> str:
    response = client.models.generate_content(
        model="gemini-2.5-flash", contents=body.message
    )
    return response.text
