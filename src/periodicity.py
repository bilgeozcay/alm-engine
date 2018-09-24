from enum import Enum, auto


class Periodicity(Enum):
    MONTHLY = 1
    QUARTERLY = 3
    SEMI_ANNUAL = 6
    ANNUAL = 12