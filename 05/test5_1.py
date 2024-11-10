import string
import keyword
input_string = input("Будь ласка, введіть рядок: ")
# Перевіряємо, чи рядок є зареєстрованим словом
if input_string in keyword.kwlist:
    print(False)
else:
    # Перевіряємо, чи рядок починається з цифри
    if input_string[0].isdigit():
        print(False)
    else:
        # Перевіряємо на наявність великих літер, пробілів, знаків пунктуації (окрім "_")
        invalid_chars = string.punctuation.replace("_", "") + string.whitespace + string.ascii_uppercase
        if any(char in invalid_chars for char in input_string):
            print(False)
        else:
            # Перевіряємо, чи повне ім'я змінної містить не більше одного нижнього підкреслення
            if input_string.count("_") > 1:
                print(False)
            else:
                print(True)