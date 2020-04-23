import turtle

C_Turtle=turtle.Turtle()
C_Turtle.speed(15)

def square():
  
  C_Turtle.forward(100)
  C_Turtle.right(90)
  C_Turtle.forward(100)
  C_Turtle.right(90)
  C_Turtle.forward(100)
  C_Turtle.right(90)
  C_Turtle.forward(100)

#square()


elephant_weight=3000
ant_weight=0.1

if elephant_weight<ant_weight:
    square()
else:
    C_Turtle.forward(100)

print(3000>200)

while(1>0):
    square()#infinit loop If we can use break keyword we can stop our loop
print(5==5)

for i in range(5):
    square()
