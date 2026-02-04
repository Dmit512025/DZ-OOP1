class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __str__(self):
        sumgrades = 0
        amount = 0
        for item in self.grades.items():
            for grades_list in item:
                if isinstance(grades_list, list) and all(isinstance(x, (int, float)) for x in grades_list):
                    sumgrades += sum(grades_list)
                    amount += len(grades_list)
        average_grade = sumgrades / amount if amount else 0
        return (f"Имя: {self.name}\nФамилия: {self.surname}\n"
                f"Средняя оценка за лекции: {average_grade}\n"
                f"Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n"
                f"Завершенные курсы: {", ".join(self.finished_courses)}")

    def rate_lecture(self, lecturer1, course, grade):
        if isinstance(lecturer1, Lecturer) and course in lecturer1.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer1.grades[course] += [grade]
                return None
            else:
                lecturer1.grades[course] = [grade]
                return None
        else:
            return 'Ошибка'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self,name,surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        sumgrades = 0
        amount = 0
        for item in self.grades.items():
            for grades_list in item:
                if isinstance(grades_list, list) and all(isinstance(x, (int, float)) for x in grades_list):
                    sumgrades += sum(grades_list)
                    amount += len(grades_list)
        average_grade = sumgrades / amount if amount else 0
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {average_grade}"

class Reviewer(Mentor):
    def __init__(self,name,surname):
        super().__init__(name, surname)

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"

    def rate_student(self, student1, course, grade):
        if isinstance(student1, Student) and course in self.courses_attached and course in student1.courses_in_progress:
            if course in student1.grades:
                student1.grades[course] += [grade]
            else:
                student1.grades[course] = [grade]
        else:
            return 'Ошибка'


lecturer = Lecturer('Иван', 'Иванов')
reviewer = Reviewer('Пётр', 'Петров')
student = Student('Алёхина', 'Ольга', 'Ж')

student.courses_in_progress += ['Python', 'Java']
lecturer.courses_attached += ['Python', 'C++','Java']
reviewer.courses_attached += ['Python', 'C++']

print(student.rate_lecture(lecturer, 'Python', 5))   # None
print(student.rate_lecture(lecturer, 'Java', 8))     # Ошибка
print(student.rate_lecture(lecturer, 'С++', 8))      # Ошибка
print(student.rate_lecture(reviewer, 'Python', 6))   # Ошибка

print(lecturer.grades)  # {'Python': [7]}

print(reviewer)
print(lecturer)
print(student)
