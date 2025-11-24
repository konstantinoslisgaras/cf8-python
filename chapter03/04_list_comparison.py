def compare_lists(listA: list, listB: list) -> None:
    """
    Compare two lists for identity equality.

    Args:
        listA (list): The first list to compare.
        listB (list): The second list to compare.

    Returns:
        None
    """
    # Check if lists are the same object (identity)
    print(f"{listA} is {listB}: {listA is listB}")

    # Check if lists have the same content (equality)
    print(f"{listA} == {listB}: {listA == listB}")

def main():
    a_list = [1, 2, 3]
    b_list = [1, 2, 3]

    compare_lists(a_list, b_list)
    

if __name__ == "__main__":
    main()