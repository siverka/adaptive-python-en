with open('input_step_339_dataset_30635_1.txt', 'r') as file:
    numbers = [int(n) ** 2 for n in file.readline().strip().split()]
    print(sum(numbers))
