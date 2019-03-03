# Matching Regular Expressions in a string
import re
words = ['Hello', 'this']
expression = '|'.join(words)
print(re.findall(expression, 'Hello world This is Parul', re.M))



# Reading from a file and splitting into strings

with open('test.txt') as f:
    words = f.read().split()

print(words)
