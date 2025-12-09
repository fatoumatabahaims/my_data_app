import sqlite3
import pandas as pd

def save_to_sql(df, table_name):
    conn = sqlite3.connect("data/data.db")
    df.to_sql(table_name, conn, if_exists="replace", index=False)
    conn.close()


def load_from_sql(table_name):
    conn = sqlite3.connect("data/data.db")
    df = pd.read_sql(f"SELECT * FROM {table_name}", conn)
    conn.close()
    return df
