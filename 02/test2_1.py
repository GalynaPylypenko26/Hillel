# Вводимо 4-х значне число з клавіатури, з урахуванням того, що це число повинно бути цілим
number = int(input("Будь ласка, введить 4-х значне число: "))
# Отримуємо кожну цифру з 4-х значного числа
digit1 = number // 1000
digit2 = (number // 100) % 10
digit3 = (number // 10) % 10
digit4 = number % 10
# Виводимо кожну цифру з 4-х значного числа в стовпчик з нового рядку
print(digit1)
print(digit2)
print(digit3)
print(digit4)
