seconds = int(input())
units = [3600, 60, 1]
times = [24, 60, 60]
watches = [seconds // units[i] % times[i] for i in range(3)]
print('%d:%02d:%02d' % tuple(watches))
