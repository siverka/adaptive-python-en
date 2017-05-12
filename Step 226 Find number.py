def digits(n):
    return sum(int(d) for d in str(n))

n = int(input())
m = digits(n)
numbers = [i for i in range(n) if digits(i) == m]
print(len(numbers))
