from pydantic import BaseModel


class CityBaseResponse(BaseModel):
    id: int


class CityResponse(CityBaseResponse):
    name: str
    venues: list
