import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

classes = pd.read_excel('data/klassen_21-22.xlsx')
classes = classes.drop(classes.index[-7:])
classes = classes.drop(['Spalte1'], axis=1)
classes['Imm'].fillna('nein', inplace=True)
classes['Wechsel SPF'].fillna('', inplace=True)
classes['Bemerkungen'].fillna('', inplace=True)
classes['ZZ'].fillna('', inplace=True)



print(f"höchster Notenschnitt:\t{classes['MW'].max():.2f}")
print(f"tiefster Notenschnitt:\t{classes['MW'].min():.2f}")
print(f"mittlerer Notenschnitt:\t{classes['MW'].mean():.2f}")

classes['MW'].plot.hist(bins=20)
plt.savefig('output/Notenverteilung.pdf')