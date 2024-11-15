from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
from .schemas import Blog


app = FastAPI()


@app.post('/')
def home(request: Blog):
    return {"msg", f"{request.title},'content': {request.content}"}


if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8000)
