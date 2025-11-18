import math

class Point:
    """
    A class representing a point in a 2D space.
    
    Attrubutes:
        x (float): The x-coordinate of the point.
        y (float): The y-coordinate of the point.
    """

    def __init__(self, x: float = 0, y: float = 0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"
    
    def distance_to(self, other):
        return math.sqrt(math.pow(self.x - other.x, 2) + math.pow(self.y - other.y, 2))

def main():
    p1 = Point(0, 3)
    p2 = Point(4, 0)
    print(f"Point 1x: {p1.x}")
    print(p1)
    print(p1.distance_to(p2))

if __name__ == "__main__":
    main()