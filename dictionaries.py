from collections import OrderedDict

dictionary={'bananas':5,'oranges':3}

print(dictionary)

print(dictionary['bananas'])#wrong key get key error

print(dictionary.get('bananas'))

contacts={
    'Chanuka':[456256,'hecdinuwa@gmail.com'],
    'Dinuwan':{'phone':685462,'email':'chanukadinuwan35@gmail.com'},
    'Hewa':895666
    }

print(contacts['Chanuka'])
print(contacts['Dinuwan'])

sentence="I like my name chanuka"

print(sentence.split(" "))

word_count={
    'I':1,
    'like':2,
    'my':3,
    'name':4,
    'chanuka':5}
print(word_count)

word_count['my']=word_count['my']+1
print(word_count)

print(word_count.items())
print(list(word_count.items()))

print(word_count.keys())

print(word_count.values())

print(word_count.pop('I'))
print(word_count)

print(word_count.popitem())#lastone

word_count['I']=1000
print(word_count)

word_count.values()
print(word_count)

word_count.clear()
print(word_count)
