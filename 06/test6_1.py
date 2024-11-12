import string
letters = tuple(string.ascii_letters)
begin, end = input("Будь ласка, введіть через дефіс дві літери: ").split('-')
begin_ind = letters.index(begin)
end_ind = letters.index(end)
result = letters[begin_ind:end_ind + 1]
print("Результат обробки:", ''.join(result))
