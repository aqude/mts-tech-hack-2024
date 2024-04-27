from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from endpoints.user import user_router

app = FastAPI()
app.include_router(user_router)


@app.get("/")
async def root():
    return {"message": "Hello World"}
