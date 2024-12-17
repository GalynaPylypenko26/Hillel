from person import Person


class Database:
    def __init__(self):
        self.people = []

    def add_person(self, person):
        """Додає людину до бази даних."""
        self.people.append(person)

    def search(self, query):
        """Шукає записи в базі, що відповідають пошуковому запиту."""
        return [person for person in self.people if person.matches(query)]

    def save_to_file(self, filename):
        """Зберігає всі записи в текстовий файл."""
        with open(filename, "w", encoding="utf-8") as f:
            for person in self.people:
                f.write(person.serialize() + "\n")

    def load_from_file(self, filename):
        """Завантажує записи з текстового файлу."""
        self.people = []
        try:
            with open(filename, "r", encoding="utf-8") as f:
                for line in f:
                    self.people.append(Person.deserialize(line))
        except FileNotFoundError:
            print(f"Файл {filename} не знайдено.")
        except ValueError as e:
            print(f"Помилка у форматі даних: {e}")
