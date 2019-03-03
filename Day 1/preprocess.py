import re
sentence = 'John has been selected for the trial phase this time. Congrats!!'
sentence = sentence.lower()

sentence = sentence.replace('!', '').replace('.', '')
print(sentence)

words = sentence.split()
positive_words = ['Congrats']
result = list(set(words) - set(positive_words))
print(result)
