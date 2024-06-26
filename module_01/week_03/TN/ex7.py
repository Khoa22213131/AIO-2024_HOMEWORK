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


class Doctor (Person):
    def __init__(self, name: str, yob: int, specialist: str):
        super().__init__(name, yob)
        self._specialist = specialist

    def describe(self):
        print(f"Doctor - Name: {self._name.strip()} - YoB: {self._yob} - Specialist: {self._specialist.strip()} ")

if __name__ == '__main__':
    doctor1 = Doctor(name=" doctorZ2023 ", yob=1981, specialist=" Endocrinologists ")
    doctor1.describe()
