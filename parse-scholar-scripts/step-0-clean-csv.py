# /bin/environment python3

import pandas as pd
from os import listdir
from os.path import isfile, join
import re

def list_csv_files(dir:str):
  csv_files = [f for f in listdir(dir) if isfile(join(dir, f)) and f.lower().endswith(".csv")]
  return csv_files

def clean_citation(x):
  if x is None:
    return 0
  cite = [e for e in str(x).split() if e.isdigit()]
  if len(cite) == 0:
    return 0
  return cite[0]

def clean_version(x):
  if x is None:
    return 1
  version = [e for e in str(x).split() if e.isdigit()]
  if len(version) == 0:
    return 1
  return version[0]

def clean_string(x):
  if x is None:
    return ''
  x = str(x).replace('\n', '')
  x = x.replace('\t', '')
  x = x.replace('"', '')
  return x

def identify_year(x):
  numbers = re.findall('(\d{4})', str(x))
  for number in numbers:
    number_int = int(number)
    if number_int < 2024 and number_int > 1989:
      return number
  return current_year

def read_csv_clean(file_name: str) -> pd.DataFrame:
  df = pd.read_csv(file_name)
  df["cited"] = df["cited"].apply(clean_citation)
  df["numOfVersions"] = df["numOfVersions"].apply(clean_version)
  df["snippet"] = df["snippet"].apply(clean_string)
  df["title"] = df["title"].apply(clean_string)
  return df

if __name__ == "__main__":
    dir = "../../raw-data/2023-10-15"
    csv_files = list_csv_files(dir)
    dfs = list()
    current_year = None
    for csv in csv_files:
      current_year = csv[0:4]
      print(current_year)
      temp_df = read_csv_clean(join(dir, csv))
      temp_df['year'] = temp_df["publishedData"].apply(identify_year)
      dfs.append(temp_df)
    result = pd.concat(dfs)
    result = result.drop_duplicates(subset=['title'])
    result.to_csv('step-0-cleaned.csv', index=False, columns=["year","cited","title","publishedData","numOfVersions","snippet","link"])