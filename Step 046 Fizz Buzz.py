a, b = (int(i) for i in input().split())

for i in range(a, b + 1):
    print('Fizz' * (i % 3 == 0) + 'Buzz' * (i % 5 == 0) or i)
