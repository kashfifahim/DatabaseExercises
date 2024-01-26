# Winter 2024
# Utility Class to support db applications
# Kashfi Fahim
# Collaborated with class

import pymysql
import time
import texttable
import json
import csv
import xml.etree.ElementTree as ET
from io import StringIO
import OutputUtil as ou


DB = 'udb'
ASSN = None


def make_pivot_tables(examples, ASSN):
    html_tables = []
    for example in examples:
        html_tables += [pivot_table(example[0], example[1], example[2], example[3])]
    output_file = ASSN.replace(" ", "") + "-pivot-tables.html"
    title = "Pivot Tables for select examples"
    ou.write_html_file_new(output_file, title, html_tables, True, None, True)


def pivot_table(table, column_x, column_y, column_val):
    query = f"SELECT DISTINCT {column_x} FROM {table}"
    comment = f"Get all distinct values of {column_x} from {table} for pivot table"
    headers, data = run_query(query, comment, DB, ASSN)
    query_parts = [
        f"SUM(CASE WHEN {column_x} = '{row[0]}' THEN {column_val} ELSE 0 END) AS {row[0].replace('.', '_').replace(' ', '_')}"
        for row in data
    ]
    query = f"SELECT {column_y}, " + ",\n ".join(query_parts) + f" FROM {table} GROUP BY {column_y}"
    comment = f"Build a pivot table for {column_x} vs {column_y} for {table}"
    headers, data, = run_query(query, comment, DB, ASSN)

    numeric = [all([is_number(data[i][j]) for i in range(len(data))]) for j in range(len(data[0]))]
    types = ["N" if numeric[j] else "S" for j in range(len(numeric))]
    alignments = ["r" if numeric[j] else "l" for j in range(len(numeric))]
    table = [comment, headers, types, alignments, data]
    return table


def restore_data(name):
    query = f"SELECT * FROM backup where dtm = (SELECT MAX(dtm) FROM backup WHERE lower(relation) = '{name.lower()}')"
    desc = f"Retrieve the lastest backup row for the table {name}"
    headers, data = run_query(query, desc, DB, ASSN)
    print(headers)


# [3c] Create a Python function from_json(json) that converts the json into headers (1D) and data (2D)
def from_json(json_string):
    # Parse the JSON string
    data_list = json.loads(json_string)
    # Extract headers (assuming all objects have the same keys)
    headers = list(data_list[0].keys()) if data_list else []
    # Extract data
    data = [[row[header] for header in headers] for row in data_list]
    return headers, data


# [3b] Create a Python function from_xml(xml) that converts the xml into headers (1D) and data (2D)
def from_xml(xml_string):
    # Parse the XML string
    root = ET.fromstring(xml_string)
    # Assuming all children of the root have the same structure
    # and the first child represents the structure
    headers = [elem.tag for elem in root[0]]
    # Extract data
    data = [[elem.text for elem in row] for row in root]
    return headers, data


# [3a] Create a Python function from_csv(csv) that converts the csv into headers (1D) and data (2D)
def from_csv(csv_string):
    # Use StringIO to turn the CSV string into a file-like object
    f = StringIO(csv_string)
    # Use csv.reader to parse the file-like object
    reader = csv.reader(f)
    # Extract headers (first row)
    headers = next(reader)
    # Extract data (remaining rows)
    data = [row for row in reader]
    return headers, data


# [2c] Create a Python function to_json(headers, data) that converts the headers and data into JSON format
def to_json(title, headers, data):
    # Creating a list of dictionaries for each row in data
    data_dicts = [{headers[j]: str(data[i][j]) for j in range(len(headers))} for i in range(len(data))]
    # Use the json module to convert the data into JSON format
    json_data = json.dumps({title: data_dicts}, indent=2)
    return json_data


# [2b] Create a Python function to_xml(headers, data) that converts the headers and data into XML format
def xml_clean(item):
    return str(item).replace("&", "&amp;")


def to_xml_(title, headers, data):
    nl = "\n"
    headers = [header.replace(" ", "") for header in headers]
    x_header = '<?xml version="1.0" encoding="UTF-8"' + '?>'
    x_title = nl + ou.create_element("title", xml_clean(title))
    content = ""
    for row in data:
        x_items = nl + "".join([ou.create_element(headers[i], xml_clean(row[i])) for i in range(len(row))])
        x_row = ou.create_element("row", x_items)
        content += x_row
    x_body = nl + ou.create_element("root", x_title + content)
    xml = x_header + x_body
    return xml


# [2a] Create a Python function to_csv(headers, data) that converts the headers and data into CSV format
def to_csv(headers, data):
    s_headers = ','.join(headers)
    s_data = '\n'.join([",".join([str(col) for col in row]) for row in data])
    return s_headers + '\n' + s_data


# [4] Create a Python function backup_table(name)
def backup_table(name, DB, ASSN):
    query = f"SELECT * FROM {name}"
    desc = f"Retrieve rows from {name} for backup"
    headers, data = run_query(query, desc, DB, ASSN)
    csv_data = to_csv(headers, data)
    # print(csv_data)
    xml_data = to_xml_(name, headers, csv_data)
    # print(xml_data)
    json_data = to_json(name, headers, data)
    print(json_data)
    query2 = (f"INSERT into backup (relation, num_rows, num_cols, csv_length, xml_length, json_length, csv_data) "
              f"values ('{name}', {len(data)}, {len(headers)}, {len(csv_data)},{len(xml_data)}, {len(json_data)}, ',' '{len(csv_data)}')")
    desc2 = f"Save copy of table {name} in different formats"
    headers2, data2 = run_query(query2, desc2, DB, ASSN)


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


def retrieve_query_log(assignments, db):
    query_log = []
    for assignment in assignments:
        sql = f"select * from query where query_assn = '{assignment}'"
        desc = f"retrieve all queries executed for {assignment}"
        headers, data = run_query(sql, desc, db, assignments[-1])
        alignments = ["l"] * len(headers)
        types = ["S"] * len(headers)
        query = [desc, headers, types, alignments, data]
        query_log.append(query)
    output_file = assignment.replace(" ", "") + "-query-history.html"
    title = "All queries for assignment to date"
    ou.write_html_file_new(output_file, title, query_log, True, None, None)


def is_float(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


def get_ruler_for_html(length):
    ruler1 = "".join([str(10 * i).rjust(10, ' ') for i in range(1, 2 + int(length / 10))])
    ruler1 = ruler1.replace(" ", '&nbsp;')
    ruler2 = "0123456789" * (1 + int(length / 10))
    return ruler1 + "<br>" + ruler2


def is_number(x):
    return isinstance(x, int) or isinstance(x, float) or (isinstance(x, str) and is_float(x))


def process_queries(comments, queries, db, assignment, format=""):
        tables = []
        for i in range(len(queries)):
            query = queries[i]
            comment = comments[i]
            try:
                # print('INSIDE PROCESS QUERIES')
                if format in ["F", "V"]:
                    headers, data, cursor_desc = run_query(query, comment, db, assignment, True)
                    print(cursor_desc)
                    add_formatted_data(cursor_desc, data, format, headers)
                else:
                    headers, data = run_query(query, comment, db, assignment)
                if len(headers) == 0:
                    continue
                # check if data returned is a numbers column or not
                numeric = [all([is_number(data[i][j]) for i in range(len(data))]) for j in range(len(data[0]))]
                types = ["N" if numeric[j] else "S" for j in range(len(numeric))]
                alignments = ["r" if numeric[j] else "l" for j in range(len(numeric))]
                table = [comment, headers, types, alignments, data]
                tables.append(table)
            except Exception as e:
                print(f"Error processing query: {query}\nError: {e}\n\n", query)
        output_file = assignment.replace(" ", "") + ".html"
        title = f"All queries for '{assignment}'"
        ou.write_html_file_new(output_file, title, tables, True, None, True)


def add_formatted_data(cursor_desc, data, format, headers):
    headers.append(("Fixed" if format == "F" else "Variable") + "-Length Format")
    column_widths = [desc[3] for desc in cursor_desc]
    for row in data:
        # print(format)
        if format == "F":
            record = "".join([str(row[i]).ljust(column_widths[i], " ") for i in range(len(column_widths))])
            record = record.replace(" ", "&nbsp;")
        else:
            record = "|".join([str(row[i]) for i in range(len(column_widths))])
        ruler = "<tt> " + get_ruler_for_html(sum(column_widths)) + "<br>" + record + " </tt>"
        row.append(ruler)


def read_queries(file_name):
    with open(file_name, "r") as file:
        comments = []
        sqls = []
        text = file.read()
        queries = text.strip().split(";")
        for query in queries:
            if len(query.strip()) == 0:
                continue
            if "*/" in query:
                comment, sql = query.split("*/", 1)
                comment = comment.replace("/*", "").strip()
            else:
                comment = f"Query from: '{file_name}'"
                sql = query
            sql = sql.strip()
            if "CREATE FUNCTION" in sql.upper() or "CREATE PROCEDURE" in sql.upper():
                sql = sql.replace("##", ";")
                print(f"REPLACED ## with {sql}")
            comments.append(comment)
            sqls.append(sql)

        return comments, sqls