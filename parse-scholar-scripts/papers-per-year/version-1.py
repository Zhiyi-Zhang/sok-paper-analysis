import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

sns.set_theme(style="darkgrid")
fig, ax = plt.subplots()

# attack figure

df = pd.read_csv("step-1-filtered.csv")
count_df = df["year"].value_counts().rename_axis('year').reset_index(name='# of papers')
count_df = count_df.sort_values(by=["year"])

sns.regplot(x="year", y="# of papers", data=count_df, ax=ax)
ax.set_ylim(0, 560)
ax.set_xlabel('Year')
ax.set_ylabel('# of DDoS Related Papers / Year')

# paper figure
ax2 = ax.twinx()
df = pd.read_csv("raw-data/attacks.csv")
sns.regplot(x="x", y="y", data=df, ax=ax2, color='r', order=3, ci=None)

for line in range(0,df.shape[0]):
     plt.text(df.x[line]+0.2, df.y[line], df["tag"][line], horizontalalignment='left', size='medium', color='black', weight='semibold')

ax2.set_ylabel('Peak Traffic Rate (Gbps)')
ax2.set_ylim(0, 2600)

ax.set_title('DDoS Paper Publication and Scale of DDoS Attack')
ax.set_xlim(1990, 2025)
plt.tight_layout()
plt.savefig('combined.pdf')