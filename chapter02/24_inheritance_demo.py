class Base:
    def __init__(self):
        self.public = "I am a public variable."
        self.__private = "I am a private variable."

    def get_private(self):
        return self.__private

class Derived(Base):
    def __init__(self):
        super().__init__()
        self.new_attr = "I am a derived variable."

def main():
    b = Base()
    print(b.public)
    print(b.get_private())

    d = Derived()
    print(d.public)
    print(d.get_private())
    print(d.new_attr)

if __name__ == "__main__":
    main()