def binary_search(array, x):
    left = 0
    right = len(array)
    while right > left + 1:
        median = (right + left) // 2
        if x < array[median]:
            right = median
        else:
            left = median
        # print(left, right)

    if array[left] == x:
        return left + 1
    else:
        return -1


n, *array_a = map(int, input().split())
k, *array_b = map(int, input().split())
# n, k = 5, 5
# array_a = [1, 5, 8, 12, 13]
# array_b = [8, 1, 23, 1, 11]
answer = [binary_search(array_a, b) for b in array_b]
print(*answer)
