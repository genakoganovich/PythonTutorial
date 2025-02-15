from enum import Enum


class Color(Enum):
    RED = 1
    CRIMSON = 1
    SALMON = 1
    GREEN = 2
    BLUE = 3

if __name__ == '__main__':
    print(Color.RED is Color.CRIMSON)
    print(Color.RED is Color.SALMON)
    print()
    print(Color(1))
    print()
    for color in Color:
        print(color)
