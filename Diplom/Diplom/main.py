from database import Database
from person import Person


def main_menu():
    print("\nМеню:")
    print("1. Додати нову людину")
    print("2. Пошук записів")
    print("3. Зберегти дані у файл")
    print("4. Завантажити дані з файлу")
    print("5. Вийти")


def main():
    db = Database()

    while True:
        main_menu()
        choice = input("Оберіть дію: ")

        if choice == "1":
            try:
                first_name = input("Ім'я: ")
                last_name = input("Прізвище (необов'язково): ")
                patronymic = input("По-батькові (необов'язково): ")
                birth_date = input("Дата народження (формат: 12.10.1980): ")
                death_date = input("Дата смерті (якщо є, формат: 12.10.2000): ")
                death_date = death_date.strip() if death_date.strip() else None
                gender = input("Стать (m/f): ").lower()

                person = Person(first_name, last_name, patronymic, birth_date, death_date, gender)
                db.add_person(person)
                print("Запис додано успішно!")
            except ValueError as e:
                print(f"Помилка: {e}")

        elif choice == "2":
            query = input("Введіть пошуковий запит: ")
            results = db.search(query)
            if results:
                for person in results:
                    print(person)
            else:
                print("Нічого не знайдено.")

        elif choice == "3":
            filename = input("Введіть назву файлу для збереження: ")
            db.save_to_file(filename)
            print("Дані збережено успішно!")

        elif choice == "4":
            filename = input("Введіть назву файлу для завантаження: ")
            try:
                db.load_from_file(filename)
                print("Дані завантажено успішно!")
            except FileNotFoundError:
                print(f"Файл {filename} не знайдено.")
            except ValueError as e:
                print(f"Помилка у форматі даних: {e}")

        elif choice == "5":
            print("До побачення!")
            break

        else:
            print("Невірний вибір. Спробуйте ще раз.")


if __name__ == "__main__":
    main()


