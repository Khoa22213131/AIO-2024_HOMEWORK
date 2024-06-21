import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from TN.ex5 import Student, Person
from TN.ex6 import Teacher
from TN.ex7 import Doctor
from abc import ABC, abstractmethod


class Ward:
    def __init__(self, name: str):
        self.__name = name
        self.__listPeople = list()

    def add_person(self, person: Person):
        self.__listPeople.append(person)

    def describe(self):
        print(f" Ward Name : {self.__name}")
        for p in self.__listPeople:
            p.describe()

    def count_doctor(self):
        count = 0
        for p in self.__listPeople:
            if isinstance(p, Doctor):
                count += 1
        return count

if __name__ == '__main__':
    student1 = Student(name=" studentA ", yob=2010, grade="7")
    teacher1 = Teacher(name=" teacherA ", yob=1969, subject=" Math ")
    teacher2 = Teacher(name=" teacherB ", yob=1995, subject=" History ")
    doctor1 = Doctor(name=" doctorA ", yob=1945, specialist=" Endocrinologists ")
    doctor2 = Doctor(name=" doctorB ", yob=1975, specialist=" Cardiologists ")
    ward1 = Ward(name=" Ward1 ")
    ward1.add_person(student1)
    ward1.add_person(teacher1)
    ward1.add_person(teacher2)
    ward1.add_person(doctor1)
    ward1.add_person(doctor2)
    print(ward1.count_doctor())
