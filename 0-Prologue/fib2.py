def fib2(n):
    if n == 0: return 0
    f = [0] * (n + 1)
    f[0] = 0
    f[1] = 1
    for i in range(2, n + 1):
        f[i] = f[i - 1] + f[i - 2]
    return f[n]

assert fib2(0) == 0
assert fib2(1) == 1
assert fib2(2) == 1
assert fib2(3) == 2
assert fib2(5) == 5
assert fib2(6) == 8
assert fib2(10) == 55
