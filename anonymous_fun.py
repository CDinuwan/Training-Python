def square(a):
    return a*a

result=square(5)
print(result)

#Functions are object in python

f=lambda a: a*a
result=f(5)
print(result)

f=lambda a,b:a+b
result=f(5,6)
print(result)