from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi import status

app = FastAPI()

@app.get("/hello")
async def hello():
    return JSONResponse({
        "message": "Hi there! Learning Jenkins!"
    }, status_code=status.HTTP_200_OK)