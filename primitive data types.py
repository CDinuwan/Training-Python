#primitive data types

#Integer
#Floats
#Strings
#Boolean

#Casting

x=1
float(x)
str(1)
int("34")

#Strings

str="Hello"
print(str)
print(str[1])

#Lists

a=[1,2,3,4]
b=[1,2,"string",[1,3]]
print(a)
print(b)
print(a[0])

a.insert(3,"insert")
print(a)

a.remove(3)
print(a)

a.reverse()
print(a)

numbers=[1,23,6,8]
numbers.sort()
print(numbers)

for num in numbers:
    print(num)

digits=[0,1,2,3,4,5,6,7,8,9]

name="Chanuka Dinuwan"
print(name[:3])

print(digits[3])

print(digits[-2])

print(digits[:2])

print(digits[0:2:3])

print(digits[::-1])#reverse

for i in range(len(digits)):
    #print(digits[0:i])

    print(digits[0:i+3])

