# Winter 2024
# Assignment 9 - Pivot Tables In and Outside MySQL
# Kashfi Fahim
# Collaborated with class

import Assignment5 as as5
import Assignment3 as as3
import OutputUtil as ou

ASSN = "Assignment9"
DB = "udb"


def pivot_table(table, column_x, column_y, column_val):
    query = f"SELECT DISTINCT {column_x} FROM {table}"
    comment = f"Get all distinct values of {column_x} from {table} for pivot table"
    headers, data = as3.run_query(query, comment, DB, ASSN)
    query_parts = [
        f"SUM(CASE WHEN {column_x} = '{row[0]}' THEN {column_val} ELSE 0 END) AS {row[0].replace('.', '_').replace(' ', '_')}"
        for row in data
    ]
    query = f"SELECT {column_y}, " + ",\n ".join(query_parts) + f" FROM {table} GROUP BY {column_y}"
    comment = f"Build a pivot table for {column_x} vs {column_y} for {table}"
    headers, data, = as3.run_query(query, comment, DB, ASSN)

    numeric = [all([as5.is_number(data[i][j]) for i in range(len(data))]) for j in range(len(data[0]))]
    types = ["N" if numeric[j] else "S" for j in range(len(numeric))]
    alignments = ["r" if numeric[j] else "l" for j in range(len(numeric))]
    table = [comment, headers, types, alignments, data]
    return table


def main():
    comments, queries = as5.read_queries("Assignment9.sql")
    as5.process_queries(comments, queries, DB, ASSN)
    examples = [["product_sales", "product_name", "store_location", "num_sales"],
                ["instructor", "dept_name", "name", "salary"]]
    html_tables = []
    for example in examples:
        html_tables += [pivot_table(example[0], example[1], example[2], example[3])]
    output_file = ASSN.replace(" ", "") + "-pivot-tables.html"
    title = "Pivot Tables for select examples"
    ou.write_html_file_new(output_file, title, html_tables, True, None, True)
    comments, queries = as5.read_queries("Analytics.sql")
    as5.process_queries(comments, queries, DB, ASSN+"a")


if __name__ == "__main__":
    main()