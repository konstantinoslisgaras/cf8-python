def fibo(n: int) -> int:
    if n in (0, 1): return n
    return fibo(n-1) + fibo(n-2)

def main():
    print(fibo(5))
    print(fibo(10))
    print(fibo(15))
    print(fibo(20))    

if __name__ == "__main__":
    main()