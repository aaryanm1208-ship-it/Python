class Student:
    college = "MIT"   # class variable

    def __init__(self, name):
        self.name = name   # instance variable

s1 = Student("Aaryan")
s2 = Student("Krishna")

print(s1.college)
print(s2.college)
