def is_even(number):

    # Перетворюємо число на рядок і перевіряємо останню цифру
    last_digit = str(number)[-1]
    # Перевіряємо,чи є остання цифра однією з парних цифр: '0', '2', '4', '6', '8'. Якщо так, то функція повертає True (число парне). Інакше - False.
    return last_digit in '02468'

# Перевірка
assert is_even(2494563894038**2) == True, 'Test1'
assert is_even(1056897**2) == False, 'Test2'
assert is_even(24945638940387**3) == False, 'Test3'
print('OK')




