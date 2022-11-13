import pandas as pd


def read_csv():
    df = pd.read_csv("https://www.sololearn.com/uploads/ca-covid.csv")


def separ(df, s=''):
    if s:
        print(s)
    print(df)
    print('-' * 30)
    print('-' * 30)


def create_dataframe():
    data = {
        'date': ["25.01.20", "26.01.20", "27.01.20", "28.01.20", "29.01.20", "27.12.20", "28.12.20", "29.12.20",
                 "30.12.20",
                 "31.12.20"],
        'cases': [1, 1, 0, 0, 0, 37555, 41720, 34166, 32386, 32264],
        'deaths': [0, 0, 0, 0, 0, 62, 246, 425, 437, 574],
        'month': ["January", "January", "January", "January", "January", "December", "December", "December", "December",
                  "December", ]
    }

    df = pd.DataFrame(data)
    return df


def add_df(df):
    df['ratio'] = df['deaths'] / df['cases']
    df['ratio_1'] = df['cases'] / df['deaths']


def output(df):
    separ(df['ratio'].max(), "df['ratio'].max()")
    separ(df['ratio_1'].max(), "df['ratio_1'].max()")
    separ(df[df['ratio'] == df['ratio'].max()], "df[df['ratio'] == df['ratio'].max()]")


# df.drop('state', axis=1, inplace=True)

# df['month'] = pd.to_datetime(df['date'], format="%d.%m.%y").dt.month_name()

# df['area'] = df['width']*df['height']


if __name__ == '__main__':
    print()
    df = create_dataframe()
    separ(df, 'df_begin')
    df.set_index('date', inplace=True)
    separ(df, 'df_begin_1')
    add_df(df)
    output(df)
