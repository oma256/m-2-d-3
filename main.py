"""
Задача 1: Класс Книга
Создайте класс Book с атрибутами (свойства) title (название), 
author (автор), и pages (количество страниц). Добавьте метод info, 
который возвращает информацию о книге в виде строки.
"""

# class Book:
#     def __init__(self, title, author, pages):
#         self.title = title
#         self.author = author
#         self.pages = pages

#     def info(self):
#         print(f'Название: {self.title}\n'
#               f'Автор: {self.author}\n'
#               f'Кол-во страниц: {self.pages}')

#     def size(self):
#         if self.pages > 300:
#             print('Книга большая')
#         else:
#             print('Книга маленькая')


# book1 = Book('Гракаем алгоритмы', 'Адитья Бхаргава', 350)
# book1.info()
# book1.size()


"""
Задача 2: Класс Студент
Создайте класс Student с атрибутами name (имя) и grade (оценка). 
Добавьте методы для установки и получения оценки студента.
"""

# class Student:

#     def __init__(self, name) -> None:
#         self.name = name
#         self.grade = None
    
#     def set_grade(self, grade):
#         self.grade = grade
    
#     def get_grade(self):
#         if self.grade is None:
#             print('У студента не проставлена оценка!')
#         else:
#             print(f'Оценка студента: {self.grade}')


# studet1 = Student('Omurbek')
# studet1.get_grade()
# studet1.set_grade(83)
# studet1.get_grade()


"""
Задача 3: Наследование - Класс Преподаватель
Создайте класс TeacherMath, TeacherLang наследуемый от Teacher, 
с дополнительным атрибутом subject (предмет преподавания). 
Переопределите метод info.
"""

# class Teacher:
    
#     def __init__(self, name, subject):
#         self.name = name
#         self.subject = subject
    
#     def info(self):
#         print(f'{self.name} предмет преподавания {self.subject}')


# class TeacherMath(Teacher):
#     pass


# class TeacherLang(Teacher):

#     def info(self):
#         print('Я сперва унаследовал!!!')
#         print(f'{self.name} предмет преподавания {self.subject}')


# teacher_math = TeacherMath(name='Фибоначи', subject='Математика')
# teacher_lang = TeacherLang(name='Гвидо Ван Рассум', subject='Python')

# teacher_math.info()
# teacher_lang.info()
