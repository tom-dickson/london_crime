import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('full_data.csv')
print(df['Last outcome category'].unique())

df2 = df[(df['Last outcome category'] != 'Under investigation')
        & (df['Last outcome category'] != 'nan')]


def plot_found_suspect(df, crime):
    column = df[df['Crime type'] == crime]
    no_suspect = column[(column['Last outcome category'] == 'Unable to prosecute suspect')
                | (column['Last outcome category'] == 'Investigation complete; no suspect identified')]
    suspect_dict = {'total cases': column.shape[0],
                    'no suspect prosecuted': no_suspect.shape[0]}
    plt.bar(suspect_dict.keys(), suspect_dict.values())
    plt.title(f'Resolutions for {crime} in London from October 2021 to March 2022')
    plt.show()
    

print(df2['Last outcome category'].unique())
plot_found_suspect(df2, 'Violence and sexual offences')
