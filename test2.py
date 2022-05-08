from multiprocessing.spawn import import_main_path
import nltk
from nltk import word_tokenize
from nltk import WordNetLemmatizer, PorterStemmer
text = "Today is Sunday, then what will be tomorrow?"

tokens = word_tokenize(text)
print("Pos tags are: ")
print(nltk.pos_tag(tokens))

text1 = nltk.Text(word.lower() for word in tokens)
print(text1.similar("today"))

print("Noun: ")
word_tag_pairs = nltk.corpus.treebank.tagged_words(tagset='universal')
noun_preceders = [a for (a, b) in word_tag_pairs if b == 'NOUN']
fdist = nltk.FreqDist(noun_preceders)
res = [tag for (tag, _) in fdist.most_common()][0:100]
print(res)

print("Verb: ")
wsj = nltk.corpus.treebank.tagged_words(tagset='universal')
word_tag_fd = nltk.FreqDist(wsj)
res2 = [wt[0] for (wt, _) in word_tag_fd.most_common() if wt[1] == 'VERB'][0:100]
print(res)

sentence="Hello Guru99, You have to build a very good site and I love visiting your site."
words = word_tokenize(sentence)
ps = PorterStemmer()
for w in words:
    rootWord=ps.stem(w)
    print(rootWord)

wordnet_lemmatizer = WordNetLemmatizer()
text = "studies studying cries cry"
tokenization = nltk.word_tokenize(text)
for w in tokenization:
    print("Lemma for {} is {}".format(w, wordnet_lemmatizer.lemmatize(w)))