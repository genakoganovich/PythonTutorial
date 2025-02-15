class Point2D:
    __slots__ = ('x', 'y')

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Point2D({self.x},{self.y})'


if __name__ == '__main__':
    point = Point2D(0, 0)
    print(point.__slots__)
    point.z = 0
