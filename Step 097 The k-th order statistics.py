def partition(list, k, n):
    reference = list[-1]
    i, j = 0, 0
    print('k', k, 'list: ', list)
    while j < n - 1:
        if list[j] < reference:
            a = list[i]
            list[i] = list[j]
            list[j] = a
            i += 1
            j += 1
        else:
            j += 1
    a = list[i]
    list[i] = list[j]
    list[j] = a

    print('k:', k, 'list:', list)
    print('reference:', reference, 'list:', list[:i], k)
    print('reference:', reference, 'list:', list[i:], k - i)
    print('i:', i, ',j:', j, ',k:', k)
    print('------------')
    if i == k:
        return list[i]
    if i == 0:
        return partition(list[1:], k - 1, n - 1)
    if i == len(list) - 1:
        return partition(list[:-1], k, n - 1)
    if k < i:
        return partition(list[:i], k, i)
    else:
        return partition(list[i:], k - i, n - i)


# array = [3, 6, 5, 7, 2, 9, 8, 10, 4, 1]
# print(partition(array, 9, 10))

n, k = (int(i) for i in input().split())
list = [int(i) for i in input().split()]
print(partition(list, k, n))

