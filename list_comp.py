names=["Chanuka","joe","Dinuwan"]

l=[]

for person in names:
    l.append(person+' dumped me')

print(l)

print([person for person in names])

movies_and_ratings={"Harry Pottor":8.0,"Load of the rings":8.0}

l=[]
for movie in movies_and_ratings:
    if movies_and_ratings[movie]>6:
        l.append(movie)
print(l)

print([movie for movie in movies_and_ratings if movies_and_ratings[movie]>6])

