def simple_generator():
    print("First value.")
    yield 1
    print("Second value")
    yield 2
    print("Third value")
    yield 3

def main():
    gen = simple_generator()
    print(next(gen))
    print("Hello KappaLambda!")
    print(next(gen))
    print("*"*20)
    print(next(gen))

if __name__ == "__main__":
    main()