number1 = float(input("Будь ласка,введіть 1-е число: "))
operation = (input("Будь ласка, введить потрібну дію (+, -, *, /): "))
number2 = float(input("Будь ласка,введіть 2-е число: "))
if operation == '+':
    result = number1 + number2
    print ("Результат дії:", result)
elif operation == '-':
    result = number1 - number2
    print ("Результат дії:", result)
elif operation == '*':
    result = number1 * number2
    print ("Результат дії:", result)
elif operation == '/':
    if number2 != 0:
        result = number1 / number2
        print ("Результат дії:", result)
    else:
        print ("Ділити на 0 не можна!")
else:
    print ("Некоректна дія!")


