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
Run it

```bash
fastapi dev main.py
```

# Step 4
Test it

```bash
curl -X POST http://localhost:8000/ -H "Content-Type: application/json" -d '{"message": "What is 2+2?"}'
```
