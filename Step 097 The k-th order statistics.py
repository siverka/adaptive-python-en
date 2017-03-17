def partition(list, k, n):
    reference = list[-1]
    i, j = 0, 0
    while j < n - 1:
        if list[j] < reference:
            list[i], list[j] = list[j], list[i]
            i += 1
            j += 1
        else:
            j += 1
    list[i], list[j] = list[j], list[i]

    if i == k:
        return list[i]
    if i == 0:
        return partition(list[1:], k - 1, n - 1)
    if k < i or i == n - 1:
        return partition(list[:i], k, i)
    else:
        return partition(list[i:], k - i, n - i)


n, k = (int(i) for i in input().split())
array = [int(i) for i in input().split()]
print(partition(array, k, n))

# array = [3, 6, 5, 7, 2, 9, 8, 10, 4, 1]
# print(partition(array, 0, 10))  # 1
# print(partition(array, 9, 10))  # 10
# print(partition(array, 4, 10))  # 5

