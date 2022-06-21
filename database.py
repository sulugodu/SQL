"""Contains functions for inserting data to sql database."""

import pandas as pd
from sqlalchemy import create_engine, exc
import sqlalchemy


class DataBase:
    """ Database class"""
    def __init__(self, dialect: str, host_name: str, port: str, user_name:
        str, password: str,  data_base_name:str):
        conn_string = f'{dialect}://{user_name}:{password}@{host_name}:{port}/{data_base_name}'
        self.__engine = create_engine(conn_string)
        self.__conn = None

    def check_db_connection(self) -> bool:
        """
        Checks the database connection.

        :return: bool:status of connection
        """
        if self.__conn:
            return True
        else:
            return False

    def connect_to_db(self, ):
        """
        Creates connection to database server.

        """
        try:
            if self.__conn is None:
                self.__conn = self.__engine.connect()

        except exc.SQLAlchemyError as e:
            print(f"Error while connecting to databse {e}")
            raise Exception(e)

    def insert_to_db(self, data_frame: pd.DataFrame, table_name: str):
        """
        Scripts to insert data to database.

        :param conn: connection object
        :param data_frame: data
        :param table_name: database table name
        """
        try:
            if self.__conn:
                data_frame.to_sql(table_name, self.__conn, if_exists='replace')
            else:
                raise exc.SQLAlchemyError
        except exc.SQLAlchemyError as vx:
            print(vx)
            raise Exception(vx)

    def read_from_db(self, table_name: str) -> pd.DataFrame:
        """
        Reads data from database.

        :param table_name: database table name
        :return: data
        """
        try:
            if self.__conn:
                data_frame = pd.read_sql(f"select * from {table_name}", self.__conn)
                return data_frame
            else:
                raise exc.SQLAlchemyError
        except exc.SQLAlchemyError as vx:
            print(vx)
            raise Exception(vx)

    def close_conncetion(self):
        """Close the database connection."""
        if self.__conn:
            self.__conn.close()
