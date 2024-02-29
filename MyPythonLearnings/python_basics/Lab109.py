from abc import ABC,abstractmethod

class ATB(ABC):
    @abstractmethod
    def perform_task1(self):
        pass
    def perform_task2(self):
        pass
class Vani(ATB):
    def perform_task1(self):
        return "Assignment 1"
    def perform_task2(self):
        return "Assignment 2"
vani = Vani()
print(vani.perform_task1())
print(vani.perform_task2())