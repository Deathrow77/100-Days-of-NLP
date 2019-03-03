from sklearn.feature_extraction.text import TfidfVectorizer
text = ['Hello Everyone', 'My name is Parul', ' My mother gave me this name']
vect = TfidfVectorizer()
X = vect.fit_transform(text)
print(X.todense())
