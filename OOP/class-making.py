"""Simple class."""
class Student:
    def __init__(self, name):
        self.name = name
    
    def name(self):
        return self.name
    
    def finished(self):
        return ("False")


student = Student("John")
print(student.name)       # John
print(student.finished)   # False