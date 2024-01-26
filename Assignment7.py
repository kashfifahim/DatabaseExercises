# Winter 2024
# Assignment 7 - Stored Procedures and Functions
# Kashfi Fahim

import Assignment5 as as5
import Assignment3 as as3


def main():
    assignment = "Assignment 7"
    comments, queries = as5.read_queries("Assignment7.sql")
    as5.process_queries(comments, queries, "udb", assignment)

    assignment = "Assignment 7 Analytics"
    comments, queries = as5.read_queries("Analytics.sql")
    as5.process_queries(comments, queries, "udb", assignment)


if __name__ == "__main__":
    main()