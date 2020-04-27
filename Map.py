from functools import reduce

def add_all(a,b):
    return a+b

nums=[3,2,6,8,9,7,9]
even=list(filter(lambda n: n%2==0,nums))
print(even)

doubles=list(map(lambda n: n+2,even))
print(doubles)

sum=reduce(lambda a,b: a+b,doubles)
print(sum)