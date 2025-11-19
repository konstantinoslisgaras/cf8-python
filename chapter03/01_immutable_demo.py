def print_id(variable_name, variable):
    print(f"id({variable_name}) = {id(variable)}")

def main():
    a = 10
    b = 10

    s1 = "CF8"
    s2 = "Kappa"

    print_id("a", a)
    print_id("b", b)
    print_id("s1", s1)
    print_id("s2", s2)

if __name__ == "__main__":
    main()