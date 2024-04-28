from fastapi import HTTPException
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

import services
from core.database import get_session
from schemas.city import CityResponse, CityBaseResponse

city = APIRouter(prefix="/api/city", tags=["City"])


@city.get("/", response_model=list[CityResponse])
async def read_cities(db: AsyncSession = Depends(get_session)) -> list[CityResponse]:
    cities = await services.read_cities(db)
    return cities


@city.post("/", response_model=CityBaseResponse)
async def add_city(db: AsyncSession = Depends(get_session), city_name: str = "Moscow") -> CityBaseResponse:
    id_city = await services.add_city(db, city_name)
    return CityBaseResponse(id=id_city)


@city.delete("/", response_model=CityBaseResponse)
async def delete_city(db: AsyncSession = Depends(get_session), city_id: int = 1) -> CityBaseResponse:
    id_city = await services.delete_city(db, city_id)
    if id_city is None:
        raise HTTPException(status_code=404, detail="City not found")
    return CityBaseResponse(id=id_city)




