from fastapi import FastAPI
from routes import router as describe_router

app=FastAPI()

app.inlcude_router(describe_router)

@app.get("/")
async def root():
    return {"message":"Welcome to FastAPI Image description API"}