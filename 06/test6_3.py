number = int(input("Будь ласка, введіть ціле число: "))
while number > 9:
    result = 1
    for digit in str(number):
        digit_value = int(digit)
        result = result * digit_value
    number = result
print("Результат обробки:", number)
