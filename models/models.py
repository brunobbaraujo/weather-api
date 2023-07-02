from fastapi_utils.guid_type import GUID, GUID_SERVER_DEFAULT_POSTGRESQL
from sqlalchemy import Column, Date, Float, Integer, String

from database.database import Base


class WeatherModel(Base):
    __tablename__ = "grid_weather_data"
    cod_city = Column(Integer, primary_key=True, index=True, nullable=False)
    date = Column(Date, index=True, nullable=False)
    hour = Column(Integer, nullable=False)
    precipitation = Column(Float(8), nullable=True)
    dry_bulb_temperature = Column(Float(8), nullable=True)
    wet_bulb_temperature = Column(Float(8), nullable=True)
    high_temperature = Column(Float(8), nullable=True)
    low_temperature = Column(Float(8), nullable=True)
    relative_humidity = Column(Float(8), nullable=True)
    relative_humidity_avg = Column(Float(8), nullable=True)
    pressure = Column(Float(8), nullable=True)
    sea_pressure = Column(Float(8), nullable=True)
    wind_direction = Column(Float(8), nullable=True)
    wind_speed_avg = Column(Float(8), nullable=True)
    cloud_cover = Column(Float(8), nullable=True)
    evaporation = Column(Float(8), nullable=True)


class CityModel(Base):
    __tablename__ = "grid_weather_city"
    cod_city = Column(Integer, primary_key=True, index=True, nullable=False)
    latitude = Column(Float(8), nullable=True)
    longitude = Column(Float(8), nullable=True)
    name_station = Column(String(100), nullable=False)
