def correct_sentence(text):
    text = text[0].upper() + text[1:]
    if not text.endswith('.'):
        text += '.'
    return text
# Перевірка
Test1 = correct_sentence("greetings, friends")
print(Test1)
Test2 = correct_sentence("hello")
print(Test2)
Test3 = correct_sentence("Greetings. Friends")
print(Test3)
Test4 = correct_sentence("Greetings, friends.")
print(Test4)
Test5 = correct_sentence("greetings, friends.")
print(Test5)
