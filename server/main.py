from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from endpoints.city import city
from endpoints.global_event import global_event
from endpoints.user import user_router

app = FastAPI()
app.include_router(user_router)
app.include_router(city)
app.include_router(global_event)


@app.get("/")
async def root():
    return {"message": "Hello World"}
