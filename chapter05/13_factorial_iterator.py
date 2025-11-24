class FactoIterator:
    def __init__(self, n):
        """
        Initialize the iterator with the given number n.

        Params:
            n (int): The number up to which factorials are generated.
        """
        self.n = n
        self.result = 1
        self.order = 1

    def __iter__(self):
        """
        Return the iterator object itself.

        Returns:
            self (FactoIterator): The iterator object itself.
        """
        return self
    
    def __next__(self):
        """
        Returns the next factorial in the sequence.

        Returns:
            int: The next factorial in the sequence.

        Raises:
            StopIteration: When the sequence is complete.
        """
        if self.order > self.n:
            raise StopIteration
        
        self.result *= self.order
        self.order += 1
        return self.result
    
def main():
    factor_iter = FactoIterator(6)

    a = next(factor_iter)
    print(f"a = {a}")

    for factorial in factor_iter:
        print(factorial)

if __name__ == "__main__":
    main()