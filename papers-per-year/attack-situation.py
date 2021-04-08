import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("attacks.csv")

print(df.head())

sns.set_theme(style="darkgrid")
ax = sns.regplot(x="x", y="y", data=df, order=3, ci=None)

for line in range(0,df.shape[0]):
     plt.text(df.x[line]+0.2, df.y[line], df["tag"][line], horizontalalignment='left', size='medium', color='black', weight='semibold')

ax.set_title('Peak Traffic Rate of Famous DDoS Attacks')
ax.set_xlabel('Year')
ax.set_ylabel('Peak Traffic Rate (Gbps)')
ax.set_ylim(0, 2600)
plt.tight_layout()
plt.savefig('attack.pdf')