import numpy as np
import pandas as pd
import matplotlib

classes = pd.read_excel('data/klassen_21-22.xlsx')
classes = classes.drop(classes.index[-7:])
classes = classes.drop(['Spalte1'], axis=1)
classes['Imm'].fillna('nein', inplace=True)
classes['Wechsel SPF'].fillna('', inplace=True)
classes['Bemerkungen'].fillna('', inplace=True)
classes['ZZ'].fillna('', inplace=True)



print('höchster Notenschnitt: ', classes['MW'].max())
print('tiefster Notenschnitt: ', classes['MW'].min())
print('mittlerer Notenschnitt: ', classes['MW'].mean())

classes['MW'].plot.hist(bins=10)