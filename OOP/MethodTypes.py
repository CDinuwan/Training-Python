class Student:

    school="Chanuka"

    def __init__(self,n1,n2,n3):
        self.n1=n1
        self.n2=n2
        self.n3=n3

    def avg(self):
        return (self.n1+self.n2+self.n3)/3

    def get_n1(self):
        return self.n1

    @classmethod
    def info(cls):
        return cls.school

    @staticmethod
    def infos():
        print("This is static method")

s1=Student(34,67,33)
s2=Student(32,65,98)

print(s1.avg())
print(s2.avg())
print(Student.info())
Student.infos()
