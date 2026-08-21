from enum import Enum, unique

@unique
class Status(Enum):
    ACTIVE = 1
    INACTIVE = 2
    DELETED = 1
