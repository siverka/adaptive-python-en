numbers = [int(x) for x in input().split()]
even_numbers = [numbers[i] for i in range(len(numbers)) if i % 2 == 1]
for n in even_numbers:
    print(n, end='\n')
print(sum(x for x in numbers if x % 2 == 0))
