from fastapi import FastAPI  # Import fastapi
from google import genai  # Import Google Gemini Client
from pydantic import BaseModel  # Import basemodel for abstract base class


app = FastAPI()  # Boilerplate so that FastAPI knows what to run

client = genai.Client(api_key="YOUR API KEY HERE")  # Boilerplate for Gemini


class UserReq(
    BaseModel
):  # This is will be the body of the api post request, so it will contain only a message
    message: str  # the message is a string


@app.post("/")  # on any post request to '/' (This is a decorator by the way)
def api(body: UserReq) -> str:  # perform this function
    response = client.models.generate_content(  # generate some text from Gemini
        model="gemini-2.5-flash",  # with the model gemini-2.5-flash (because it's got nice rate limits
        contents=body.message,  # where the input is the message we provided
    )
    return response.text  # and return the text response from it


if __name__ == "__main__":
    import uvicorn  # import uvicorn (this is the ASGI server that FastAPI uses)
    uvicorn.run(app, host="0.0.0.0", port=8000) # run the app