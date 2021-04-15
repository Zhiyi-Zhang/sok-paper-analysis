import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = None

sdn = ['sdn', 'defined']
iot = ['iot', 'thing', 'things', 'home']
ai = ['neural', 'learning', 'machine', 'artificial', 'intelligence', 'deep']
capability = ['capability', 'tva', 'capabilities', 'siff']
filter = ['filter', 'ingress', 'filtering', 'filters']

def collect_data():
    years = list()
    columns = ['SDN', 'IoT', 'Machine Learning', 'Capability', 'Filter']
    values = list()
    raw = pd.read_csv("step-2-word-count.csv")
    for i in range(1990, 2020):
      temp = list()
      years.append(i+1)
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
    sns.set_theme(style="darkgrid")
    fig, ax = plt.subplots(figsize=(8, 4))
    sns.lineplot(data=df, linewidth=2.5, ax=ax)
    ax.locator_params(integer=True)
    ax.set_xlim(2000, 2020)
    ax.set_ylabel('Published Papers')
    ax.set_xlabel('Year')
    plt.tight_layout()
    # plt.show()
    fig.savefig("step-3-1-key-words.pdf")
