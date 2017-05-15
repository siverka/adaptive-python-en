roman = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
arabic = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

n = int(input())
res = ''

for i in range(len(roman)):
    while n >= arabic[i]:
        n -= arabic[i]
        res += roman[i]

print(res)
