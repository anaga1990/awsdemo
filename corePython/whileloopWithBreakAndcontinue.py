a = 1
while a <= 10:
    print("*" * a)
    a = a + 1
    if a == 5:
        break

print("_" * 50)

b = 10
while b >= 0:
    b = b - 1
    if b % 2 == 0:
        continue
    print("*" * b)
