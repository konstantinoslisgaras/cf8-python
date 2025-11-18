class Temperature:
    def __init__(self, celcius):
        self.__celcius = celcius
    
    # Getter
    def get_celcius(self):
        return self.__celcius

    # Setter
    def set_celcius(self, value):
        if value < -273.15:
            raise ValueError("Below absolute zero.")
        else:
            self.__celcius = value

    # Deleter
    def del_celcius(self):
        del self.__celcius

    # Full property attributes (for presentation only - do not use)
    celcius = property(
        fget = get_celcius,
        fset = set_celcius,
        fdel = del_celcius,
        doc = "Temperature in Celcius."
    )

def main():
    temp = Temperature(25)
    print(temp.get_celcius())
    temp.celcius = 100
    print(temp.celcius)
    temp.set_celcius(200)
    print(temp.celcius)

if __name__ == "__main__":
    main()