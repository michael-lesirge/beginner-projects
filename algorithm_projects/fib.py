from functools import lru_cache

@lru_cache(2)
def fib1(n):
    if n < 2:
        return n
    return fib1(n-1) + fib1(n-2)


# no imports
def fib2(n, memo={0: 0, 1: 1}):
    if n not in memo:
        memo[n] = fib2(n-1) + fib2(n-2)
    return memo[n]
