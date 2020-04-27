class A:
    def feature1(self):
        print("This is feature1")
    
    def feature2(self):
        print("This is feature2")

class B:
    def feature3(self):
        print("This is feature1")
    
    def feature4(self):
        print("This is feature2")

class C(A,B):#Multiple inheritance/Multilevel inheritance
    def feature5(self):
        print("This is feature5")

a1=A()

a1.feature1()
a1.feature2()

b1=B()
b1.feature1()#Inheritence