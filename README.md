# Intro
Build your own free AI assistant that you can query from the web!

# Step 1
Create a virtual environment, please. This is important. You need to do this otherwise I'll be mad

```bash
python -m venv .venv
```

Activate the virtual environment


windows
```bash
./.venv/Scripts/activate
```

mac/linux
```bash
. ./.venv/bin/activate
```

# Step 2

Install dependancies

If you are cool and using `uv`
```bash
uv sync
```

If you are not cool and have not installed `uv`

```bash
pip install -r requirements.txt
```


# Step 3
Let's build the app. Open `main.py`.

It has imports and a listener at the bottom, but nothing in the middle.

First, let's set up the app. Add this around **line 5**:

```python
app = FastAPI()
client = genai.Client(api_key="YOUR API KEY HERE")
```

# Step 4
Next, we need to define what the user sends us. We use Pydantic for this because it's awesome and validates everything for us.

Add this right after the code you just added (around **line 9**):

```python
class UserReq(BaseModel):
    message: str
```

# Step 5
Now for the meat of the app. The API route. This is where the magic happens.

Add this after the UserReq class (around **line 13**):

```python
@app.post("/")
def api(body: UserReq) -> str:
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=body.message,
    )
    return response.text
```

We use gemini-2.5-flash because it's free and has nice rate limits.
This is a POST request, so we need to define what the user sends us, the body of the request (of type UserReq, containing a message!)

# Step 6
Finally, we need a way to run this thing. We use `uvicorn` for that.

**What is Uvicorn?**
FastAPI is an **ASGI** framework (Asynchronous Server Gateway Interface). It's super fast, but it needs an ASGI server to actually talk to the network.

This already exists at the bottom of your file to start the server (around **line 21**):


```python
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

# Step 7
Run it

```bash
uv run main.py
```

```bash
uvicorn main:app --host 127.0.0.1 --port 8000
```

# Step 8
Test it

```bash
curl -X POST http://localhost:8000/ -H "Content-Type: application/json" -d '{"message": "What is 2+2?"}'
```

or on Windows :\( 

```powershell
Invoke-RestMethod -Method Post -Uri http://localhost:8000/ -Body '{"message": "What is 2+2?"}'
```
