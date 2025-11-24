from collections import deque

class Garage:
    def __init__(self, capacity):
        self.garage = deque()
        self.capacity = capacity

    def car_arrives(self, car):
        if len(self.garage) < self.capacity:
            self.garage.append(car)
            print(f"{car} arrived. Currend state: {list(self.garage)}")
        else:
            print(f"{car} cannot enter. Garage full. Currend state: {list(self.garage)}")

    def car_leaves(self):
        if self.garage:
            car = self.garage.popleft()
            print(f"{car} left. Currend state: {list(self.garage)}")
            return car
        else:
            print("Garage is empty.")
            return None
        
    def find_car(self, car):
        if car in self.garage:
            position = list(self.garage).index(car) + 1
            print(f"{car} is in the garage at position {position}")
        else:
            print(f"{car} is not in the garage.")

def main():
    GARAGE_CAPACITY = 5
    garage = Garage(GARAGE_CAPACITY)

    garage.car_arrives("Car 1")
    garage.car_arrives("Car 2")
    garage.car_arrives("Car 3")
    garage.car_arrives("Car 4")

    left_car_leaves = garage.car_leaves()
    print(left_car_leaves)

    garage.car_arrives("Car 5")
    garage.car_arrives("Car 6")
    garage.car_arrives("Car 7")

    left_car_leaves = garage.car_leaves()
    left_car_leaves = garage.car_leaves()
    left_car_leaves = garage.car_leaves()
    left_car_leaves = garage.car_leaves()
    left_car_leaves = garage.car_leaves()
    left_car_leaves = garage.car_leaves()
    left_car_leaves = garage.car_leaves()
    left_car_leaves = garage.car_leaves()

if __name__ == "__main__":
    main()