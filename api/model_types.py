from pydantic import BaseModel


# TODO: Find a way to make generics work
class ValueCountInt(BaseModel):
    value: int
    count: int


class ValueCountStr(BaseModel):
    value: str
    count: int


class Duration(BaseModel):
    total: int
    count: int
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
    day: ValueCountInt
    month: ValueCountStr


class TripResponse(BaseModel):
    start: str
    end: str
    count: int
    duration: Duration
    station: Station


class UserResponse(BaseModel):
    type: UserType
    gender: UserGender
    birth: UserBirthInfo


class QueryResponse(BaseModel):
    time: TimeResponse
    trip: TripResponse
    user: UserResponse


class QueryBody(BaseModel):
    city: str
    filter: str
    month: str
    day: str
