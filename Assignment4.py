# Winter 2024
# Assignment 4 - Query Runner, Tracker, and Visualizer
# Kashfi Fahim
# Collaborated with class

import Assignment3 as as3
import OutputUtil as ou


def process_queries(file_name, db, assignment):
    with open(file_name, 'r') as file:
        text = file.read()
        queries = text.strip().split(";")
        tables = []
        for i, query in enumerate(queries):
            if '*/' in query:
                comment, sql = query.split("*/")
                comment = comment.replace("/*", '').strip()
                sql = sql.strip()
                if sql:  # Check if the SQL query is not empty
                    headers, data = as3.run_query(sql, comment, db, assignment)
                    alignments = ["l"] * len(headers)
                    types = ["S"] * len(headers)
                    table = [comment, headers, types, alignments, data]
                    tables.append(table)
                else:
                    print(f"Empty SQL query at index {i}: {comment}")
        output_file = assignment.replace(" ", "") + ".html"
        title = "All queries for " + assignment + " in " + file_name
        ou.write_html_file_new(output_file, title, tables, open_file=True, style_sheet=None, do_toc=True)


def retrieve_query_log(assignments, db):
    query_log = []
    for assignment in assignments:
        sql = f"select * from query where query_assn = '{assignment}'"
        desc = f"retrieve all queries executed for {assignment}"
        headers, data = as3.run_query(sql, desc, db, assignments[-1])
        alignments = ["l"] * len(headers)
        types = ["S"] * len(headers)
        query = [desc, headers, types, alignments, data]
        query_log.append(query)
    output_file = assignment.replace(" ", "") + "-query-history.html"
    title = "All queries for assignment to date"
    ou.write_html_file_new(output_file, title, query_log, True, None, None)

def main():
    assignment = "Assignment 4"
    process_queries("assignment4.sql", "udb", assignment)
    assignments = [f"Assignment {i}" for i in range(3, 5)]
    retrieve_query_log(assignments, "udb")

if __name__ == "__main__":
    main()