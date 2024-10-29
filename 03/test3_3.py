lst = [1, 2, 3, 4, 5, 6]
if len(lst) == 0:
# якщо список порожній
    result = [[],[]]
elif len(lst) % 2 == 0:
    # якщо список має парну кількість елементів
    mid = len(lst) // 2
    result = [lst[:mid], lst[mid:]]
else:
    # якщо список має непарну кількість елементів
    mid = len(lst) // 2 + 1
    result = [lst[:mid], lst[mid:]]
print(result)

lst1 = [1, 2, 3]
if len(lst1) == 0:
# якщо список порожній
    result = [[],[]]
elif len(lst1) % 2 == 0:
    # якщо список має парну кількість елементів
    mid = len(lst1) // 2
    result = [lst1[:mid], lst1[mid:]]
else:
    # якщо список має непарну кількість елементів
    mid = len(lst1) // 2 + 1
    result = [lst1[:mid], lst1[mid:]]
print(result)

lst2 = [1, 2, 3, 4, 5]
if len(lst2) == 0:
# якщо список порожній
    result = [[],[]]
elif len(lst2) % 2 == 0:
    # якщо список має парну кількість елементів
    mid = len(lst2) // 2
    result = [lst2[:mid], lst2[mid:]]
else:
    # якщо список має непарну кількість елементів
    mid = len(lst2) // 2 + 1
    result = [lst2[:mid], lst2[mid:]]
print(result)

lst3 = [1]
if len(lst3) == 0:
# якщо список порожній
    result = [[],[]]
elif len(lst3) % 2 == 0:
    # якщо список має парну кількість елементів
    mid = len(lst3) // 2
    result = [lst3[:mid], lst3[mid:]]
else:
    # якщо список має непарну кількість елементів
    mid = len(lst3) // 2 + 1
    result = [lst3[:mid], lst3[mid:]]
print(result)

lst4 = []
if len(lst4) == 0:
# якщо список порожній
    result = [[],[]]
elif len(lst4) % 2 == 0:
    # якщо список має парну кількість елементів
    mid = len(lst4) // 2
    result = [lst4[:mid], lst4[mid:]]
else:
    # якщо список має непарну кількість елементів
    mid = len(lst4) // 2 + 1
    result = [lst4[:mid], lst4[mid:]]
print(result)
