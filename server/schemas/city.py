from pydantic import BaseModel


class CityResponse(BaseModel):
    id: int
    name: str
    short_name: str
    venues: list