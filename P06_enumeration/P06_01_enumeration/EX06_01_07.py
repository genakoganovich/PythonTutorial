from color_enum import Color

if __name__ == '__main__':
    print(Color.RED)
    print(Color['RED'])
    print(Color(1))
    print(Color['RED'] == Color(1))
    print(Color['RED'] is Color(1))