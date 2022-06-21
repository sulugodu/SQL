"""Functions for generating the results for the sql task."""

import pandas as pd
from db_utils import data_to_db, data_from_db


# mysql: // user1: test123 @ localhost:33060
def data_frame_csv(file_name: str, data: pd.DataFrame):
    """
    Write results to csv file.

    :param file_name: name of csv file
    :param data: data
    """
    data.to_csv(f'./{file_name}', sep=';', index=False)


def price_rank(data: pd.DataFrame):
    """

    Function to generate Ranks based on column “Price”,  grouped by “brand”.

    Saves results to csv file.

    :param data: data from the database
    """
    data_rank = data.copy()
    idx = data_rank.groupby(['brand'])['price'].transform(max) == data_rank[
        'price']
    data_rank = data_rank.loc[idx]
    data_rank['rank'] = data_rank['price'].rank(method="dense",
                                                ascending=False)
    # data_rank['ranks'] = data_rank.groupby(['brand'])['price'].rank(method="dense", ascending=False)
    data_rank_result = data_rank.sort_values(['rank'])
    data_frame_csv('rank.csv', data_rank_result)


def min_max(data: pd.DataFrame):
    """

    Function to generate Minimum and maximum of column “HDD_GB”.

    Saves results to csv file.

    :param data: data from the database
    """
    data_min_max = data.copy()
    min = data_min_max['HDD_GB'].min()
    max = data_min_max['HDD_GB'].max()
    result = pd.DataFrame(columns=['min_HDD_GB', 'max_HDD_GB'],
                          data=[[min, max]])
    data_frame_csv('min_max.csv', result)


def medina_ghz(data: pd.DataFrame):
    """

    Function to generate Median of column “GHz”, grouped by column “RAM_GB”.

    Saves results to csv file.

    :param data: data from the database
    """
    data_min_max = data.copy()
    data_median = data_min_max.groupby(['RAM_GB'])[
        'GHz'].median().to_frame().reset_index()
    data_frame_csv('median.csv', data_median)


def task_run():
    """Main function to generate results for the defined tasks."""

    try:
        ######################################
        # task 1 Import testset_B.tsv into the SQL DB

        tsv_file_path = 'testset_B.tsv'
        data_to_db(tsv_file_path)

        ######################################

        # task 2 Reads data from data  base
        dat_db: pd.DataFrame = data_from_db()

        ######################################

        # a. Ranks based on column “Price”, grouped by column “brand”
        data_clean = dat_db.drop('index', axis=1)
        price_rank(data_clean)
        print(f'CSV file is generated for task:  Ranks based on column '
              f'“Price”, '
              'grouped by column “brand”: rank.csv')

        #######################################

        # b. Minimum and maximum of column “HDD_GB”
        min_max(data_clean)
        print(f'CSV file is generated for task:  Minimum and maximum of '
              f'column '
              '"HDD_GB" : min_max.csv')

        ######################################

        # c. Median of column “GHz”, grouped by column “RAM_GB”
        medina_ghz(data_clean)
        print(f'CSV file is generated for task:  Median of column “GHz”,'
              'grouped by column “RAM_GB” :median.csv')
    except:
        print('Error in the script')


if __name__ == "__main__":
    task_run()
