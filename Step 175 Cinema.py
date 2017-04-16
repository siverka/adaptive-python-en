n, m = map(int, input().split())
seats = [[int(x) for x in input().split()] for _ in range(n)]
k = int(input())


def have_seats(seats):
    for i in range(n):
        for j in range(m-k+1):
            if all(map(lambda x: x == 0, seats[i][j:j+k])):
                return i + 1
    return 0

print(have_seats(seats))

