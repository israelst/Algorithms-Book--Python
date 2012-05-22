def divide(x, y):
    if x == 0: return (0, 0)
    q, r = divide(x/2, y)
    q *= 2
    r *= 2
    if x % 2 == 1:
        r += 1
    if r >= y:
        r -= y
        q += 1
    return (q, r)

assert divide(4, 2) == (2, 0)
assert divide(17, 3) == (5, 2)
assert divide(10, 15) == (0, 10)
assert divide(14, 5) == (2, 4)
