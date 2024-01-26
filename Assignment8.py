# Winter 2024
# Assignment 8 - "Complex Data Types"
# Kashfi Fahim
# Collaborated with class

import Assignment5 as as5
import Assignment3 as as3
import OutputUtil as ou
import json
import csv
import xml.etree.ElementTree as ET
from io import StringIO

ASSN = "Assignment 8"
DB = "udb"


# [5] Create a Python function restore_data(name, format) that will
def restore_data(name):
    query = f"SELECT * FROM backup where dtm = (SELECT MAX(dtm) FROM backup WHERE lower(relation) = '{name.lower()}')"
    desc = f"Retrieve the lastest backup row for the table {name}"
    headers, data = as3.run_query(query, desc, DB, ASSN)
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
def backup_table(name):
    query = f"SELECT * FROM {name}"
    desc = f"Retrieve rows from {name} for backup"
    headers, data = as3.run_query(query, desc, DB, ASSN)
    csv_data = to_csv(headers, data)
    # print(csv_data)
    xml_data = to_xml_(name, headers, csv_data)
    # print(xml_data)
    json_data = to_json(name, headers, data)
    print(json_data)
    query2 = (f"INSERT into backup (relation, num_rows, num_cols, csv_length, xml_length, json_length, csv_data) "
              f"values ('{name}', {len(data)}, {len(headers)}, {len(csv_data)},{len(xml_data)}, {len(json_data)}, ',' '{len(csv_data)}')")
    desc2 = f"Save copy of table {name} in different formats"
    headers2, data2 = as3.run_query(query2, desc2, DB, ASSN)


def main():
    comments, queries = as5.read_queries("Assignment8.sql")
    as5.process_queries(comments, queries, DB, ASSN)

    udb_tables = ['advisor', 'classroom', 'course', 'department', 'instructor', 'math_circle',
                  'math_shape2d', 'math_shape3d', 'prereq', 'query', 'section',
                  'section', 'student', 'takes', 'teaches', 'time_slot']
    for table in udb_tables:
        backup_table(table)

    html_tables = []
    for table in udb_tables:
        html_tables += restore_data(table)
    output_file = assn.replace(" ", "") + "- restoration.html"
    title = "Restoration of all original University Database Tables"
    ou.write_html_file_new(output_file, title, html_tables, True, None, True)

    restore_data('student')

    comments, queries = as5.read_queries("Analytics.sql")
    as5.process_queries(comments, queries, DB, ASSN+"a")


if __name__ == "__main__":
    main()