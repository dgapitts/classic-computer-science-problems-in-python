## fib1.py 1st attempt at a recursive solution 

I added a simple print(n):

```
[~/projects/classic-problems-python/chap1-small-problems] # cat fib1.py
def fib1(n: int) -> int:
    print(n)
    return fib1(n - 1) + fib1(n - 2)

if __name__ == "__main__":
    print(fib1(5))

```

and we can see the "RecursionError: maximum recursion depth" happens around the 998th/999th call 

```
[~/projects/classic-problems-python/chap1-small-problems] # python3 fib1.py  &> fib1.log
[~/projects/classic-problems-python/chap1-small-problems] # head fib1.log
5
4
3
2
1
0
-1
-2
-3
-4
[~/projects/classic-problems-python/chap1-small-problems] # tail fib1.log 
    return fib1(n - 1) + fib1(n - 2)
  File "fib1.py", line 3, in fib1
    return fib1(n - 1) + fib1(n - 2)
  File "fib1.py", line 3, in fib1
    return fib1(n - 1) + fib1(n - 2)
  File "fib1.py", line 3, in fib1
    return fib1(n - 1) + fib1(n - 2)
  File "fib1.py", line 2, in fib1
    print(n)
RecursionError: maximum recursion depth exceeded while getting the str of an object
[~/projects/classic-problems-python/chap1-small-problems] # less fib1.log
[~/projects/classic-problems-python/chap1-small-problems] # head -1000 fib1.log|tail 
-985
-986
-987
-988
-989
-990
-991
-992
Traceback (most recent call last):
  File "fib1.py", line 6, in <module>
[~/projects/classic-problems-python/chap1-small-problems] #  echo '5-(-992)'|bc
997
```

## fib2.py showing repeated calls

Again adding a debug/print statement
```
[~/projects/classic-problems-python/chap1-small-problems] # cat fib2.py 
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
```
we can now see the explicit repeat calls   

```
[~/projects/classic-problems-python/chap1-small-problems] # python3 fib2.py 
fib2 call for 2
fib2 call for 0
fib2 call for 1
1
fib2 call for 3
fib2 call for 1
fib2 call for 2
fib2 call for 0
fib2 call for 1
2
fib2 call for 4
fib2 call for 2
fib2 call for 0
fib2 call for 1
fib2 call for 3
fib2 call for 1
fib2 call for 2
fib2 call for 0
fib2 call for 1
3
fib2 call for 5
fib2 call for 3
fib2 call for 1
fib2 call for 2
fib2 call for 0
fib2 call for 1
fib2 call for 4
fib2 call for 2
fib2 call for 0
fib2 call for 1
fib2 call for 3
fib2 call for 1
fib2 call for 2
fib2 call for 0
fib2 call for 1
5
```


## fib2_timeit.py showing repeated calls
Ref: https://stackoverflow.com/questions/1557571/how-do-i-get-time-of-a-python-programs-execution
Next adding some simple clock timings for executions of fib10, fib20, fib30, fib40
```
[~/projects/classic-problems-python/chap1-small-problems] # cat fib2_timeit.py 
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
```    

and we can see the exponential time growth:

```
[~/projects/classic-problems-python/chap1-small-problems] # python3 fib2_timeit.py 
55
--- 6e-05 seconds ---
6765
--- 0.00326 seconds ---
832040
--- 0.32899 seconds ---
102334155
--- 40.63359 seconds ---
```

## fib3 adding a Dict to cache interim call results - very fast even for 40th element of fib sequence

```
[~/projects/classic-problems-python/chap1-small-problems] # cat fib3_timeit.py 
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
```

now exec times are flat

```
[~/projects/classic-problems-python/chap1-small-problems] # python3 fib3_timeit.py 
55
--- 3e-05 seconds ---
6765
--- 1e-05 seconds ---
832040
--- 1e-05 seconds ---
102334155
--- 1e-05 seconds ---
```

## fib4 lru_cache for automatic memorization of previous calls

```
[~/projects/classic-problems-python/chap1-small-problems] # cat fib4_timeit.py 
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
```    
exec times are flat again
```
[~/projects/classic-problems-python/chap1-small-problems] # python3 fib4_timeit.py 
55
--- 3e-05 seconds ---
6765
--- 1e-05 seconds ---
832040
--- 1e-05 seconds ---
102334155
--- 1e-05 seconds ---
```


## fib5 and yes there is a simple iterative solution

```
[~/projects/classic-problems-python/chap1-small-problems/Fibonacci] # cat fib5_timeit.py 
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
```

again exec times are flat
```
[~/projects/classic-problems-python/chap1-small-problems/Fibonacci] # python3 fib3_timeit.py 
55
--- 3e-05 seconds ---
6765
--- 1e-05 seconds ---
832040
--- 1e-05 seconds ---
102334155
--- 1e-05 seconds ---
```


