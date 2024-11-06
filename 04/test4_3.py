import random
# список випадкових чисел з кількістю елементів від 3 до 10
random_list = [random.randint(1, 10) for _ in range(random.randint(3, 10))]
print("Початковий список випадкових чисел:", random_list)
# новий список з 3 елементів: 1-й, 3-й, 2-й з кінця
new_list = [random_list[0], random_list[2], random_list[-2]]
print("Новий список з 3-х елементів:", new_list)