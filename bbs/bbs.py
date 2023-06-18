import pandas as pd
import matplotlib.pyplot as plt
from pathvalidate import sanitize_filename


# define paths and import data
path = '~/OneDrive - SekII Zürich/Schulleitung/Umfragen/Belastungsstudie MNG/'
file1 = 'BBS1.xlsx'
file2 = 'BBS2.xlsx'
file3 = 'BBS3.xlsx'
file_cols = 'columns.xlsx'

cols = pd.read_excel(path+file_cols)
df1 = pd.read_excel(path+file1)
df2 = pd.read_excel(path+file2)
df34 = pd.read_excel(path+file3)

# define dataframes
cols_sel1 = cols[cols['col_include']==1]
cols_sel4 = cols[cols['col_include']==3]
cols_lst1 = cols_sel1['col_ind'].to_list()
cols_lst4 = cols_sel4['col_ind'].to_list()
df1 = df1.iloc[:, cols_lst1]
df2 = df2.iloc[:, cols_lst1]
df3 = df34.iloc[:, cols_lst1]
df4 = df34.iloc[:, cols_lst4]

df = pd.concat([df1, df2, df3])

# clean data
df.loc[df['Einschätzung_Leistung']=='knapp ', 'Einschätzung_Leistung'] = 'knapp'
df['ha_fächer_we'] = df['ha_fächer_we'].str[:-1].str.split(';')
df['ha_fächer_wt'] = df['ha_fächer_wt'].str[:-1].str.split(';')
df['pv_fächer_we'] = df['pv_fächer_we'].str[:-1].str.split(';')
df['pv_fächer_wt'] = df['pv_fächer_wt'].str[:-1].str.split(';')

herkunft = {'Vor dem Eintritt ins MNG habe ich ein Untergymnasium besucht.': 'UG',
            'Vor dem Eintritt ins MNG habe ich eine Sekundarschule besucht.': 'Sek',
            'Andere Herkunft (z.B. Hospitant etc.)': 'andere'}

df['Schulische Herkunft'] = df['Schulische Herkunft'].map(herkunft)

ziel = {'Ich möchte mit möglichst wenig Aufwand durchkommen.': 'wenig Aufwand', 
        'In Fächern, die mich interessieren, möchte ich gute Noten erreichen.': 'gute Noten in einzelnen Fächern',
        'Ich möchte in möglichst vielen Fächern gute Noten erreichen.': 'gute Noten in vielen Fächern',
        'Ich möchte in möglichst vielen Fächern sehr gute Noten erreichen.': 'sehr gute Noten in vielen Fächern'}

df['Ziel'] = df['Ziel'].map(ziel)


degree = {1: '1 - gar nicht', 2: '2 - wenig', 3: '3 - mittel', 4: '4 - stark', 5: '5 - sehr stark'}

# df['zeitl_bel_7d'] = df['zeitl_bel_7d'].map(degree)
# df['mental_bel_7d'] = df['mental_bel_7d'].map(degree)

# define additional columns with numerical data instead of strings
time_str2flt = {'0 - 1 Stunde': 0.5, '1 - 2 Stunden': 1.5, '2 - 3 Stunden': 2.5, '3 - 4 Stunden': 3.5, '4 - 5 Stunden': 4.5, 
                '5 - 6 Stunden': 5.5, '6 - 7 Stunden': 6.5, 'mehr': 7.5, }

df['pv_zeit_we_flt'] = df['pv_zeit_we'].map(time_str2flt)
df['ha_zeit_we_flt'] = df['ha_zeit_we'].map(time_str2flt)
df['pv_zeit_wt_flt'] = df['pv_zeit_wt'].map(time_str2flt)
df['ha_zeit_wt_flt'] = df['ha_zeit_wt'].map(time_str2flt)

count_pres_str2flt = {'1-3': 2.0, '4-6': 5.0, '7-9': 8.0, '10 und mehr': 11.0}
freq_nh_str2flt = {'nein': 0.0, 'weniger als einmal pro Woche': 0.5, 'einmal pro Woche': 1.0, 'zweimal pro Woche': 2.0, 
                 'mehr als zweimal pro Woche': 3.0}
count_nh_str2flt = {'Keines': 0.0, '1 Fach': 1.0, '2 Fächer': 2.0, '3 Fächer': 3.0, 'mehr': 4.0}

df4['anz_vorträge_arbeiten_flt'] = df4['anz_vorträge_arbeiten'].map(count_pres_str2flt)
df4['nachhilfe_frequenz_flt'] = df4['nachhilfe_frequenz'].map(freq_nh_str2flt)
df4['nachhilfe_fächer_flt'] = df4['nachhilfe_fächer'].map(count_nh_str2flt)

# define labels for pie charts
orders = {'Klassen': ['1. Klasse', '2. Klasse', '3. Klasse'], 
          'Schwerpunktfach': ['Biologie/Chemie', 'Physik/Anwendungen der Mathematik'], 
          'Geschlecht': ['männlich', 'weiblich', 'andere Identität'], 
          'Leistung': ['knapp', 'durchschnittlich', 'gut', 'sehr gut'], 
          'Herkunft': ['UG', 'Sek', 'andere'], 
          'Ziel': ['wenig Aufwand', 'gute Noten in einzelnen Fächern', 'gute Noten in vielen Fächern', 'sehr gute Noten in vielen Fächern']}

cols['labels'] = cols['labels'].map(orders)


df_m = df[df['Geschlecht']=='männlich']
df_w = df[df['Geschlecht']=='weiblich']
df_a = df[df['Geschlecht']=='andere Identität']

df_1 = df[df['Klassenstufe']=='1. Klasse']
df_2 = df[df['Klassenstufe']=='2. Klasse']
df_3 = df[df['Klassenstufe']=='3. Klasse']

df_sg = df[df['Einschätzung_Leistung']=='sehr gut']
df_g = df[df['Einschätzung_Leistung']=='gut']
df_d = df[df['Einschätzung_Leistung']=='durchschnittlich']
df_k = df[df['Einschätzung_Leistung']=='knapp']

df_bc = df[df['Schwerpunktfach']=='Biologie/Chemie']
df_pa = df[df['Schwerpunktfach']=='Physik/Anwendungen der Mathematik']


# function to plot histograms
def plot_hist(data, bins, range, suptitle, title, color, path):
    fig = plt.figure(figsize=(8, 5), dpi=150)
    mean = data.mean()
    title = title + f' (⌀ = {mean:.2f})'
    data.hist(bins=bins, range=range, rwidth=0.8, color=color, ax=plt.gca())
    plt.suptitle(suptitle)
    plt.title(title)
    # plt.xticks(range(1,7))
    plt.grid(False)
    plt.tight_layout()
    plt.savefig(path)
    plt.close()

# function to plot bar charts
def plot_bar(data, suptitle, title, color, path):
    fig = plt.figure(figsize=(8, 5), dpi=150)
    data.value_counts().sort_index(ascending=True).plot.bar(color=color, ax=plt.gca())
    plt.suptitle(suptitle)
    plt.title(title)
    # plt.xticks(range(1,7))
    plt.grid(False)
    plt.tight_layout()
    plt.savefig(path)
    plt.close()

# function to plot pie charts
def plot_pie(data, order, suptitle, title, path):
    fig = plt.figure(figsize=(8, 5), dpi=150)
    data.value_counts().reindex(order).plot.pie(autopct='%1.0f%%', ylabel='', ax=plt.gca())
    plt.suptitle(suptitle)
    plt.title(title)
    # plt.xticks(range(1,7))
    plt.grid(False)
    plt.tight_layout()
    plt.savefig(path)
    plt.close()


subjects = {'Bildnerisches Gestalten': 'BG', 'BildnerischesGestalten': 'BG', 'Biologie': 'B', 'Chemie': 'C', 'Deutsch': 'D', 
            'Englisch': 'E', 'Französisch/Italienisch': 'F/I', 'Geografie': 'Gg', 'Geschichte': 'G', 'Informatik': 'Inf', 
            'Mathematik': 'M', 'Physik': 'P'}

dfs = [df, df_m, df_w, df_a, df_1, df_2, df_3, df_bc, df_pa, df_sg, df_g, df_d, df_k]
labels = ['alle', 'nur männlich', 'nur weiblich', 'nur andere Identität', '1. Klasse', '2. Klasse', '3. Klasse', 'Biologie/Chemie', 'Physik/AM', 'sehr gut', 'gut', 'durchschnittlich', 'knapp']
suffixes = ['_all', '_m', '_w', '_a', '_1', '_2', '_3', '_bc', '_pa', '_sg', '_g', '_d', '_k']
colors = ['Black', 'CornflowerBlue', 'LightPink', 'DarkSalmon', 'AntiqueWhite', 'BurlyWood', 'DarkGoldenRod', 'DarkSlateBlue', 'FireBrick', 'LightGreen', 'MediumSeaGreen', 'LightSlateGrey', 'PaleVioletRed']

for dfr, label, suffix, color in zip(dfs, labels, suffixes, colors):
    for index, row in cols.iterrows():
        if row['col_include'] == 1.0:
            column = row['col_name']
            suptitle = row['col_description']
            fn = sanitize_filename(column)
            path = 'figures/'+fn+suffix+'.png'

            if row['col_diag'] == 'bar':
                plot_bar(dfr[column], suptitle, label, color, path)

            if row['col_diag'] == 'bar_exp':
                dfplot = dfr.explode(column)
                data = dfplot[column].map(subjects)
                plot_bar(data, suptitle, label, color, path)

            if row['col_diag'] == 'hist':
                plot_hist(dfr[column], 5, (0.5, 5.5), suptitle, label, color, path)

            if row['col_diag'] == 'pie':
                if column == 'Schwerpunktfach' and (suffix == '_1' or suffix == '_2'):
                    pass
                else:
                    order = row['labels']
                    plot_pie(dfr[column], order, suptitle, label, path)