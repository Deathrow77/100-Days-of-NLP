from sklearn.feature_extraction.text import CountVectorizer
text = ['Hello everyone. ','My name is Paul.','This is my Blog.','My age is 27.']
cv = CountVectorizer()
cv_fit = cv.fit_transform(text)
print(cv.get_feature_names())
print(cv_fit.toarray())
