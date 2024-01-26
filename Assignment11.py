# Winter 2024
# Assignment 11 - Database Record Storage
# Kashfi Fahim
# Collaborated with class

import Assignment5 as as5


def main():
    assn = "Assignment11"
    db = 'udb'

    comments, queries = as5.read_queries(f"{assn}.sql")
    as5.process_queries(comments, queries, db, assn + "F", "F")
    as5.process_queries(comments, queries, db, assn + "V", "V")

    comments, queries = as5.read_queries("Analytics.sql")
    as5.process_queries(comments, queries, db, f"{assn}-A")


if __name__ == "__main__":
    main()