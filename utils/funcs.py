import pandas as pd
import sqlite3
from dijkstra import Graph


def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connection to SQLite DB successful")
    except sqlite3.Error as e:
        print(f"The error '{e}' occurred")

    return connection


def build_graph(db_path="baza.db"):
    graph = Graph()
    conn = sqlite3.connect(db_path)

    sql_query = pd.read_sql_query('''
                                   SELECT
                                   *
                                   FROM products
                                   ''', conn)

    df = pd.DataFrame(sql_query, columns=['product_id', 'product_name', 'price'])
    print(df)


def load_graph(path="2.xlsx", path_db="baza.db"):
    connection = create_connection(path_db)
    df = pd.read_excel(path, sheet_name="Roads")
    df2 = pd.read_excel(path, sheet_name="Points")
    cursor = connection.cursor()
    drop_query = ''' 
            DROP TABLE IF EXISTS roads;
            '''
    cursor.execute(drop_query)
    drop_query1 = '''
            DROP TABLE IF EXISTS points;
            '''
    cursor.execute(drop_query1)
    df.to_sql("roads", connection, index=False)
    df2.to_sql("points", connection, index=False)


def load_data():
    pass


def load_timetable(path="baza.db"):
    connection = create_connection("baza.db")
    df = pd.read_excel(path)
    cursor = connection.cursor()
    drop_query = '''
    DROP TABLE IF EXISTS flights;
    '''
    cursor.execute(drop_query)
    df.to_sql("flights", connection, index=False)


load_timetable("../files/1.xlsx")
load_graph("../files/2.xlsx")