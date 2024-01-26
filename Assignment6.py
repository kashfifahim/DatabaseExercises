# Winter 2024
# Assignment 6 - DDL and DML Practice
# Kashfi Fahim
import Assignment5 as as5


def main():
    assignment = "Assignment 6"
    comments, queries = as5.read_queries("assignment6.sql")
    as5.process_queries(comments, queries, "udb", assignment)

    assignment = "Assignment 6 Analytics"
    comments, queries = as5.read_queries("Analytics.sql")
    as5.process_queries(comments, queries, "udb", assignment)


if __name__ == "__main__":
    main()