def common_elements():
    # Числа кратні 3
    multiples_of_3 = {x for x in range(100) if x % 3 == 0}
    # Числа кратні 5
    multiples_of_5 = {x for x in range(100) if x % 5 == 0}
    intersection = multiples_of_3.intersection(multiples_of_5)
    return intersection
# Перевірка
result = common_elements()
print(result)
