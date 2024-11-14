seconds = int(input("Будь ласка, введіть кількість секунд (0 <= число < 8640000): "))
days, remainder = divmod(seconds, 86400)        # 1 день = 86400 секунд
hours, remainder = divmod(remainder, 3600)      # 1 година = 3600 секунд
minutes, seconds = divmod(remainder, 60)        # 1 хвилина = 60 секунд
# Коректне написання "день" (кількість днів закінчується на 1, але не 11 — "день", кількість днів закінчується на 2,3,4, але не в діапазоні 12–14 — "дні", інше — "днів"
if days % 10 == 1 and days % 100 != 11:
    day_print = "день"
elif 2 <= days % 10 <= 4 and not (12 <= days % 100 <= 14):
    day_print = "дні"
else:
    day_print = "днів"
hours = str(hours).zfill(2)
minutes = str(minutes).zfill(2)
seconds = str(seconds).zfill(2)

# Виведення результату
print(f"{days} {day_print}, {hours}:{minutes}:{seconds}")