# /bin/environment python3

import pandas as pd

key_word_list = ["ddos", "dos", "denial", "flooding", "volumetric", "denial-of-service"]

def filter_irrelevant_by_title(x:str):
  filtered = [e for e in x.lower().split() if e in key_word_list]
  if len(filtered) > 0:
    return x
  else:
    return None

if __name__ == "__main__":
   # filter works whose title do not contain key words
   df = pd.read_csv("step-0-cleaned.csv")
   df["title"] = df["title"].apply(filter_irrelevant_by_title)
   df = df.dropna(subset=['title'])
   df = df.sort_values(by=["cited", "year"], ascending=False)
   df.to_csv('step-1-filtered.csv', index=False)