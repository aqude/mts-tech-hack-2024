from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from endpoints.venue import venue_router
from endpoints.city import city_router
from endpoints.global_event import global_event
from endpoints.user import user_router
from endpoints.organizer import organizer_router
from endpoints.venue import venue_router

app = FastAPI()
app.include_router(user_router)
app.include_router(organizer_router)
app.include_router(venue_router)
app.include_router(city_router)
app.include_router(global_event)
app.include_router(venue_router)


@app.get("/")
async def root():
    return {"message": "Hello World"}
