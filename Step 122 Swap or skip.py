numbers = [int(x) for x in input().split() if int(x) != -1]
count = 0
for i in range(len(numbers)-1):
    if numbers[i] > numbers[i + 1]:
        count += 1
        numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]

print(count)
