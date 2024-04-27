from http.client import HTTPException

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

import services
from core.database import get_session
from schemas.city import CityResponse

city = APIRouter(prefix="/api/city", tags=["City"])


@city.get("/", response_model=list[CityResponse])
async def read_cities(db: AsyncSession = Depends(get_session)):
    cities = await services.read_cities(db)
    return cities


@city.post("/", response_model=CityResponse)
async def add_city(db: AsyncSession = Depends(get_session), city_name: str = ""):
    city = await services.add_city(db, city_name)
    return city


@city.put("/", response_model=CityResponse)
async def delete_city(db: AsyncSession = Depends(get_session), city_name: str = ""):
    element = await services.delete_city(db, city_name)
    if element is None:
        return HTTPException(status_code=404, detail="City not found")
    return element
