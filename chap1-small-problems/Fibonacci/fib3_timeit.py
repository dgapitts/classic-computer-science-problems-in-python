import time
from typing import Dict

#memo: Dict[int, int] 
memo = {0: 0, 1: 1}  # our base cases

def fib3(n: int) -> int:
    if n not in memo:
        memo[n] = fib3(n - 1) + fib3(n - 2)  # memoization
    return memo[n]

if __name__ == "__main__":
    start_time = time.time()
    print(fib3(10))
    print("--- %s seconds ---" % round((time.time() - start_time),5))
    start_time = time.time()
    print(fib3(20))
    print("--- %s seconds ---" % round((time.time() - start_time),5))
    start_time = time.time()
    print(fib3(30))
    print("--- %s seconds ---" % round((time.time() - start_time),5)) 
    start_time = time.time()  
    print(fib3(40))
    print("--- %s seconds ---" % round((time.time() - start_time),5))
    


