def main():
    store_a_products = { "Mangos", "Kiwis", "Papayas", "Peaches", "Melons", "Figs" }
    store_b_products = { "Bananas", "Apples", "Pears", "Cherries", "Figs", "Mangos" }

    # Find common fruits (intersection)
    common_products_1 = store_a_products & store_b_products
    print(common_products_1)

    common_products_2 = store_a_products.intersection(store_b_products)
    print(common_products_2)

    # Find all unique fruits (union)
    all_products_1 = store_a_products | store_b_products
    print(all_products_1)

    all_products_2 = store_a_products.union(store_b_products)
    print(all_products_2)

    # Find fruits in store a but not in store b and the opposite (difference)
    store_a_exclusive = store_a_products - store_b_products
    print(store_a_exclusive)
    store_b_exclusive = store_b_products.difference(store_a_products)
    print(store_b_exclusive)

    # Find fruits that exist in either stores but not in both (symmetric difference)
    unique_products = store_a_products ^ store_b_products
    print(unique_products)
    unique_products = store_a_products.symmetric_difference(store_b_products)

if __name__ == "__main__":
    main()