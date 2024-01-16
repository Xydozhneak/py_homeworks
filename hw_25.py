class Human:

    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Student(Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f'{super().__str__()}, Record Book: {self.record_book}'


class Group:

    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        self.group.add(student)

    def delete_student(self, last_name):
        student_to_remove = self.find_student(last_name)
        if student_to_remove:
            self.group.remove(student_to_remove)

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def __str__(self):
        all_students = '\n'.join([str(student) for student in self.group])
        return f'Number: {self.number}\n{all_students}'


student_1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
student_2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
group_1 = Group('PD1')
group_1.add_student(student_1)
group_1.add_student(student_2)
print(group_1)

assert str(group_1.find_student('Jobs')) == str(student_1), 'First test'
assert group_1.find_student('Jobs2') is None, 'Second test'
assert isinstance(group_1.find_student('Jobs'), Student) is True, 'Method of search should return ex'

group_1.delete_student('Taylor')
print(group_1)


group_1.delete_student('Taylor')
