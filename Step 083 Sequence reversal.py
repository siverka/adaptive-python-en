# sequence = [30, 32, 43, 65, -32, 0, 54, 34, -23, 11, 9]
# n = 11
# sequence = [30, 32, 43, 65, -32, 54, 34, -23, 11, 9]
# n = 10
n, *sequence = map(int, input().split())
answer = [sequence[i] + sequence[-1-i] for i in range(n // 2)]
if n % 2 == 1:
    answer.append(sequence[n // 2])
print(*answer)
