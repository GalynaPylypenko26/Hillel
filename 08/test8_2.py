def is_palindrome(text):
    # Залишаємо рядок тільки з букв в нижньому регістрі та цифр, без пробілів та знаків пунктуації
    clean_text = ''.join(char.lower() for char in text if char.isalnum())
    # Перевіряємо чи збігається рядок з оберненим
    return clean_text == clean_text[::-1]

# Перевірка
assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
print("ОК")
