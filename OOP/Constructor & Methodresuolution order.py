class A:
    def __init__(self):
        print("in A Iit")
    def feature1(self):
        print("This is feature1")
    
    def feature2(self):
        print("This is feature2")

class B:
    def __init__(self):
        print("in B init")
    def feature3(self):
        print("This is feature1")
    
    def feature4(self):
        print("This is feature2")

class C(A,B):
    def __init__(self):
        super().__init__()
        print("in C init")

    def feat(self):
        super().feature2()

a1=C()
print(a1.__init__)
a1.feature1()
a1.feat()

#In multiple inheritance method resolution order have left to right

