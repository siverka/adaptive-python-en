def is_intersected(interval1, interval2):
    return max(interval1[0], interval2[0]) <= min(interval1[1], interval2[1])


def points(intervals):
    intervals = sorted(intervals, key=lambda interval: interval[1])
    result_set = []

    while intervals:
        interval = intervals.pop(0)
        result_set.append(interval)
        intervals = [x for x in intervals if not is_intersected(x, interval)]

    print(len(result_set))
    for interval in result_set:
        print(interval[1], end=" ")


n = int(input())
intervals = [[int(i) for i in input().split()] for _ in range(n)]
points(intervals)
# points([[4, 7], [1, 3], [2, 5], [5, 6], [2, 5], [4, 7]])  # 2, 3 6
# points([[1, 3], [2, 5], [3, 6]])  # 1, 3
