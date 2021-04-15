# /bin/environment python3

import pandas as pd
from nltk.corpus import stopwords
import nltk

wnl = nltk.WordNetLemmatizer()

def clean_up_title(x):
  x = str(x)
  x = x.lower().strip()
  x = x.replace('/', ' ')
  x = x.replace('(', ' ')
  x = x.replace(')', ' ')
  x = x.replace('[', ' ')
  x = x.replace(']', ' ')
  x = x.replace(',', ' ')
  x = x.replace('-', ' ')
  x = x.replace('.', ' ')
  x = x.replace(':', ' ')
  x = x.replace('–', ' ')
  return [wnl.lemmatize(word) for word in nltk.wordpunct_tokenize(x)]

if __name__ == "__main__":
   stop = stopwords.words('english')
   other_stop_words = ["attack", "attacks", "based", "ddos", "dos",
                       "denial", "flooding", "volumetric", "service",
                       "detection", "mitigation", "using"]
   stop.extend(other_stop_words)

   df = pd.read_csv("step-1-filtered.csv")
   df = df.groupby(['year'])['title'].apply(lambda x: ' '.join(x)).reset_index()
   df['title'] = df['title'].apply(clean_up_title)
   df['title'] = df['title'].apply(lambda x: [e for e in x if e not in stop])
   df = df.explode('title')
   dfg = df.groupby(['year', 'title']).agg({'title': 'count'})
   dfg.to_csv('step-2-word-count.csv')

   colnames = ['year', 'word', 'count']
   df = pd.read_csv("step-2-word-count.csv", names=colnames, header=None, skiprows = [0])
   df = df.sort_values(by=["year", "count"], ascending=False)
   df.to_csv('step-2-word-count.csv', index=False)