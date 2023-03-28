from pydantic import BaseModel
from typing import Optional


# TODO: Convert to generic
class ValueCountInt(BaseModel):
    value: int
    count: int


class ValueCountStr(BaseModel):
    value: str
    count: int


class Duration(BaseModel):
    total: int
    avg: int


class Station(BaseModel):
    start: ValueCountStr
    end: ValueCountStr


class UserType(BaseModel):
    subscriber: int
    customer: int


class UserGender(BaseModel):
    male: int
    female: int


class UserBirthInfo(BaseModel):
    earliest: int
    latest: int
    mode: int


class TimeResponse(BaseModel):
    hour: ValueCountInt
    day: Optional[ValueCountStr]
    month: Optional[ValueCountInt]


class TripResponse(BaseModel):
    full_trip: str
    count: int
    duration: Duration
    station: Station


class UserResponse(BaseModel):
    total: int
    type: UserType
    gender: Optional[UserGender]
    birth: Optional[UserBirthInfo]


class QueryBody(BaseModel):
    city: str
    filter: str
    month: int
    day: str


class StatusResponse(BaseModel):
    status: str
    code: int
    message: Optional[str]
