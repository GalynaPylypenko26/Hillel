seconds = int(input("Будь ласка, введіть кількість секунд (0 <= число < 8640000): "))
days, remainder = divmod(seconds, 86400)        # 1 день = 86400 секунд
hours, remainder = divmod(remainder, 3600)      # 1 година = 3600 секунд
minutes, seconds = divmod(remainder, 60)        # 1 хвилина = 60 секунд
# Коректне написання "день" (1 день, 2-4 дні, > 4 днів)
if days == 1:
    day_print = "день"
elif 2 <= days <= 4:
    day_print = "дні"
else:
    day_print = "днів"
hours = str(hours).zfill(2)
minutes = str(minutes).zfill(2)
seconds = str(seconds).zfill(2)
print(f"{days} {day_print}, {hours}:{minutes}:{seconds}")
