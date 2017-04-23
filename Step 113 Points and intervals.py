n, m = map(int, input().split())
intervals = [[int(x) for x in input().split()]for _ in range(n)]
points = [int(x) for x in input().split()]
counts = [0 for _ in range(m)]


# def qsort_interval(list):
#     if list:
#         return qsort([x for x in list if x[0] < list[0][0]]) + \
#                [x for x in list if x[0] == list[0][0]] + \
#                qsort([x for x in list if x[0] > list[0][0]])
#     return []
# intervals = qsort_interval(intervals)

intervals.sort(key=lambda interval: interval[0])

for i in range(m):
    j = 0
    while j < n and intervals[j][0] <= points[i]:
        if points[i] <= intervals[j][1]:
            counts[i] += 1
        j += 1

print(*counts)
