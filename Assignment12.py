# Winter 2024
# Assignment 12 - Database Record Storage
# Kashfi Fahim
# Collaborated with class

import DBUtil as dbu


def main():
    assn = "Assignment12"
    db = 'udb'

    comments, queries = dbu.read_queries(f"{assn}.sql")
    dbu.process_queries(comments, queries, db, assn)

    comments, queries = dbu.read_queries("Analytics.sql")
    dbu.process_queries(comments, queries, db, f"{assn}-A")


if __name__ == "__main__":
    main()