def fib1(n):
    if n == 0: return 0
    if n == 1: return 1
    return fib1(n - 1) + fib1(n - 2)


assert fib1(0) == 0
assert fib1(1) == 1
assert fib1(2) == 1
assert fib1(3) == 2
assert fib1(5) == 5
assert fib1(6) == 8
assert fib1(10) == 55
