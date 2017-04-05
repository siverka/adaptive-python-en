numbers = [int(x) for x in input().split()]
min_value, max_value = numbers[0], numbers[0]
for n in numbers:
    if n < min_value:
        min_value = n
    if n > max_value:
        max_value = n
print(max_value, min_value)
