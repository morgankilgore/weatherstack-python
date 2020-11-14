from typing import List

import pydantic

from weatherstack.enums import RequestType, Unit


class Request(pydantic.BaseModel):
    type: RequestType
    query: str
    language: str
    unit: Unit

    class Config:
        use_enum_values = True


class Location(pydantic.BaseModel):
    name: str
    country: str
    region: str
    lat: str
    lon: str
    timezone_id: str
    localtime: str
    localtime_epoch: int
    utc_offset: str


class CurrentWeather(pydantic.BaseModel):
    observation_time: str
    temperature: int
    weather_code: int
    weather_icons: List[str]
    weather_descriptions: List[str]
    wind_speed: int
    wind_degree: int
    wind_dir: str
    pressure: int
    precip: int
    humidity: int
    feelslike: int
    uv_index: int
    visibility: int


class CurrentWeatherResponse(pydantic.BaseModel):
    request: Request
    location: Location
    current: CurrentWeather
