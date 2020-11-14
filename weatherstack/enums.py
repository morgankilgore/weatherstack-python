import enum


class Unit(enum.Enum):
    f = 'f'
    m = 'm'
    s = 's'


class RequestType(enum.Enum):
    City = 'City'
    LatLon = 'LatLon'
    IP = 'IP'
    Zipcode = 'Zipcode'
