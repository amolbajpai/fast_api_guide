from fastapi import  FastAPI
from pydantic import BaseModel
import uvicorn


app = FastAPI()

@app.get('/')
def home():
    return {"msg", "Jai Shri Ram"}


if __name__ == '__main__':
    uvicorn.run(app,host="127.0.0.1",port=8000)