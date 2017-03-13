info = input().split()
string = '{name}, You will be 100 years old in {year} year.'
print(string.format(name=info[0], year=100 - int(info[1]) + 2016))
