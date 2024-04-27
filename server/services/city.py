from sqlalchemy import select

from models import City


async def read_cities(session):
    cities = await session.execute(select(City))
    return cities.scalars().all()


async def add_city(session, name):
    city = City(name=name)
    session.add(city)
    await session.commit()
    await session.refresh(city)
    return city


async def delete_city(session, name):
    city = await session.execute(select(City).where(City.name == name))
    city = city.scalars().first()
    if not city:
        return None
    session.delete(city)
    await session.commit()