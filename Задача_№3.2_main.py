class Student:
    def __init__(self, surname, name, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def calc_average(self):
        sumgrades = 0
        amount = 0
        for item in self.grades.items():
            for grades_list in item:
                if isinstance(grades_list, list) and all(isinstance(x, (int, float)) for x in grades_list):
                    sumgrades += sum(grades_list)
                    amount += len(grades_list)
        average_grade = sumgrades / amount if amount else 0
        return average_grade

    def __str__(self):
        average_grade = self.calc_average()
        return (f"Имя: {self.name}\nФамилия: {self.surname}\n"
                f"Средняя оценка за лекции: {average_grade}\n"
                f"Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n"
                f"Завершенные курсы: {", ".join(self.finished_courses)}")

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
                return None
            else:
                lecturer.grades[course] = [grade]
                return None
        else:
            return 'Ошибка'

    def __eq__(self, other) :
        if isinstance(other, Student) :
            return self.calc_average() == other.calc_average()

    def __lt__(self, other) :
        if isinstance(other, Student) :
            return self.calc_average() < other.calc_average()

    def __gt__(self, other) :
        if isinstance(other, Student) :
            return self.calc_average() > other.calc_average()

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self,name,surname):
        super().__init__(name, surname)
        self.grades = {}

    def calc_average(self):
        sumgrades = 0
        amount = 0
        for item in self.grades.items():
            for grades_list in item:
                if isinstance(grades_list, list) and all(isinstance(x, (int, float)) for x in grades_list):
                    sumgrades += sum(grades_list)
                    amount += len(grades_list)
        return sumgrades / amount if amount else 0

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

    def __eq__(self, other) :
        if isinstance(other, Lecturer) :
            return self.calc_average() == other.calc_average()

    def __lt__(self, other) :
        if isinstance(other, Lecturer) :
            return self.calc_average() < other.calc_average()

    def __gt__(self, other) :
        if isinstance(other, Lecturer) :
            return self.calc_average() > other.calc_average()

class Reviewer(Mentor):
    def __init__(self,name,surname):
        super().__init__(name, surname)

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"

    def rate_student(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'



lecturer1 = Lecturer('Иван', 'Иванов')
lecturer2 = Lecturer('Андрей', 'Андреев')
reviewer1 = Reviewer('Пётр', 'Петров')
student1 = Student('Алёхина', 'Ольга', 'Ж')
student2 = Student('Коньков', 'Саня', 'М')

student1.courses_in_progress += ['Python', 'Java']
student2.courses_in_progress += ['Python', 'JavaScript']
lecturer1.courses_attached += ['Python', 'C++','Java', 'JavaScript']
lecturer2.courses_attached += ['JavaScript']
reviewer1.courses_attached += ['Python', 'C++','JavaScript']
reviewer1.rate_student(student1,'Python',8)
reviewer1.rate_student(student1,'Java',3)
reviewer1.rate_student(student2,'Python',7)
reviewer1.rate_student(student2,'JavaScript',1)
student2.rate_lecture(lecturer2,'JavaScript',8)

print(student1.rate_lecture(lecturer1, 'Python', 5))   # None
print(student1.rate_lecture(lecturer1, 'Java', 8))     # Ошибка
print(student1.rate_lecture(lecturer1, 'С++', 8))      # Ошибка
print(student1.rate_lecture(reviewer1, 'Python', 6))   # Ошибка

print(student2.rate_lecture(lecturer1, 'JavaScript', 9))   # None

print(lecturer1.grades)  # {'Python': [7]}
print(f"{student1.surname} {student1.grades}")
print(f"{student2.surname} {student2.grades}")

print(reviewer1)
print(lecturer1)
print(student1)
print(student2)
print(f"равенство студентов: {student1 == student2}")
print(f"у первого студента выше оценка : {student1 > student2}")
print(f"у первого студента ниже оценка : {student1 < student2}")
print(lecturer1.grades)  # {'Python': [7]}
print(lecturer2.grades)
print(f"равенство лекторов: {lecturer1 == lecturer2}")
print(f"у первого лектора выше оценка : {lecturer1 > lecturer2}")
print(f"у первого лектора ниже оценка : {lecturer1 < lecturer2}")
