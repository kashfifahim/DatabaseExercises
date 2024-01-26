/* Assignment 5 In-class View of all tables and columns in udb database */
CREATE OR REPLACE VIEW v_udb_table_columns AS
SELECT table_name, ordinal_position as COLUMN_NUM, COLUMN_NAME, DATA_TYPE, coalesce(CHARACTER_MAXIMUM_LENGTH, NUMERIC_PRECISION) as LENGTH, is_nullable as NULLABLE
FROM information_schema.columns
WHERE table_schema = 'udb'
ORDER BY table_name, ordinal_position;

/* Select everything from the new view: v_udb_table_columns */
SELECT *
from v_udb_table_columns
order by TABLE_NAME, COLUMN_NUM;

/* Aggregation technique: Retrieve number of columns per table */
SELECT table_name, count(column_name) as columns
FROM v_udb_table_columns
GROUP BY table_name;