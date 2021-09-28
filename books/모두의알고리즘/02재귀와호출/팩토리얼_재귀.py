def fact(n):
    if n <= 2:
        return n
    else:
        return n * fact(n-1)

print(fact(1))
print(fact(5))
print(fact(10))