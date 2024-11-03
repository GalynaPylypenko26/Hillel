lst1 = [0, 1, 7, 2, 4, 8]
lst2 = [1, 3, 5]
lst3 = [6]
lst4 = []

result1 = sum(lst1[i] for i in range(0, len(lst1), 2)) * lst1[-1] if lst1 else 0
result2 = sum(lst2[i] for i in range(0, len(lst2), 2)) * lst2[-1] if lst2 else 0
result3 = sum(lst3[i] for i in range(0, len(lst3), 2)) * lst3[-1] if lst3 else 0
result4 = sum(lst4[i] for i in range(0, len(lst4), 2)) * lst4[-1] if lst4 else 0

print(result1)
print(result2)
print(result3)
print(result4)