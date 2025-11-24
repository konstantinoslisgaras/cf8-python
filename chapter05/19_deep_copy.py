import copy

def main():
    ages = [10, [20, 30, 40], 50]

    # 1. Shallow copy using list slicing.
    ages_slice = ages[:]

    # 2. Shallow copy using copy() method from lists.
    ages_cp = ages.copy()

    # 3. Shallow copy using the list constructor.
    ages_list = list(ages)

    # 4. Deep copy using deepcopy() method from copy module.
    ages_dc = copy.deepcopy(ages)


    ages[0] = 100
    ages[1][0] = 200

    print(f"ages: {ages}")
    print(f"ages_slice: {ages_slice}")
    print(f"ages_cp: {ages_cp}")
    print(f"ages_list: {ages_list}")
    print(f"ages_dc: {ages_dc}")

if __name__ == "__main__":
    main()