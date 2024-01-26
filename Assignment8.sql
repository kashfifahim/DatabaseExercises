drop table if exists backup;
/* [1] Create a new table "backup" with the following columns and datatypes */
CREATE TABLE backup (
    backup_id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    relation VARCHAR(30) NOT NULL,
    num_rows INT NOT NULL,
    num_cols INT NOT NULL,
    csv_length INT NOT NULL,
    xml_length INT NOT NULL,
    json_length INT NOT NULL,
    csv_data LONGTEXT,
    xml_data LONGTEXT,
    json_data JSON,
    dtm DATETIME DEFAULT CURRENT_TIMESTAMP
);

/* [7] Create a view v_table_backups that has a list of backups without the actual csv_data, xml_data, and json_data */
CREATE OR REPLACE VIEW v_table_backup AS
SELECT backup_id, relation as table_name, num_rows, num_cols, csv_length, xml_length, json_length, dtm as data_saved
from backup
ORDER BY relation, dtm;

/* [7] Retrieve from the view */
SELECT * from v_table_backup