lst = [12, 3, 4, 10]
if len(lst) > 1:
    lst = [lst[-1]] + lst[:-1]
print(lst)
lst1 = [1]
if len(lst1) > 1:
    lst1 = [lst1[-1]] + lst1[:-1]
print(lst1)
lst2 = []
if len(lst2) > 1:
    lst2 = [lst2[-1]] + lst2[:-1]
print(lst2)
lst3 = [12, 3, 4, 10, 8]
if len(lst3) > 1:
    lst3 = [lst3[-1]] + lst3[:-1]
print(lst3)