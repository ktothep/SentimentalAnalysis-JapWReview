import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from textblob import classifiers
from textblob import TextBlob
from nltk.tokenize import word_tokenize
nltk.download('stopwords')
nltk.download('punkt')
dataset=pd.read_csv("//Users//karanprinja//Documents//Dataset//review.csv")
dataset=dataset.drop_duplicates(subset={'Brand','Review_Content'},keep='first')
dataset['Sentiment']=''

print(dataset.head())
a=dataset['Brand'].size
print(a)
def preprocessing(phrase):
    phrase = re.sub(r"won't", "will not", phrase)
    phrase = re.sub(r"can\'t", "can not", phrase)
    phrase = re.sub(r"n\'t", " not", phrase)
    phrase = re.sub(r"\'re", " are", phrase)
    phrase = re.sub(r"\'s", " is", phrase)
    phrase = re.sub(r"\'d", " would", phrase)
    phrase = re.sub(r"\'ll", " will", phrase)
    phrase = re.sub(r"\'t", " not", phrase)
    phrase = re.sub(r"\'ve", " have", phrase)
    phrase = re.sub(r"\'m", " am", phrase)
    phrase=re.sub(r"http\S+", "", phrase)
    phrase=re.sub(r"http\S+", "", phrase)
    phrase=re.sub(r"http\S+", "", phrase)
    phrase=re.sub(r"http\S+", "", phrase)
    phrase=re.sub("\S*\d\S*", "", phrase).strip()
    phrase=re.sub('[^A-Za-z0-9]+', ' ', phrase)
    return phrase
stop_words = set(stopwords.words('english'))
preprocessed=[]
for i in range(0,a):
    sentence=preprocessing(dataset['Review_Content'].values[i])
    sentence = ' '.join(e.lower() for e in sentence.split() if e.lower() not in stop_words)
    preprocessed.append(sentence)


train = [
     ('disappointing.', 'neg'),
     ('Good', 'pos'),
     ('Very subtle beautiful flavors .', 'pos'),
     ('this is my best performance.', 'pos'),
     ("what an awesome view", 'pos'),
     ('I do not like this place', 'neg'),
     ('This is training wheels for Scotch..', 'neg'),
     ("I can't deal with all this tension", 'neg'),
     ('he is my sworn enemy!', 'neg'),
     ('my friends is horrible.', 'neg')

 ]

from textblob.classifiers import NaiveBayesClassifier
cl = NaiveBayesClassifier(train)
review=[]

for j in preprocessed:

   review.append(cl.classify(j))


for k in range(0,len(review)):
    sentiment=review[k]
    dataset.iloc[k,5]=sentiment
dataset.to_csv("UpdateJapWhisky.csv", index=False, encoding='utf8')


