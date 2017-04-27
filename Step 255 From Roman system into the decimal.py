def roman_to_decimal(n):
    roman = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    arabic = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

    i, res = 0, 0
    while i < len(n):
        if i == len(n) - 1 or roman.index(n[i]) <= roman.index(n[i+1]):
            res += arabic[roman.index(n[i])]
            i += 1
        else:
            res += arabic[roman.index(n[i:i+2])]
            i += 2

    return res

print(roman_to_decimal(input()))
