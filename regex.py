import re

text="hecdinuwan@gmail.com My name Chanuka chanukadinuwan35@gmail.com"

pattern=re.compile("[a-zA-Z0-9]+@gmail.com")# \+ escape sequence

result=pattern.search(text)#a-c as a range [a-zA-Z0-9] can give

print(result)#Only search first match

result=pattern.findall(text)#Can find all similar words

print(result)
