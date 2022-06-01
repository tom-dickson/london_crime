import pandas as pd
import matplotlib.pyplot as plt



def gather_data(start_21, start, end):
    """
    Draws data from the csvs into pandas frames
    """
    df1 = pd.read_csv(f'/Users/tomdickson/Desktop/london_police/london_police_data/2022-0{start}/2022-0{start}-city-of-london-street.csv')
    for i in range(start, end+1):
        frame = pd.read_csv(f'/Users/tomdickson/Desktop/london_police/london_police_data/2022-0{i}/2022-0{i}-city-of-london-street.csv')
        df1 = df1.append(frame, ignore_index=True)
    df2 = pd.read_csv(f'/Users/tomdickson/Desktop/london_police/london_police_data/2021-{start_21}/2021-{start_21}-city-of-london-street.csv')
    for i in range(start_21+1, 13):
        frame = pd.read_csv(f'/Users/tomdickson/Desktop/london_police/london_police_data/2021-{i}/2021-{i}-city-of-london-street.csv')
        df2 = df2.append(frame, ignore_index=True)
    return df2.append(df1, ignore_index=True)



def scatter_longitude_latitude(frame, column):
    """
    Creates a scatter plot of a column of the frame where the y axis is latitude
    and x axis is longitude
    """
    colors = ['r', 'b', 'g', 'y', 'm', 'c', 'k', 'lightpink',
                'darkgoldenrod', 'orangered', 'lightgrey',
                'chocolate', 'indigo', 'teal']
    counter = 0
    for x in frame[column].unique():
        df = frame[frame[column] == x]
        plt.scatter(df['Longitude'], df['Latitude'], c=colors[counter],
                    label=x, alpha=.25)
        counter += 1
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.title(f'{column} in London From October 2021 to March 2022')
    plt.legend()
    plt.show()


def bar_counts(df, col):
    """
    Creates a bar chart of the counts of a column of the frame
    """
    counts = df[col].value_counts()
    counts.plot(kind='barh', title=f'London {col.lower()} From October 2021 to March 2022')
    plt.yticks(fontsize=5)
    plt.show()


def plot_lines(df, col):
    """
    Creates a line graph of the counts of a column over each month
    """
    months = df['Month'].unique()
    for val in df[col].unique():
        count = []
        for month in months:
            by_month = df[(df['Month'] == month) & (df['Crime type'] == val)]
            count.append(by_month.shape[0])
        plt.plot(months, count)
    plt.legend(df[col].unique())
    plt.title(f'{col} in London by month, October 2021 to March 2022')
    plt.show()


df = gather_data(10, 1, 3)
scatter_longitude_latitude(df, 'Crime type')
