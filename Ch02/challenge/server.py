"""Write an /info handler that will return a JSON object with:

- version: string, say "0.1.0"
- time: the current time in ISO format
- user: The user running the application (hint: USER environment variable)
"""
from fastapi import FastAPI
from datetime import datetime
import os

app = FastAPI()


@app.get('/info')
async def now():
    return {
        "version": "0.1.0",
        "time": datetime.now().isoformat(),
        "user": os.environ.get("USER", ""),
    }

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app)
