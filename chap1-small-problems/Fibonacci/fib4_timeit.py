import time
 
from functools import lru_cache
@lru_cache(maxsize=None)
def fib4(n: int) -> int:  # same definition as fib2()
    if n < 2:  # base case
        return n
    return fib4(n - 2) + fib4(n - 1)  # recursive case

if __name__ == "__main__":
    start_time = time.time()
    print(fib4(10))
    print("--- %s seconds ---" % round((time.time() - start_time),5))
    start_time = time.time()
    print(fib4(20))
    print("--- %s seconds ---" % round((time.time() - start_time),5))
    start_time = time.time()
    print(fib4(30))
    print("--- %s seconds ---" % round((time.time() - start_time),5)) 
    start_time = time.time()  
    print(fib4(40))
    print("--- %s seconds ---" % round((time.time() - start_time),5))
    


