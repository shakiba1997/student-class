import abc
from abc import abstractmethod


class Person():
    name = ""
    family = ""
    age = 0
    sex = True
    phone = 0
    @abstractmethod
    def __init__(self):
        pass


class School():
    name = ""
    place = ""
    fax = ""
    telephone = ""
    Teachers = []
    ClassRooms = []
    Sections = []

    def __init__(self, name="", place="", fax=0, telephone=12):
        self.name = name
        self.place = place
        self.fax = fax
        self.telephone = telephone

    def add_teacher(self, teacher):
        self.Teachers.append(teacher)

    def add_classRoom(self, classRoom):
        self.ClassRooms.append(classRoom)

    def add_section(self, section):
        self.Sections.append(section)


class Student(Person):
    codeStudent = 0
    codeMelly = 0
    School = None
    Sections = []

    def __init__(self, name="", family="", age=1, sex=True, phone=12, codeStudent=1, codeMelly=00):
        self.name = name
        self.family = family
        self.age = age
        self.sex = sex
        self.phone = phone
        self.codeStudent = codeStudent
        self.codeMelly = codeMelly
        self.Sections = []

    def add_section(self, section):
        self.Sections.append(section)

    def getDars(self):
        for item in self.Sections:
            print(item.dars.title)


class Teacher(Person):
    edu = ""
    history = ""
    School = []
    Sections = []

    def __init__(self, name="", family="", age=0, sex=False, phone=1, edu="", history=""):
        self.name = name
        self.family = family
        self.age = age
        self.sex = sex
        self.phone = phone
        self.edu = edu
        self.history = history
        self.Sections = []

    def add_School(self,school):
        self.School.append(school)

    def add_section(self, section):
        self.Sections.append(section)

    def GetSection(self):
        return len(self.Sections)


class ClassRoom():
    code = 0
    height = 0
    level = True
    Sections = []

    def __init__(self, code=0, height=0, level=True):
        self.code = code
        self.height = height
        self.level = level
        self.Sections = []

    def add_section(self, section):
        self.Sections.append(section)


class Dars():
    code = 0
    title = ""
    Sections = []

    def __init__(self, code=0, title=""):
        self.code = code
        self.title = title
        self.Sections = []

    def add_section(self, section):
        self.Sections.append(section)


class Section():
    School = None
    Teachers = None
    ClassRooms = None
    Dars = None
    Students = []
    start = ""
    end = ""

    def __init__(self,school, teacher, classRoom, dars, student, start, end):
        self.school = school
        self.teachers = teacher
        self.classRooms = classRoom
        self.dars = dars
        self.students = student
        self.start = start
        self.end = end

    def add_Student(self,student):
        self.Students.append(student)


#client_code

objschool = School("salman farsi", "tehran", 1, 5)

teacher1 = Teacher("zeynab", "asadi", 35, True, 2, "", "")
teacher2 = Teacher("ali", "talebzade", 35, False, 2, "", "")

student1 = Student("shakiba", "davoodi", 16, True, 2, 5, 00)
student2 = Student("parastoo", "rahimpour", 16, True, 2, 5, 00)
student3 = Student("mohammad", "rezai", 16, False, 2, 5, 00)

dars1 = Dars(22, "html5")
dars2 = Dars(11, "database")

classroom1 = ClassRoom(1, 50, True)
classroom2 = ClassRoom(2, 30, False)

section = Section(objschool, teacher1, classroom1, dars1, student1, "7", "9")
section1 = Section(objschool, teacher2, classroom2, dars2, student1, "10", "12")

student1.add_section(section)
student1.add_section(section1)
student2.add_section(section)
student3.add_section(section)


student1.getDars()

section.add_Student(student1)
section.add_Student(student2)
section.add_Student(student3)

teacher1.add_section(section)
teacher1.add_section(section1)
teacher2.add_section(section)

dars1.add_section(section)

objschool.add_section(section)

print(teacher2.GetSection())