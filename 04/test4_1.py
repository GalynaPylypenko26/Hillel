lst1 = [0, 1, 0, 12, 3]
lst2 = [0]
lst3 = [1, 0, 13, 0, 0, 0, 5]
lst4 = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]

lst1 = [x for x in lst1 if x != 0] + [0] * lst1.count(0)
lst2 = [x for x in lst2 if x != 0] + [0] * lst2.count(0)
lst3 = [x for x in lst3 if x != 0] + [0] * lst3.count(0)
lst4 = [x for x in lst4 if x != 0] + [0] * lst4.count(0)
print(lst1)
print(lst2)
print(lst3)
print(lst4)