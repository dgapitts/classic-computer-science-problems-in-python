def fib2(n: int) -> int:
    print("fib2 call for " + str(n))
    if n < 2:  # base case
        return n
    return fib2(n - 2) + fib2(n - 1)  # recursive case

if __name__ == "__main__":
    print(fib2(2))
    print(fib2(3))
    print(fib2(4))
    print(fib2(5))

    

    


