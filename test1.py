from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer

text = "Hi there! I'm writing a simple code, which is very cooler and cools studies and studying"

tokens1 = text.split(" ")
tokens = word_tokenize(text)

print(tokens1)
print("tokens are", end = ": ")
print(tokens)
print("filtered text is: ", end = "")
stopWords = stopwords.words("english")
filteredWords = [w for w in tokens if not w in stopWords]
ps = PorterStemmer()
wl = WordNetLemmatizer()
stems = [ps.stem(f) for f in filteredWords]
lemaas = [wl.lemmatize(f) for f in filteredWords]

print(filteredWords)
print("stems are: ", end = "")
print(stems)
print("lemmas are: ", end = "")
print(lemaas)

buys = ["wait", "waits", "waited", "waiting"]
lemaas = [wl.lemmatize(f) for f in buys]
stems = [ps.stem(f) for f in buys]
print(stems)
print(lemaas)