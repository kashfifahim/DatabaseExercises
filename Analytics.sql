/* Summary of tables and columns */
SELECT table_name, count(column_name) as columns
FROM v_udb_table_columns
GROUP BY table_name;

/* Detail of tables and columns */
SELECT *
from v_udb_table_columns
order by TABLE_NAME, COLUMN_NUM;

/* List of databases, tables, columns, and data types */
SELECT * from v_udb_columns;

/* Summary of queries */
SELECT assignment, COUNT(*), MIN(query_dur) AS Min_Dur, AVG(query_dur) AS Avg_Dur, MAX(query_dur) AS Max_Dur, SUM(query_dur) AS Total_Dur
FROM query
GROUP BY query_assn
ORDER BY query_assn;

/* Retrieve queries for Assignment 3 */
SELECT * FROM query where upper(query_assn) in ('Assignment 3', "Assignment3") ORDER BY query_ended LIMIT 200;

/* Retrieve queries for Assignment 4 */
SELECT * FROM query where upper(query_assn) in ('ASSIGNMENT 4', "ASSIGNMENT") ORDER BY query_ended LIMIT 200;

/* Retrieve queries for Assignment 5 */
SELECT * FROM query where upper(query_assn) in ('ASSIGNMENT 5', "ASSIGNMENT5") ORDER BY query_ended LIMIT 200;

/* Retrieve queries for Assignment 6 */
SELECT * FROM query where upper(query_assn) in ('ASSIGNMENT 6', "ASSIGNMENT6") ORDER BY query_ended LIMIT 200;

/* Retrieve queries for Assignment 7 */
SELECT * FROM query where upper(query_assn) in ('ASSIGNMENT 7', "ASSIGNMENT7") ORDER BY query_ended LIMIT 200;

/* Retrieve queries for Assignment 8 */
SELECT * FROM query where upper(query_assn) in ('ASSIGNMENT 8', "ASSIGNMENT8") ORDER BY query_ended LIMIT 200;

/* Retrieve queries for Assignment 9 */
SELECT * FROM query where upper(query_assn) in ('ASSIGNMENT 9', "ASSIGNMENT9") ORDER BY query_ended LIMIT 200;

/* Retrieve queries for Assignment 10 */
SELECT * FROM query where upper(query_assn) in ('ASSIGNMENT 10', "ASSIGNMENT10") ORDER BY query_ended LIMIT 200;

/* Retrieve queries for Assignment 10 */
SELECT * FROM query where upper(query_assn) in ('ASSIGNMENT 11', "ASSIGNMENT11") ORDER BY query_ended LIMIT 200;