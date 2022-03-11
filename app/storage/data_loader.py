import sqlite3 as sql

import pandas as pd


class DataLoader:

    def postgresql_upload(self, url, table) -> pd.DataFrame:
        conn = sql.connect(url)
        df = pd.read_sql_query(f'SELECT * FROM {table}', conn)
        return df

    def file_upload(self, path: str) -> pd.DataFrame:
        if path.endswith('csv'):
            df = pd.read_csv(path)
        else:
            df = pd.read_excel(path, sheet_name='Sheet1')
        return df
