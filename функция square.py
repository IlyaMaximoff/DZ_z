def square(a):
    p = a * 4
    s = a * a
    d = a * (2**0.5)
    return p,s,d
squares = square(2)
print(squares)