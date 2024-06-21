from abc import ABC, abstractmethod


class Person (ABC):
    def __init__(self, name: str, yob: int):
        self._name = name
        self._yob = yob

    def get_yob(self):
        return self._yob

    @abstractmethod
    def describe(self):
        pass


class Student (Person):

    def __init__(self, name: str, yob: int, grade: str):
        super().__init__(name, yob)
        self._grade = grade

    def describe(self):
        print(f"Student - Name: {self._name.strip()} - YoB: {self._yob} - Grade: {self._grade.strip()}")

if __name__ == '__main__':  
    student1 = Student(name=" studentZ2023 ", yob=2011, grade="6")
    student1.describe()
