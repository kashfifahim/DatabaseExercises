/* Drop Index on query table */
ALTER TABLE query DROP INDEX idx_query_assignment;

/* Select all queries using IN clause without index*/
Select count(*) as count from query where query_assn in
('Assignment3', 'Assignment4', 'Assignment5',
'Assignment6', 'Assignment7', 'Assignment8',
'Assignment9', 'Assignment10', 'Assignment11');

/* Select all queries using OR clause without index */
Select count(*) as count from query where
query_assn = 'Assignment3' or
query_assn = 'Assignment4' or
query_assn = 'Assignment5' or
query_assn = 'Assignment6' or
query_assn = 'Assignment7' or
query_assn = 'Assignment8' or
query_assn = 'Assignment9' or
query_assn = 'Assignment10' or
query_assn = 'Assignment11';

/* Select all queries using LIKE clause without index */
Select count(*) as count from query where query_assn like 'Assignment %';

/* Select all queries using UNION clause without index */
Select sum(c) from
(Select count(*) as c from query where query_assn = 'Assignment3'
union
Select count(*) as c from query where query_assn = 'Assignment4'
union
Select count(*) as c from query where query_assn = 'Assignment5'
union
Select count(*) as c from query where query_assn = 'Assignment6'
union
Select count(*) as c from query where query_assn = 'Assignment7'
union
Select count(*) as c from query where query_assn = 'Assignment8'
union
Select count(*) as c from query where query_assn = 'Assignment9'
union
Select count(*) as c from query where query_assn = 'Assignment10'
union
Select count(*)  as c from query where query_assn = 'Assignment11')
as count;

/* Create Index on query table*/
CREATE INDEX idx_query_assignment ON query (query_assn);

/* Select all queries using IN clause with index */
Select count(*) as count from query where query_assn in
('Assignment3', 'Assignment4', 'Assignment5',
'Assignment6', 'Assignment7', 'Assignment8',
'Assignment9', 'Assignment10', 'Assignment11');

/* Select all queries using OR clause with index */
Select count(*) as count from query where
query_assn = 'Assignment3' or
query_assn = 'Assignment4' or
query_assn = 'Assignment5' or
query_assn = 'Assignment6' or
query_assn = 'Assignment7' or
query_assn = 'Assignment8' or
query_assn = 'Assignment9' or
query_assn = 'Assignment10' or
query_assn = 'Assignment11';

/* Select all queries using LIKE clause with index */
Select count(*) as count from query where query_assn like 'Assignment %';

/* Select all queries using UNION clause with index */
Select sum(c) from
(Select count(*) as c from query where query_assn = 'Assignment3'
union
Select count(*) as c from query where query_assn = 'Assignment4'
union
Select count(*) as c from query where query_assn = 'Assignment5'
union
Select count(*) as c from query where query_assn = 'Assignment6'
union
Select count(*) as c from query where query_assn = 'Assignment7'
union
Select count(*) as c from query where query_assn = 'Assignment8'
union
Select count(*) as c from query where query_assn = 'Assignment9'
union
Select count(*) as c from query where query_assn = 'Assignment10'
union
Select count(*)  as c from query where query_assn = 'Assignment11')
as count;


/* Find queries associated with this assignment */
Select query_id, query_desc, query_dur from query where query_assn = 'Assignment12' order by query_ended desc limit 10;