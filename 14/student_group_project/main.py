from student import Student
from group import Group
from exceptions import MaxStudentsError

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
