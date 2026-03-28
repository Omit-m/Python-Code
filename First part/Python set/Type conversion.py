data = [1, 2, 2, 3]

a = tuple(data)   # list → tuple
b = set(data)     # list → set
c = list(b)       # set → list

print(a)   # (1, 2, 2, 3)
print(b)   # {1, 2, 3}
print(c)   # [1, 2, 3]