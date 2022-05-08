import nltk
import re

from nltk.corpus import treebank

text = "Hi there! How are you today && ?"
text = text.lower()

s = re.sub(r'[^a-zA-Z0-9\s]', "", text)
tokens = [token for token in s.split(" ") if token != '']
print(tokens)

print(list(nltk.ngrams(tokens, 5)))

train_data = treebank.tagged_sents()[0:3000]
test_data = treebank.tagged_sents()[3000:]

# text = "Various of the apartments are of the terrace type being on the ground floor so that the entrance is direct" 
# bigram_tagger = nltk.BigramTagger(train_data)
# bigram_Tg = bigram_tagger.tag(text)
# unseen_text = "the population of the congo is 13.5 million, divided into at least 7 major culture,clusters and innumerable tribes speaking 400 separate dialects."
# res2 = bigram_tagger.tag(test_data[0])
# res, a = bigram_tagger.evaluate(text)
# print("Bigram tagger:" ,res2)
# print("Bigram result : ", res)