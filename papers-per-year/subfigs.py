import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

sns.set_theme(style="darkgrid")
fig, axes = plt.subplots(1, 3,figsize=(8,5))

# attack figure

df = pd.read_csv("paper-per-year.csv")

sns.regplot(x="year", y="# of papers", data=df, ax=axes[0])

for line in range(0, df.shape[0]):
     axes[0].text(df['year'][line]-3, df['# of papers'][line]+0.1,
                  df["tag"][line], horizontalalignment='left',
                  size='small', color='black', weight='semibold')

axes[0].get_yaxis().set_visible(False)
axes[0].set_ylim(0, 560)
axes[0].set_xlim(1990, 2020)
axes[0].set_xlabel('Year')
axes[0].set_ylabel('')
axes[0].set_title("Papers Per Year")

# market size
df = pd.read_csv("market-size.csv")
print(df)
sns.lineplot(x="year", y="size", data=df, ax=axes[1], color='g', markers=True, marker="o")

for line in range(0, df.shape[0]):
     axes[1].text(df['year'][line]-3, df['size'][line]+0.1, df["tag"][line], horizontalalignment='left', size='small', color='black', weight='semibold')

axes[1].get_yaxis().set_visible(False)
axes[1].set_ylim(0, 5)
axes[1].set_xlabel('Year')
axes[1].set_xlim(2010, 2025)
axes[1].set_title("Market Size (Billion$)")

# paper figure
df = pd.read_csv("attacks.csv")
sns.regplot(x="x", y="y", data=df, ax=axes[2], color='r', order=3, ci=None)

for line in range(0, df.shape[0]):
     axes[2].text(df.x[line]-3, df.y[line]+0.2, df["tag"][line], horizontalalignment='left', size='small', color='black', weight='semibold')

axes[2].get_yaxis().set_visible(False)
axes[2].set_ylim(0, 2600)
axes[2].set_xlabel('Year')
axes[2].set_xlim(2000, 2020)
axes[2].set_title("Peak Traffic Rate (Gbps)")

plt.tight_layout()
# plt.show()
plt.savefig('combined-2.pdf')