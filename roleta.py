from typing import Sequence
from dataclasses import dataclass
from random import randint

def number_position_table(number):
    col = (number - 1 ) // 3
    line = (number - 1) % 3
    return col, line

DEFAULT_NUMBERS = (
    0,
    32,
    15,
    19,
    4,
    21,
    2,
    25,
    17,
    34,
    6,
    27,
    13,
    36,
    11,
    30,
    8,
    23,
    10,
    5,
    24,
    16,
    33,
    1,
    20,
    14,
    31,
    9,
    22,
    18,
    29,
    7,
    28,
    12,
    35,
    3,
    26,
)

DEFAULT_RED_NUMBERS = tuple(DEFAULT_NUMBERS[1::2])
DEFAULT_BLACK_NUMBERS = tuple(DEFAULT_NUMBERS[2::2])

class InvalidBet(Exception):
    pass

@dataclass
class Bet:
    value: float
    numbers: Sequence[int]
    
    @classmethod
    def create_black(cls, value: float):
        return cls(value=value, numbers=set(DEFAULT_BLACK_NUMBERS))
    
    @classmethod
    def create_red(cls, value: float):
        return cls(value=value, numbers=set(DEFAULT_RED_NUMBERS))
    
    @classmethod
    def create_from_filter(cls, value: float, fn):
        return cls(
            value=value,
            numbers=set(filter(fn, DEFAULT_NUMBERS[1:]))
        )
    
    @classmethod
    def create_odd(cls, value: float):
        return cls.create_from_filter(value, lambda it: it % 2 == 1)
    
    @classmethod
    def create_even(cls, value: float):
        return cls.create_from_filter(value, lambda it: it % 2 == 0)
    
    @classmethod
    def create_from_range(cls, value: float, range):
        return cls(value, set(range))

    @classmethod
    def create_low_range(cls, value: float):
        return cls.create_from_range(value, range(1, 19))
    
    @classmethod
    def create_high_range(cls, value: float):
        return cls.create_from_range(value, range(19, 37))

class Roulette:
    random_number: int
    
    @classmethod
    def get_random_number(cls):
        return cls.random_number(randint(0, 36))
    
