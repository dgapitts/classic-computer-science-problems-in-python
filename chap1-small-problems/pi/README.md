## calculate_pi.py via Leibniz formula

I didn't know about the "Leibniz formula for pi", I enjoyed (i.e. very elegant but a bit too sophisticated for me) the proof in https://en.wikipedia.org/wiki/Leibniz_formula_for_%CF%80 

I tweaked the code to review the rate of convergency of the first 1000 steps in the sequence

```
[~/projects/classic-problems-python/chap1-small-problems/pi] # cat calculate_pi.py 
def calculate_pi(n_terms: int) -> float:
    numerator: float = 4.0
    denominator: float = 1.0
    operation: float = 1.0
    pi: float = 0.0
    for step in range(n_terms):
        pi += operation * (numerator / denominator)
        denominator += 2.0
        operation *= -1.0
        print( str(pi) + " - interim result at sequence step  "  +str(step)  )
    return pi

if __name__ == "__main__":
    print(calculate_pi(1000))
```

and the rate of convergence is not that fast

```
[~/projects/classic-problems-python/chap1-small-problems/pi] # time python3.9 calculate_pi.py  
4.0 - interim result at sequence step  0
2.666666666666667 - interim result at sequence step  1
3.466666666666667 - interim result at sequence step  2
2.8952380952380956 - interim result at sequence step  3
3.3396825396825403 - interim result at sequence step  4
2.9760461760461765 - interim result at sequence step  5
3.2837384837384844 - interim result at sequence step  6
3.017071817071818 - interim result at sequence step  7
3.2523659347188767 - interim result at sequence step  8
3.0418396189294032 - interim result at sequence step  9
3.232315809405594 - interim result at sequence step  10
3.058402765927333 - interim result at sequence step  11
3.2184027659273333 - interim result at sequence step  12
3.0702546177791854 - interim result at sequence step  13
3.208185652261944 - interim result at sequence step  14
3.079153394197428 - interim result at sequence step  15
3.200365515409549 - interim result at sequence step  16
3.0860798011238346 - interim result at sequence step  17
3.1941879092319425 - interim result at sequence step  18
3.09162380666784 - interim result at sequence step  19
3.189184782277596 - interim result at sequence step  20
3.0961615264636424 - interim result at sequence step  21
3.1850504153525314 - interim result at sequence step  22
3.099944032373808 - interim result at sequence step  23
3.1815766854350325 - interim result at sequence step  24
3.1031453128860127 - interim result at sequence step  25
3.1786170109992202 - interim result at sequence step  26
3.1058897382719475 - interim result at sequence step  27
3.1760651768684385 - interim result at sequence step  28
3.108268566698947 - interim result at sequence step  29
3.1738423371907505 - interim result at sequence step  30
3.110350273698687 - interim result at sequence step  31
3.1718887352371485 - interim result at sequence step  32
3.112187242699835 - interim result at sequence step  33
3.1701582571925884 - interim result at sequence step  34
3.1138202290235744 - interim result at sequence step  35
3.1686147495715193 - interim result at sequence step  36
3.115281416238186 - interim result at sequence step  37
3.167229468186238 - interim result at sequence step  38
3.116596556793833 - interim result at sequence step  39
3.1659792728432157 - interim result at sequence step  40
3.117786501758878 - interim result at sequence step  41
3.1648453252882898 - interim result at sequence step  42
3.118868313794037 - interim result at sequence step  43
3.163812134018756 - interim result at sequence step  44
3.1198560900627124 - interim result at sequence step  45
3.1628668427508844 - interim result at sequence step  46
3.1207615795929895 - interim result at sequence step  47
3.161998692995051 - interim result at sequence step  48
3.121594652591011 - interim result at sequence step  49
3.1611986129870506 - interim result at sequence step  50
...
3.1426017350685425 - interim result at sequence step  990
3.140584589329763 - interim result at sequence step  991
3.1425997026798886 - interim result at sequence step  992
3.140586617627045 - interim result at sequence step  993
3.142597678461635 - interim result at sequence step  994
3.1405886377785612 - interim result at sequence step  995
3.1425956623646125 - interim result at sequence step  996
3.140590649833284 - interim result at sequence step  997
3.142593654340044 - interim result at sequence step  998
3.140592653839794 - interim result at sequence step  999
3.140592653839794

real	0m0.053s
user	0m0.032s
sys	0m0.008s
```
and switching back to million step sequence, this looks about right
```
[~/projects/classic-problems-python/chap1-small-problems/pi] # cat calculate_pi_orig.py 
def calculate_pi(n_terms: int) -> float:
    numerator: float = 4.0
    denominator: float = 1.0
    operation: float = 1.0
    pi: float = 0.0
    for _ in range(n_terms):
        pi += operation * (numerator / denominator)
        denominator += 2.0
        operation *= -1.0
    return pi

if __name__ == "__main__":
    print(calculate_pi(1000000))

[~/projects/classic-problems-python/chap1-small-problems/pi] # time python3.9 calculate_pi_orig.py 
3.1415916535897743

real	0m0.162s
user	0m0.160s
sys	0m0.004s
```
although tracking the interim results, even after a million steps this is only accurate to about 7 SF (Signficant Figures)

```
[~/projects/classic-problems-python/chap1-small-problems/pi] # cat calculate_pi.py 
def calculate_pi(n_terms: int) -> float:
    numerator: float = 4.0
    denominator: float = 1.0
    operation: float = 1.0
    pi: float = 0.0
    for step in range(n_terms):
        pi += operation * (numerator / denominator)
        denominator += 2.0
        operation *= -1.0
        print( str(pi) + " - interim result at sequence step  "  +str(step)  )
    return pi

if __name__ == "__main__":  
    print(calculate_pi(1000000))

[~/projects/classic-problems-python/chap1-small-problems/pi] # time python3.9 calculate_pi.py  | tail
3.141591653581774 - interim result at sequence step  999991
3.1415936535967743 - interim result at sequence step  999992
3.1415916535837742 - interim result at sequence step  999993
3.141593653594774 - interim result at sequence step  999994
3.141591653585774 - interim result at sequence step  999995
3.141593653592774 - interim result at sequence step  999996
3.141591653587774 - interim result at sequence step  999997
3.1415936535907742 - interim result at sequence step  999998
3.1415916535897743 - interim result at sequence step  999999
3.1415916535897743

real	0m1.804s
user	0m1.812s
sys	0m0.068s
```