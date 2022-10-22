import pandas as pd
import sqlite3
from dijkstar import Graph, find_path


def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connection to SQLite DB successful")
    except sqlite3.Error as e:
        print(f"The error '{e}' occurred")
    return connection


def build_graph(db_path="db.sqlite3"):
    graph = Graph()
    conn = sqlite3.connect(db_path)
    sql_query = pd.read_sql_query('''
                                   SELECT
                                   *
                                   FROM roads
                                   ''', conn)
    df = pd.DataFrame(sql_query)
    xx = 0
    for _, x in df.items():
        xx = len(x)
        break
    for j in range(xx):
        point = []
        for _, data in df.items():
            point.append(data[j])
        graph.add_edge(point[1], point[2], (point[3], point[0]))
    return graph


def cost_func(u, v, edge, prev):
    length, name = edge
    cost = length
    return cost


def load_graph(path="2.xlsx", path_db="db.sqlite3"):
    connection = create_connection(path_db)
    df = pd.read_excel(path, sheet_name="Roads")
    df = df.rename(columns={"road_id": "id",	"source_point_id": "sourceId", "target_point_id": "targetId", "distance": "distance"})
    df2 = pd.read_excel(path, sheet_name="Points")
    df = df2.rename(columns={"point_id": "pointId", "location_id": "locationId"})
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


def load_timetable(path="../files/1.xlsx", path_db="db.sqlite3"):
    connection = create_connection(path_db)
    df = pd.read_excel(path)
    df = df.reindex(columns=["Номер рейса", "Дата", "AD (A-прилет, D-вылет)", "Терминал", "Код а/к", "Плановое время", "Код а/п", "Аэропорт", "Тип ВС", "Номер места стоянки", "Номер гейта", "Количество пассажиров"])
    df = df.rename(columns={"Номер рейса": "number", "Дата": "date", "AD (A-прилет, D-вылет)": "type", "Терминал": "terminal", "Код а/к": "code", "Плановое время": "scheduledTime", "Код а/п": "airportCode", "Аэропорт": "airport", "Тип ВС": "planeType", "Номер места стоянки": "parkingId", "Номер гейта": "gateId", "Количество пассажиров": "passengersCount"})
    time = list(df.pop("scheduledTime"))
    date = list(df.pop("date"))
    datetime = []
    for y in range(len(date)):
        datetime.append(date[y] + " " + str(time[y]))
    df.insert(1, "datetime", datetime)
    print(df.head())
    cursor = connection.cursor()
    drop_query = '''
    DROP TABLE IF EXISTS flight;
    '''
    cursor.execute(drop_query)
    df.to_sql("flight", connection, index=False)


def make_route(start_point, destination_point, path_timetable="../files/1.xlsx", path_graph="../files/2.xlsx"):
    load_timetable(path_timetable)
    load_graph(path_graph)
    graph = build_graph()
    path_to_destination = find_path(graph, start_point, destination_point, cost_func=cost_func)
    return path_to_destination

