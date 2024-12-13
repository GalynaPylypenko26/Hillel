class MaxStudentsError(Exception):
    def __init__(self, message="У групі не може бути більше 10 студентів."):
        super().__init__(message)

class Human:
    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Student(Human):
    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f"{super().__str__()}, {self.record_book}"

class Group:
    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        if len(self.group) >= 10:
            raise MaxStudentsError()
        self.group.add(student)

    def delete_student(self, last_name):
        student = self.find_student(last_name)
        if student:
            self.group.remove(student)

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def __str__(self):
        all_students = "\n".join(str(student) for student in self.group)
        return f"Number: {self.number}\n{all_students}"

# Перевірки
try:
    st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
    st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
    st3 = Student('Male', 22, 'John', 'Doe', 'AN146')
    st4 = Student('Female', 23, 'Mary', 'Smith', 'AN147')
    st5 = Student('Male', 21, 'Alex', 'Johnson', 'AN148')
    st6 = Student('Female', 24, 'Emily', 'Davis', 'AN149')
    st7 = Student('Male', 26, 'Michael', 'Brown', 'AN150')
    st8 = Student('Female', 22, 'Linda', 'Wilson', 'AN151')
    st9 = Student('Male', 29, 'Chris', 'Martinez', 'AN152')
    st10 = Student('Female', 27, 'Patricia', 'Anderson', 'AN153')
    st11 = Student('Male', 28, 'Paul', 'Taylor', 'AN154')

    gr = Group('PD1')

    students = [st1, st2, st3, st4, st5, st6, st7, st8, st9, st10, st11]

    for student in students:
        gr.add_student(student)
        print(f"Додано студента: {student}")

except MaxStudentsError as e:
    print(f"Помилка: {e}")

print(gr)
