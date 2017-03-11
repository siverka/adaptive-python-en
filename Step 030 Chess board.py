def chess(x1, y1, x2, y2):
    if x1 == x2 or y1 == y2 or abs(x1 - x2) == abs(y1 - y2):
        return "YES"
    else:
        return 'NO'

x1, y1, x2, y2 = [int(i) for i in input().split()]
print(chess(x1, y1, x2, y2))

# print(chess(1, 1, 3, 3))  # Yes
# print(chess(1, 1, 4, 3))  # No
# print(chess(2, 2, 5, 2))  # Yes

