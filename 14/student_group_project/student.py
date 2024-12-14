from human import Human

class Student(Human):
    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f"{super().__str__()}, {self.record_book}"

    def __eq__(self, other):
        # використала isinstance - вбудовану функцію Python, яка перевіряє, чи є об'єкт other екземпляром класу Student
        if isinstance(other, Student):
            return str(self) == str(other)
        return False

    def __hash__(self):
        return hash(str(self))
