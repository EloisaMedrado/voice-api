import nltk
from nltk.corpus import wordnet

nltk.download('wordnet.br')
enses = wordnet.synsets("mesa",lang=u"fre")
print(enses)

stopwords = nltk.corpus.stopwords.words('portuguese')
print(stopwords)