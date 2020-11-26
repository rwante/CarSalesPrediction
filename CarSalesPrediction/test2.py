import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('data.csv', sep=';')

plt.scatter(df['Km'], df['Fiyat'], color='red')
plt.xlabel('Km', fontsize=14)
plt.ylabel('Fiyat', fontsize=14)
plt.legend()
plt.grid(True)
plt.show()