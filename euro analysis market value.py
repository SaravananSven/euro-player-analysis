import pandas  as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv("C:\\Users\\sarav\\Downloads\\euro2024_players.csv")
df.info()
df=df.fillna({ "Foot":"Unkown"})
df.dropna(inplace=True)

plt.figure(figsize=(10,6))
ax=sns.barplot(x='Position',y='MarketValue',data=df,errorbar=None,palette='viridis')
ax.set_xticklabels(ax.get_xticklabels(),rotation=45,ha='right')

plt.title('Positions and Avarage Maeket Value')
plt.xlabel('Positions')
plt.ylabel('Avarage Market Value')
plt.grid(axis='y')

plt.show()

