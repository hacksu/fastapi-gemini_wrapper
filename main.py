from fastapi import FastAPI
from google import genai
from pydantic import BaseModel




if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)