def gcd(a, b):
    for i in range(max(a, b), a * b + 1):
        if i % a == 0 and i % b == 0:
            return i

print(gcd(int(input()), int(input())))
# print(gcd(7, 5))
# print(gcd(15, 15))
# print(gcd(12, 16))
