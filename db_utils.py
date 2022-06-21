"""Scripts for importing and reading data for sql database"""

import pandas as pd
from database import DataBase
from database_parameters import DIALECT, HOST_NAME, PORT, USER_NAME, PASSWORD,\
    TABLE_NAME, DATA_BASE_NAME


def data_to_db(file_path: str):
    """
    Write data to data base.

    :param file_path: path of file
    """
    # reading given tsv file
    data: pd.DataFrame = pd.read_table(file_path, sep='\t')
    my_db = None
    try:
        my_db = DataBase(dialect=DIALECT, host_name=HOST_NAME, port=PORT, user_name=USER_NAME, password=PASSWORD, data_base_name=DATA_BASE_NAME)
        my_db.connect_to_db()
        my_db.insert_to_db(data, TABLE_NAME)
        print('successfully inserted the data to database')
    finally:
        if my_db and my_db.check_db_connection():
            my_db.close_conncetion()


def data_from_db() -> pd.DataFrame:
    """
    Reads data from data base.

    :return: data frame
    """
    my_db = None
    try:
        my_db = DataBase(dialect=DIALECT, host_name=HOST_NAME, port=PORT,
                         user_name=USER_NAME, password=PASSWORD,
                         data_base_name=DATA_BASE_NAME)
        my_db.connect_to_db()
        dat_db = my_db.read_from_db(TABLE_NAME)
        print('successfully extracted data from database')
        return dat_db
    finally:
        if my_db and my_db.check_db_connection():
            my_db.close_conncetion()