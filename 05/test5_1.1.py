import string
import keyword
input_string = input("Будь ласка, введіть рядок: ")
# Перевіряємо, чи рядок є зарезервованим словом
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
            # Перевірка, чи рядок складається лише з підкреслень "_"
            if input_string.replace("_", "") == "" and len(input_string) > 1:
                print(False)
            else:
                print(True)
