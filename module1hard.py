# Базовые структуры данных
# Задание "Средний балл":
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students_list = list(students)  # список студентов
students_list.sort()  # сортируем по возрастанию
list_ = 0  # для поиска оценок студентов по порядку
jurnal = {'Имя': 0}  # создали журнал с оценками
for name in students_list:  # цикл по именам
    student_grades = grades[list_]  # получим оценки студента
    student_grade_mid = sum(student_grades) / len(student_grades)  # среднее значение
    jurnal.update({name: student_grade_mid})  # добавим студента с оценкой в журнал
    list_ += 1  # к следующему студенту
jurnal.pop('Имя')  # убрать первую строку журнала, она не нужна
print(jurnal)  # вывод журнала со средними оценками