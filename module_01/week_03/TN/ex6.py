from abc import ABC, abstractmethod


class Person (ABC):
    def __init__(self, name: str, yob: int):
        self._name = name
        self._yob = yob

    def get_yob(self):
        self._yob

    @abstractmethod
    def describe(self):
        pass


class Teacher (Person):
    def __init__(self, name: str, yob: int, subject: str):
        super().__init__(name, yob)
        self._subject = subject

    def describe(self):
        print(f"Teacher - Name: {self._name.strip()} - YoB: {self._yob} - Subject: {self._subject.strip()}")

if __name__ == '__main__':
    teacher1 = Teacher(name=" teacherZ2023 ", yob=1991, subject=" History ")
    teacher1.describe()
