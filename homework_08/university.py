# Импортируйте класс Student из первого задания
# from student import Student
# Создайте переменную students - список объектов класса Student, с разными именами и средней оценкой.
# Посчитайте суммарную стипендию для всех студентов.
# Посчитайте количество отличников (используйте метод is_excellent).
# * Заверните код для пунктов 4 и 5 к функции calc_sum_scholarship и get_excellent_student_count

from student import Student

students = [
        Student("Max", 5),
        Student("Alex", 6),
        Student("Wadim", 7),
        Student("Andrey", 3),
        Student("Denis", 9)
    ]


def calc_sum_scholarship(students):
    return sum(student.get_scholarship() for student in students)


def get_excellent_student_count(students):
    return sum(student.is_excellent() for student in students)
