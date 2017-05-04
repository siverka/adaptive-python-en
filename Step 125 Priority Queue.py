numbers = []

n = int(input())
for _ in range(n):
    line = input().split()
    if line[0] == 'Insert':
        numbers.append(int(line[1]))
    else:
        max_value = max(numbers)
        print(max_value)
        numbers.remove(max_value)
