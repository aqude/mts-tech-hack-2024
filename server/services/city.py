from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from models import City


async def read_cities(db: AsyncSession) -> list[City]:
    cities = await db.execute(select(City).options(selectinload(City.venues)))
    return cities.scalars().all()


async def add_city(db: AsyncSession, name) -> int:
    city = City(name=name)
    db.add(city)
    await db.commit()
    await db.refresh(city)
    return city.id


async def delete_city(db: AsyncSession, city_id: int) -> int | None:
    city = await db.execute(
        select(City).options(selectinload(City.venues)).where(City.id == city_id)
    )
    city = city.scalar()
    if not city:
        return None
    await db.delete(city)
    await db.commit()
    return city.id
