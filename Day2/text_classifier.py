from textblob.classifiers import NaiveBayesClassifier
text = [('Today is a great day', 'pos'), ('What a wonderful day', 'pos'), ('Awesome weather today', 'pos'),('Its so warm today', 'neg'), ('Its going to rain', 'neg')]
classifier = NaiveBayesClassifier(text)
print(classifier.classify('Its so great today '))
