from datetime import datetime
from typing import List

from pydantic import BaseModel


class WeatherBaseSchema(BaseModel):
    id: str | None = None
    cod_city: int
    date: datetime.date
    hour: int
    precipitation: float | None = None
    dry_bulb_temperature: float | None = None
    wet_bulb_temperature: float | None = None
    high_temperature: float | None = None
    low_temperature: float | None = None
    relative_humidity: float | None = None
    relative_humidity_avg: float | None = None
    pressure: float | None = None
    sea_pressure: float | None = None
    wind_direction: float | None = None
    wind_speed_avg: float | None = None
    cloud_cover: float | None = None
    evaporation: float | None = None

    class Config:
        orm_mode = True


class ListWeatherResponse(BaseModel):
    status: str
    results: int
    notes: List[WeatherBaseSchema]


class CityBaseSchema(BaseModel):
    id: str | None = None
    cod_city: int
    latitude: float | None = None
    longitude: float | None = None
    name_station: str

    class Config:
        orm_mode = True


class ListCityResponse(BaseModel):
    status: str
    results: int
    notes: List[WeatherBaseSchema]
