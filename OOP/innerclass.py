class Student:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
        self.lap=self.Laptop()
    
    def show(self):
        print(self.name,self.rollno)
        self.lap.show()
    
    class Laptop:
        def __init__(self):
            self.brand='Acer'
            self.cpu='i3'
            self.ram=16

        def show(self):
            print(self.brand,self.cpu,self.ram)

s1=Student('Chanuka',2)
s2=Student('Dinuwan',3)

print(s1.name,s1.rollno)

s1.show()

lap=s1.lap
lap2=s2.lap

print(id(lap))
print(id(lap2))

s1.show()

lap3=Student.Laptop()