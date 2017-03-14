# n = int(input())
# intervals = [[int(i) for i in input().split()] for _ in range(n)]


def end_point(interval):
    return interval[1]


def is_intersects(interval1, interval2):
    return max(interval1[0], interval2[0]) <= min(interval1[1], interval2[1])


n = 4
intervals = [[4, 7], [1, 3], [2, 5], [5, 6]]

intervals = sorted(intervals, key=end_point)
print(intervals)

result_set = []
# http://cs.stackexchange.com/questions/43197/relation-between-the-point-cover-interval-problem-and-the-interval-scheduling
