# Program 5: A python program to creae student class by deriving it from the teacher class.
from teacher import Teacher
class stu(Teacher):
    def setMark(self,marks):
        self.marks=marks
    def getMark(self):
        return self.marks