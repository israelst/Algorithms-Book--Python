def fib2(n):
    if n == 0: return 0
    f = [0] * (n + 1)
    f[0] = 0
    f[1] = 1
    for i in range(2, n + 1):
        f[i] = f[i - 1] + f[i - 2]
    return f[n]

# Create this list is useless since we just need the last calculated value
def fib2_without_list(n):
    if n == 0: return 0
    f0, f1 = 0, 1
    for i in range(2, n + 1):
        f1, f0 = f0 + f1, f1
    return f1

assert fib2(0) == 0
assert fib2(1) == 1
assert fib2(2) == 1
assert fib2(3) == 2
assert fib2(5) == 5
assert fib2(6) == 8
assert fib2(10) == 55

assert fib2_without_list(0) == 0
assert fib2_without_list(1) == 1
assert fib2_without_list(2) == 1
assert fib2_without_list(3) == 2
assert fib2_without_list(5) == 5
assert fib2_without_list(6) == 8
assert fib2_without_list(10) == 55
