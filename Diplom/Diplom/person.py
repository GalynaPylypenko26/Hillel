from datetime import datetime


class Person:
    def __init__(self, first_name, last_name="", patronymic="", birth_date="", death_date=None, gender=""):
        self.first_name = first_name.capitalize()
        self.last_name = last_name.capitalize() if last_name else ""
        self.patronymic = patronymic.capitalize() if patronymic else ""
        self.birth_date = self.validate_date(birth_date)
        self.death_date = self.validate_date(death_date) if death_date else None
        self.gender = gender.lower()

    def validate_date(self, date_str):
        """Перевіряє та перетворює дату з різних форматів у формат datetime."""
        for fmt in ("%d.%m.%Y", "%d %m %Y", "%d/%m/%Y", "%d-%m-%Y"):
            try:
                return datetime.strptime(date_str, fmt)
            except ValueError:
                continue
        raise ValueError(f"Некоректний формат дати: {date_str}")

    def calculate_age(self, reference_date=None):
        """Обчислює вік на основі дати народження та смерті або поточної дати."""
        reference_date = reference_date or datetime.now()
        end_date = self.death_date or reference_date
        age = end_date.year - self.birth_date.year - (
                (end_date.month, end_date.day) < (self.birth_date.month, self.birth_date.day)
        )
        return age

    def get_age_suffix(self, age):
        """Повертає правильне закінчення для слова 'рік'."""
        if 11 <= age % 100 <= 14:
            return "років"
        elif age % 10 == 1:
            return "рік"
        elif 2 <= age % 10 <= 4:
            return "роки"
        else:
            return "років"

    def matches(self, query):
        """Перевіряє, чи відповідає пошуковий запит даним про людину."""
        query = query.lower()
        full_name = f"{self.first_name} {self.last_name} {self.patronymic}".lower()
        return query in full_name

    def __str__(self):
        """Повертає текстове представлення об'єкта Person."""
        # Обчислення віку та правильного закінчення для слова "рік"
        age = self.calculate_age()
        age_suffix = self.get_age_suffix(age)

        # Форматування статі та фраз
        if self.gender == "m":
            gender_str = "чоловік"
            born_str = "Народився"
            died_str = "Помер"
            alive_str = "Живий"
        elif self.gender == "f":
            gender_str = "жінка"
            born_str = "Народилась"
            died_str = "Померла"
            alive_str = "Жива"
        else:
            gender_str = "невідомо"
            born_str = "Народився/лась"
            died_str = "Помер/ла"
            alive_str = "Живий/Жива"

        # Форматування тексту залежно від наявності дати смерті
        if self.death_date:
            death_str = f"{died_str}: {self.death_date.strftime('%d.%m.%Y')}"
        else:
            death_str = alive_str

        # Формування остаточного рядка
        return (f"{self.first_name} {self.last_name} {self.patronymic} {age} {age_suffix}, {gender_str}. "
                f"{born_str} {self.birth_date.strftime('%d.%m.%Y')}. {death_str}.")

    def serialize(self):
        """Серіалізує дані для збереження у текстовому файлі."""
        birth_date = self.birth_date.strftime("%d.%m.%Y")
        death_date = self.death_date.strftime("%d.%m.%Y") if self.death_date else ""
        return f"{self.first_name}|{self.last_name}|{self.patronymic}|{birth_date}|{death_date}|{self.gender}"

    @staticmethod
    def deserialize(line):
        """Створює об'єкт Person із рядка."""
        parts = line.strip().split("|")
        if len(parts) != 6:
            raise ValueError(f"Некоректний запис: {line}")
        return Person(
            first_name=parts[0],
            last_name=parts[1],
            patronymic=parts[2],
            birth_date=parts[3],
            death_date=parts[4] if parts[4] else None,
            gender=parts[5],
        )
