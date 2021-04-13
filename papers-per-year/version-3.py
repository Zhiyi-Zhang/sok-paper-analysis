import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

sns.set_theme(style="darkgrid", color_codes=True)
fig, ax = plt.subplots(figsize=(8,4))

# attack figure

df = pd.read_csv("raw-data/attack-market.csv")
ax.set_ylim(0, 3)
# sns.lineplot(x="year", y="size", data=df.query("type == 'attack'"), ax=ax, color='r', markers=True, marker="o", ci=False, label='attack traffic rate')
sns.regplot(x="year", y="size", data=df.query("type == 'attack'"), ax=ax, color='r', order=3, ci=None, truncate=True, label='attack traffic rate')
# sns.lineplot(x="year", y="size", data=df.query("type == 'market'"), ax=ax, color='g', markers=True, marker="o", label='market size')
sns.regplot(x="year", y="size", data=df.query("type == 'market'"), ax=ax, color='g', order=3, ci=None, truncate=True, label='market size')
ax.legend(loc=9)
ax.set_ylabel('Peak Traffic Rate (Tbps), Market Size ($Billion)')

# paper figure
ax2 = ax.twinx()
df = pd.read_csv("raw-data/paper-per-year-from-2000.csv")
ax2.grid(False)
ax2.set_xlim(2000, 2020)
ax2.set_ylim(100, 600)
sns.regplot(x="year", y="# of papers", data=df, ax=ax2, truncate=False, label='papers per year')
ax2.legend(loc=2)
ax2.set_ylabel('Number of Papers per Year')

# ax.set_title('DDoS Paper Publication, Market Size, and Scale of DDoS Attack')
ax.set_xlabel('Year')
ax.locator_params(integer=True)
plt.tight_layout()
# plt.show()
plt.savefig('version-3.pdf')