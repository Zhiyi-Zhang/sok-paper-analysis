import numpy as np
import pandas as pd
import seaborn as sns

df = None

sdn = ['sdn', 'defined']
iot = ['iot', 'thing', 'things', 'home']
ai = ['neural', 'learning', 'machine', 'artificial', 'intelligence']
capability = ['capability', 'tva']
filter = ['filter', 'ingress']

def collect_data():
    years = list()
    columns = ['SDN', 'IoT', 'Machine Learning', 'Capability', 'Filter']
    values = list()
    raw = pd.read_csv("step-2-word-count.csv")
    for i in range(1990, 2020):
      temp = list()
      years.append(i)
      temp.append(raw[(raw['year']==i) & (raw['word'].isin(sdn))]['count'].sum())
      temp.append(raw[(raw['year']==i) & (raw['word'].isin(iot))]['count'].sum())
      temp.append(raw[(raw['year']==i) & (raw['word'].isin(ai))]['count'].sum())
      temp.append(raw[(raw['year']==i) & (raw['word'].isin(capability))]['count'].sum())
      temp.append(raw[(raw['year']==i) & (raw['word'].isin(filter))]['count'].sum())
      values.append(temp)
    global df
    df = pd.DataFrame(values, years, columns=columns)
    print(df.head)


if __name__ == "__main__":
    collect_data()
    print(df)
    sns.set_theme(style="whitegrid")
    plot = sns.lineplot(data=df, palette="tab10", linewidth=2.5)
    plot.figure.savefig("step-3-1-key-words.pdf")
