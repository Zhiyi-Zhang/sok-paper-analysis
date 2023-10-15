import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../step-1-filtered.csv")

print(df.head())

count_df = df["year"].value_counts().rename_axis('year').reset_index(name='# of papers')
count_df = count_df.sort_values(by=["year"])

print(count_df)

sns.set_theme(style="darkgrid")
# ax = sns.histplot(data=df, x="year", binwidth=2, bins=29, kde=True)
# plt.show()

# ax = sns.lineplot(x="year", y="counts", data=count_df)
# plt.show()

ax = sns.regplot(x="year", y="# of papers", data=count_df)
# ax.set(ylim=(0, 560))
ax.set_xlim(1990, 2025)
ax.set_title('Published DDoS Related Papers')
ax.set_xlabel('Year')
ax.set_ylabel('# of DDoS Related Papers')
plt.tight_layout()
plt.savefig('paper-num.pdf')