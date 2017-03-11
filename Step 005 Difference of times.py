time1 = [int(input()) for _ in range(3)]
time2 = [int(input()) for _ in range(3)]

units = [3600, 60, 1]
diff = sum(units[i] * (time2[i] - time1[i]) for i in range(3))
print(diff)
