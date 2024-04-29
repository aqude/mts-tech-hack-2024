# from fastapi import APIRouter, Depends
# from sqlalchemy.ext.asyncio import AsyncSession
#
# from core.database import get_session
#
# global_event = APIRouter(prefix="/api/global_event", tags=["GlobalEvent"])
#
# @global_event.get("/")
# async def read_global_events(db: AsyncSession = Depends(get_session)):
#     pass
#
# @global_event.post("/")
# async def add_global_event():
#     pass
#
# @global_event.put("/")
# async def update_global_event():
#     pass
#
# @global_event.delete("/")
# async def delete_global_event():
#     pass
# @global_event.get("/")
# async def get_global_event_by_date():
#     pass
#
# @global_event.get("/")
# async def get_global_event_by_city():
#     pass
#
# @global_event.get("/")
# async def get_global_event_by_venue():
#     pass
#
# @global_event.get("/")
# async def get_global_event_by_organizer():
#     pass
#
# @global_event.get("/")
# async def get_global_event_by_user():
#     pass
#
# @global_event.get("/")
# async def get_global_event_by_tag():
#     pass
