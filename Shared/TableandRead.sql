#Load the Schema, replace with your named schema
use CDC;

#needed for loading
SHOW GLOBAL VARIABLES LIKE 'local_infile';

#after import wizarding the head file, view to see it's all there.
SELECT * FROM csv2018headnew;

#Create cdchead as a copy of the table
CREATE TABLE cdchead
AS (SELECT *
    FROM csv2018headnew);
    
#double check number of columns (230)
SELECT count(*)
FROM cdchead;

#empty new table to avoid duplicates on loading
TRUNCATE cdchead;

#double check that it is indeed empty
SELECT * FROM cdchead;

#Import full dataset into the table
LOAD DATA LOCAL INFILE '/private/tmp/CSV2018.csv' IGNORE
INTO TABLE cdchead
FIELDS TERMINATED BY ',' ENCLOSED BY '"'
ESCAPED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 LINES ;