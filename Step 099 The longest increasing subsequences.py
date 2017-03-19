def lis(array):
    n = len(array)
    length = [1 for _ in range(n)]
    previous = [0 for _ in range(n)]

    for i in range(1, n):
        js = [j for j in range(i) if array[j] < array[i]]
        sublength = [length[j] for j in js]
        if sublength:
            max_length = max(sublength)
            length[i] += max_length
            indexes = [k for k in js if sublength[js.index(k)] == max_length]
            values = [array[k] for k in indexes]
            previous[i] = indexes[values.index(min(values))]

    index = length.index(max(length))
    subseq = [array[index]]
    l = max(length) - 1
    while l > 0:
        subseq.append(array[previous[index]])
        index = previous[index]
        l -= 1

    return subseq[::-1]

array = [1, 2, 3, 4, 5]  # [1, 2, 3, 4, 5]
# array = [1, 4, 4, 3, 5, 2, 8]  # [1, 4, 5, 8]
# array = [1, 3, 5, 2, 4]  # [1, 3, 5]
# array = [10, 22, 9, 33, 21, 50, 41, 60, 80]  # [10, 22, 33, 41, 60, 80]
# array = [int(i) for i in input().split()]
print(*lis(array))
