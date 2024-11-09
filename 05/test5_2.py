continue_calculating = 'y'
while continue_calculating == 'y' or continue_calculating == 'yes':
    num1 = float(input("Будь ласка,введіть 1-е число: "))
    operator = input("Будь ласка, введить потрібну дію (+, -, *, /): ")
    num2 = float(input("Будь ласка,введіть 2-е число: "))
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            print("Ділити на 0 не можна!")
            continue
    else:
        print("Некоректна дія!")
        continue
    print("Результат:", result)

    continue_calculating = input("Якщо хочете продовжити, будь ласка, введіть y/yes: ").strip().lower()
print("Роботу калькулятора завершено!")
