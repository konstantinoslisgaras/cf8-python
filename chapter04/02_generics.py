from typing import Sequence, TypeVar, List, Any, Optional

# Declare a generic type variable
T = TypeVar('T')

Number = TypeVar('Number', int, float) # used for numbers

def first(seq: Sequence[T]) -> T:
    """
    Returns the first element of a sequence.
    If the sequence is empty, raises a ValueError.

    Args:
        seq (Sequence[T]): The sequence from which to get the first element.

    Returns:
        T: The first element of the sequence.

    Raises:
        Value: If sequence is empty.
    """
    if not seq:
        raise ValueError("Sequence is empty.")
    else:
        return seq[0]

def last(seq: Sequence[T]) -> T:
    if not seq:
        raise ValueError("Sequence is empty.")
    else:
        return seq[-1]

# my_list = [0, False, "CF8", "", 15]
def count_truthy(elements: List[Any]) -> int:
    return sum(1 for element in elements if element)

def len_str(s: Optional[str] = None) -> int:
    return len(s) if s is not None else 0

def main():
    numbers = [10, 20, 30, 40]
    print(f"First number: {first(numbers)}")
    print(f"Last number: {last(numbers)}")

    try:
        print(f"First number of an empty list: {first([])}")
    except ValueError as e:
        print(e)

    mixed_values = [0, True, False, "CF8", "", 14, None]
    print(f"Truthy values count: {count_truthy(mixed_values)}")

    print(len_str(None))
    print(len_str("Konstantinos"))

if __name__ == "__main__":
    main()