def second_index(text, some_str):
    first_index = text.find(some_str)
    if first_index == -1:
        return None
    second_index = text.find(some_str, first_index + 1)
    if second_index == -1:
        return None
    return second_index
# Перевірка
Test1 = second_index("sims", "s")
print(Test1)
Test2 = second_index("find the river", "e")
print(Test2)
Test3 = second_index("hi", "h")
print(Test3)
Test4 = second_index("Hello, hello", "lo")
print(Test4)
