import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = None

sdn = ['sdn', 'defined', 'sdnmanager', 'sdns']
wireless = ['wireless', '802','sensor', 'mobile', 'wlan', '3g', '4g', '5g']
iot = ['iot', 'thing', 'things', 'home', 'manet']
ai = ['neural', 'learning', 'machine', 'artificial', 'intelligence', 'deep']
# blockchain = ['blockchain', 'chain', 'block', 'bitcoin', 'ethereum']
cloud = ['cloud']
traceback = ['traceback', 'trace', 'tracking', 'tracing']
web = ['web', 'http', 'website', 'webpage']
filter = ['filter', 'ingres', 'filtering', 'ingress']

def collect_data():
    years = list()
    columns = ['SDN', 'IoT', 'AI\nML', 'Cloud', 'Wireless\nMobile', 'Tracing\nTracking', 'Web', 'Filter']
    values = list()
    raw = pd.read_csv("step-2-word-count.csv")
    for i in range(2001, 2023):
      # calculate percentage
      sdn_value = raw[(raw['year']==i) & (raw['word'].isin(sdn))]['count'].sum()
      wireless_value = raw[(raw['year']==i) & (raw['word'].isin(wireless))]['count'].sum()
      iot_value = raw[(raw['year']==i) & (raw['word'].isin(iot))]['count'].sum()
      ai_value = raw[(raw['year']==i) & (raw['word'].isin(ai))]['count'].sum()
      filter_value = raw[(raw['year']==i) & (raw['word'].isin(filter))]['count'].sum()
      cloud_value = raw[(raw['year']==i) & (raw['word'].isin(cloud))]['count'].sum()
      traceback_value = raw[(raw['year']==i) & (raw['word'].isin(traceback))]['count'].sum()
      web_value = raw[(raw['year']==i) & (raw['word'].isin(web))]['count'].sum()
      sum_value = sdn_value + wireless_value + iot_value + ai_value + filter_value + cloud_value + traceback_value + web_value
      # add data point
      temp = list()
      years.append(i)
      temp.append(sdn_value/sum_value)
      temp.append(iot_value/sum_value)
      temp.append(ai_value/sum_value)
      temp.append(cloud_value/sum_value)
      temp.append(wireless_value/sum_value)
      temp.append(traceback_value/sum_value)
      temp.append(web_value/sum_value)
      temp.append(filter_value/sum_value)
      values.append(temp)
    global df
    df = pd.DataFrame(values, years, columns=columns)
    print(df.head)
    df.to_csv('step-3-1-word-count.csv', index=False)


if __name__ == "__main__":
    collect_data()
    print(df)
    sns.set_theme(style="darkgrid")
    fig, ax = plt.subplots(figsize=(8, 6))

    sns.heatmap(data=df.transpose(), ax=ax, cmap="Blues")
    # sns.lineplot(data=df, linewidth=2.5, ax=ax)
    # ax.locator_params(integer=True)
    # ax.set_xlim(2000, 2023)
    # ax.set_ylabel('Topic keyword ')
    # ax.set_xlabel('Year')
    # plt.legend(bbox_to_anchor=(0, 1.2), loc='upper left', borderaxespad=0, ncol=5)
    # plt.tight_layout()
    # plt.show()
    fig.savefig("step-3-1-key-words.pdf")
