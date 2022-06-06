import pandas as pd
import matplotlib.pyplot as plt

"""
Provides functions for analyzing which crimes are most or least
likely to result in prosecution
"""

df = pd.read_csv('full_data.csv')

df2 = df[df['Last outcome category'] != 'Under investigation']


def plot_found_suspect(df, crime):
    """
    Given a crime type, plots a bar graph comparing all cases to
    cases where a suspect was not prosecuted, ignores cases undeer investigation
    """
    column = df[df['Crime type'] == crime]
    no_suspect = column[(column['Last outcome category'] == 'Unable to prosecute suspect')
                | (column['Last outcome category'] == 'Investigation complete; no suspect identified')]
    suspect_dict = {'total cases': column.shape[0],
                    'no suspect prosecuted': no_suspect.shape[0]}
    plt.bar(suspect_dict.keys(), suspect_dict.values())
    plt.title(f"No prosecutions for {crime} in London from October 2021 to March 2022.{round(no_suspect.shape[0] / column.shape[0], 2)}")
    plt.show()


def plot_percent_cases_not_pros(df, percentage=True):
    """
    Plots bar charts either comparing rates of resolution across all crimes
    (pecentage=True) or plotting non-resolved cases against total cases
    (percentage = False)
    """
    df = df[df['Crime type'] != 'Anti-social behaviour']
    dict ={}
    totals = {}
    not_pros = {}

    if percentage:
        to_remove =  ['Action to be taken by another organisation',
                    'Status update unavailable',
                    'Formal action is not in the public interest']
        df = df[~df['Last outcome category'].isin(to_remove)].dropna(axis=0, subset=['Last outcome category'])

    for crime in df['Crime type'].unique():
        find_crimes = df[df['Crime type']== crime]
        total_crimes = find_crimes.shape[0]
        not_prosecuted = find_crimes[find_crimes['Last outcome category'].isin(['Investigation complete; no suspect identified', 'Unable to prosecute suspect'])]
        dict[crime] = round(not_prosecuted.shape[0] / total_crimes, 2)
        not_pros[crime] = not_prosecuted.shape[0]
        totals[crime] = find_crimes.shape[0]
    if percentage:
        plt.bar(dict.keys(), dict.values())
        plt.title(f'Percentage of {crime} cases not prosecuted in London, October 2021 to March 2022')
        plt.xticks(fontsize=4)
    else:
        plt.bar(totals.keys(), totals.values())
        plt.legend('Total crimes')
        plt.bar(not_pros.keys(), not_pros.values(), color='tab:orange')
        plt.legend('Crimes not prosecuted')
        plt.title('London crimes vs those which did not result in prosecution, October 2021 - March 2022')
        plt.xlabel('Crime type')
        plt.ylabel('Number of crimes')
        plt.xticks(fontsize=4)
    plt.show()


plot_percent_cases_not_pros(df2, True)
