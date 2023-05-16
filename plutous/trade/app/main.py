from fastapi import APIRouter


app = APIRouter(prefix="/trade", tags=["trade"])


@app.get("/")
async def root():
    return {"message": "Hello World"}

