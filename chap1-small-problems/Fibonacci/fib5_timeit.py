import time

def fib5(n: int) -> int:
    if n == 0: return n  # special case
    last: int = 0  # initially set to fib(0)
    next: int = 1  # initially set to fib(1)
    for _ in range(1, n):
        last, next = next, last + next
    return next

if __name__ == "__main__":
    start_time = time.time()
    print(fib5(10))
    print("--- %s seconds ---" % round((time.time() - start_time),5))
    start_time = time.time()
    print(fib5(20))
    print("--- %s seconds ---" % round((time.time() - start_time),5))
    start_time = time.time()
    print(fib5(30))
    print("--- %s seconds ---" % round((time.time() - start_time),5)) 
    start_time = time.time()  
    print(fib5(40))
    print("--- %s seconds ---" % round((time.time() - start_time),5))
    


