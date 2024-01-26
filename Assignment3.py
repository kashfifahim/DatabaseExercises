# Queens College
# Database Systems (CSCI 331)
# Winter 2024
# Assignment 3 - SQL and Programming Languages
# Kashfi Fahim
# Collaborated with class

import pymysql
import time
import texttable


def get_password():
    with open('password.txt', 'r') as f:
        return f.read().strip()

password = get_password()
user = "Kashfi"
def show_database(cursor, sql_statement, desc):
    cursor.execute(sql_statement)
    results = [row[0] for row in cursor]
    print(desc + ":", results)
    return results


def log_query(query_text, query_desc, query_db, query_rows, query_user, query_assn, query_dur, conn=None):
    query_text = query_text.replace("'", "\\'")
    query = f"INSERT into query (query_text, query_desc, query_db, query_rows, query_user, query_assn, query_dur) values ('{query_text}',', {query_desc}', '{query_db}', '{(query_rows)}','{query_user}', '{query_assn}', '{(query_dur)}')"
    new_conn = False
    if conn is None:
        new_conn = True
        password = get_password()
        db = "udb"
        conn = pymysql.connect(host="localhost", user="root", passwd=password, db=db)
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()
    if new_conn:
        conn.close()


def run_query(query_text, query_desc, query_db, assignment, get_cursor_desc=False):
    query_src = assignment
    conn = pymysql.connect(host="localhost", user="root", passwd=password, db=query_db)
    start = time.time()
    cursor = conn.cursor()
    cursor.execute(query_text)
    end = time.time()
    duration = end - start
    rows = cursor.fetchall()
    conn.commit()
    log_query(query_text, query_desc, query_db, len(rows), user, query_src, duration)
    conn.close()
    query_upper = query_text.upper()
    if query_upper.startswith("SELECT") or query_upper.startswith("SHOW") or query_upper.startswith("DESC"):
        headers = [desc[0] for desc in cursor.description]
        if len(rows) == 0:
            data = [[None for _ in headers]]
        else:
            data = [[col for col in row] for row in rows]
        # print(get_cursor_desc)
        if get_cursor_desc:
            return headers, data, cursor.description
        else:
            return headers, data
    else:
        return [], []

# def run_query(query_text, query_desc, query_db, assignment):
#     query_src = assignment
#     query_db = 'udb'
#     conn = pymysql.connect(host="localhost", user="root", passwd=password, db=query_db)
#     cursor = conn.cursor()
#     rows = []
#     try:
#         start = time.time()
#         cursor.execute(query_text)
#         end = time.time()
#         duration = end - start
#         query_upper = query_text.upper()
#         if query_upper.startswith("SELECT") or query_upper.startswith("SHOW") or query_upper.startswith("DESC"):
#             headers = [desc[0] for desc in cursor.description]
#             rows = cursor.fetchall()
#             data = [[str(col) for col in row] for row in rows]
#         else:
#             conn.commit()
#             headers, data = [], []
#         log_query(query_text, query_desc, query_db, len(rows), user, query_src, duration)
#     except pymysql.Error as e:
#         print(f"An error occurred while executing the query: {e}")
#         headers, data = [], []
#     finally:
#         conn.close()
#     return headers, data


def print_table(title, headers, data, alignments=None):
    if alignments is None:
        alignments = ['l'] * len(headers)
    tt = texttable.Texttable(0)
    tt.set_cols_align(alignments)
    tt.add_rows([headers] + data, header=True)
    print(title)
    print(tt.draw())
    print()


def preliminary(password):
    conn = pymysql.connect(host="localhost", user="root", passwd=password)
    cursor = conn.cursor()
    # 1
    sql_statement = "SHOW DATABASES"
    desc = "DATABASES"
    database = show_database(cursor, sql_statement, desc)
    cursor.execute("USE udb")
    # run_query("use udg", "make udb default", "udb", assignmet)
    # 2
    sql_statement = "SHOW TABLES"
    desc = "Tables in udb"
    tables = show_database(cursor, sql_statement, desc)
    for table in tables:
        sql_statement = "DESC CLASSROOM"
        desc = "Columns in table" + table
        columns = show_database(cursor, sql_statement, desc)
    # 3
    sql_statement = "DESC CLASSROOM"
    columns = show_database(cursor, sql_statement, desc)
    desc = "Columns in table classroom"
    conn.close()
    return tables


def main():
    assignment = "Assignment 3"
    password = get_password()
    tables = preliminary(password)
    for table in tables:
        query = "SELECT * FROM " + table
        desc = "retrieve all rows from " + table
        db = "udb"
        headers, data = run_query(query, desc, db, assignment)
        print_table("table " + table, headers, data)


if __name__ == "__main__":
    main()