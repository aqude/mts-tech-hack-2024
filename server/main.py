from fastapi import FastAPI
from endpoints.user import user_router
from endpoints.organizer import organizer_router
from endpoints.venue import venue_router

app = FastAPI()
app.include_router(user_router)
app.include_router(organizer_router)
app.include_router(venue_router)


@app.get("/")
async def root():
    return {"message": "Hello World"}
