from enum import Enum


class Color(Enum):
    pass


class RGB(Color):
    RED = 1
    GREEN = 2
    BLUE = 3

class RGBA(RGB):
    ALPHA = 4