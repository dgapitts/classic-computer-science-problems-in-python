import time

def fib2(n: int) -> int:
    #print("fib2 call for " + str(n))
    if n < 2:  # base case
        return n
    return fib2(n - 2) + fib2(n - 1)  # recursive case

if __name__ == "__main__":
    start_time = time.time()
    print(fib2(10))
    print("--- %s seconds ---" % round((time.time() - start_time),5))
    start_time = time.time()
    print(fib2(20))
    print("--- %s seconds ---" % round((time.time() - start_time),5))
    start_time = time.time()
    print(fib2(30))
    print("--- %s seconds ---" % round((time.time() - start_time),5)) 
    start_time = time.time()  
    print(fib2(40))
    print("--- %s seconds ---" % round((time.time() - start_time),5))
    


