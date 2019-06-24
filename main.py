import lemmatizer as lemma
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

lem = lemma.Lemmatizer()

sentence = ''

with open('sentence.txt', 'r') as sent_file:
    sentence = sent_file.readline()

print('Before:\n', sentence, '\n')

_stopwords_ = stopwords.words('indonesian')

preprocessed_sent = []

for token in word_tokenize(sentence.lower()):
    if token not in _stopwords_ and token.isalpha():
        preprocessed_sent.append(token)

lemmatized_sent = []

for token in preprocessed_sent:
    lemmatized = lem.lemmatize(token)
    # print(lemmatized)

    if(type(lemmatized) == tuple):
        lemmatized_sent.append(lemmatized[0])
    else:
        print(lemmatized)
        lemmatized_sent.append(lemmatized)

print('After:\n', " ".join(lemmatized_sent))
