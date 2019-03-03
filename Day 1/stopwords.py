import nltk
from nltk.corpus import stopwords
from nltk import word_tokenize
sentence = 'This book is about Deep Learning and Natural Language Processing!'
# Preprocessing the corpus
sentence = sentence.replace('!', '')
# Tokenizing into words
tokens = word_tokenize(sentence)

# Create a list of stopwords
stopwrds = stopwords.words('english')

new_tokens = [w for w in tokens if not w in stopwrds]
print(new_tokens)
print(set(new_tokens))
