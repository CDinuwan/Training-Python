class Computer:
    speed=0
    def config(self):
        print("i5,16gb,1TB")


x=9
print(type(x))

a='8'
com1=Computer()
com2=Computer()

print(type(com1))

com1.config()
Computer.config(com1)
Computer.config(com2)

a=5
a.bit_length()