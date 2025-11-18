class Point:
    __count = 0

    def __init__(self, x: float = 0, y: float = 0):
        self.__x = x
        self.__y = y
        Point.__count += 1

    def __repr__(self):
        return f"Point(x={self.__x}, y={self.__y})"
    
    def __str__(self):
        return f"({self.__x}, {self.__y})"
    
    def __eq__(self, other):
        if isinstance(other, Point):
            return self.__x == other.__x and self.__y == other.__y
        else:
            return False
        
    @classmethod
    def get_count(cls):
        return cls.__count

def main():
    p1 = Point(10, 20)
    p2 = Point(10, 20)
    p3 = Point(20, 40)
    print(p1 == p2)
    print(Point.get_count())
    print(p1.x)
    p1.x = 100

if __name__ == "__main__":
    main()