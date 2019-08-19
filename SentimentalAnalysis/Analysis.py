import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
nltk.download('stopwords')
nltk.download('punkt')
dataset=pd.read_csv("//Users//karanprinja//Documents//Dataset//review.csv")
dataset=dataset.drop_duplicates(subset={'Brand','Review_Content'},keep='first')
dataset.head()
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
filtered_preprocessed=[]
for j in preprocessed:
   print(j)

'''for i in preprocessed:
    word_tokens=word_tokenize(i)
    for w in word_tokens:
        if w not in stop_words:
            filtered_preprocessed.append(w)

print(filtered_preprocessed[50])'''

