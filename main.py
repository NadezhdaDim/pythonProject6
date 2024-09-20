import random

# список учеников
students = ['Аполлон', 'Ярослав', 'Александра', 'Дарья', 'Ангелина']
# отсортируем список учеников
students.sort()
# список предметов
classes = ['Математика', 'Русский язык', 'Информатика']
# пустой словарь с оценками по каждому ученику и предмету
students_marks = {}
# сгенерируем данные по оценкам:
# цикл по ученикам
for student in students:  # 1 итерация: student = 'Александра'
    students_marks[student] = {}  # 1 итерация: students_marks['Александра'] = {}
    # цикл по предметам
    for class_ in classes:  # 1 итерация: class_ = 'Математика'
        marks = [random.randint(1, 5) for i in range(3)]  # генерируем список из 3х случайных оценок
        students_marks[student][class_] = marks  # students_marks['Александра']['Математика'] = [5, 5, 5]
# выводим получившийся словарь с оценками:
for student in students:
    print(f'''{student}
            {students_marks[student]}''')

print('''
        Список команд:
        1. Добавить оценки ученика по предмету
        2. Вывести средний балл по всем предметам по каждому ученику
        3. Вывести все оценки по всем ученикам
        4. Выход из программы
        5. Вывести все оценки для определенного ученика
        6. Редактирование данных по предметам
        7. Удаление ученика из списка
        8. Удаление и редактирование данных по оценкам
        9. Вывести средний балл по каждому предмету для определенного ученика
        ''')

while True:
    command = int(input('Введите команду: '))
    if command == 1:
        print('1. Добавить оценку ученика по предмету')
        # считываем имя ученика
        student = input('Введите имя ученика: ')
        # считываем название предмета
        class_ = input('Введите предмет: ')
        # считываем оценку
        mark = int(input('Введите оценку: '))
        # если данные введены верно
        if student in students_marks.keys() and class_ in students_marks[student].keys():
            # добавляем новую оценку для ученика по предмету
            students_marks[student][class_].append(mark)
            print(f'Для {student} по предмету {class_} добавлена оценка {mark}')
        # неверно введены название предмета или имя ученика
        else:
            print('ОШИБКА: неверное имя ученика или название предмета')
    elif command == 2:
        print('2. Вывести средний балл по всем предметам по каждому ученику')
        # цикл по ученикам
        for student in students:
            print(student)
            # цикл по предметам
            for class_ in classes:
                # находим сумму оценок по предмету
                marks_sum = sum(students_marks[student][class_])
                # находим количество оценок по предмету
                marks_count = len(students_marks[student][class_])
                # выводим средний балл по предмету
                print(f'{class_} - {marks_sum // marks_count}')
            print()
    elif command == 3:
        print('3. Вывести все оценки по всем ученикам')
        # выводим словарь с оценками:
        # цикл по ученикам
        for student in students:
            print(student)
            # цикл по предметам
            for class_ in classes:
                print(f'\t{class_} - {students_marks[student][class_]}')
            print()
    elif command == 4:
        print('4. Добавить нового ученика')
        student = input('Введите имя ученика: ')
        students_marks[student]={
            'Математика': [],
            'Русский язык': [],
            'Информатика':[],
        }
        print(f'Ученик {student} добавлен в список учеников')
    elif command == 5:
        print('5. Вывести все оценки для определенного ученика')
        student = input('Введите имя ученика: ')
        if student in students_marks.keys():
            print(f'Для {student} выведены оценки')
            for subj, marks in students_marks[student].items():
                print(subj + ",", marks)
        else:
            print(f'Данного ученика нет в списке класса')
    elif command == 6:
        print('6. Редактирование данных по предметам')
        student = input('Введите имя ученика: ')
        class_ = input('Введите предмет: ')
        if student in students_marks.keys() and class_ in students_marks[student].keys():
            redack_student = input('Введите новое наименование предмета: ')
            students_marks[student][class_] = redack_student
        print(f'Изменено имя предмета, новое наименование: {redack_student}')
    elif command == 7:
        print('7. Удаление ученика из списка')
        end_student = input('Введите имя ученика, которого хотите удалить: ')
        if end_student in students_marks:
            del students_marks[end_student]
            print(students_marks)
        else:
            print(f'Данного ученика нет в списке класса')
    elif command == 8:
        print('8. Удаление и редактирование данных по оценкам')
        student = input('Введите имя ученика: ')
        if student in students:
            class_ = input('Введите наименование предмета: ')
            if class_ in classes:
                end_mark = int(input('Введите оценку, которую хотите удалить: '))
                if end_mark in (students_marks[student][class_]):
                    (students_marks[student][class_]).remove(end_mark)
                    print(students_marks[student])
                else:
                    print(f'Данной оценки нет у ученика')
        else:
            print(f'Данного ученика нет в списке')
    elif command == 9:
        print('9. Вывести средний балл по каждому предмету для определенного ученика')
        student = input('Введите имя ученика: ')
        if student in students_marks.keys() and class_ in students_marks[student].keys():
            marks_sum = sum(students_marks[student][class_])
            marks_count = len(students_marks[student][class_])
            print(f'{student} - {marks_sum // marks_count}')
            print()
    elif command == 10:
        print('10. Выход из программы')
        break
