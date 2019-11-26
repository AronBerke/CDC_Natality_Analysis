#Load the Schema, replace with your named schema
use CDC;

#needed for loading
SHOW GLOBAL VARIABLES LIKE 'local_infile';

#after import wizarding the head file, view to see it's all there.
SELECT * FROM csv2018head;

#Create cdchead as a copy of the table
CREATE TABLE cdchead
AS (SELECT *
    FROM csv2018head);
    
#double check number of columns (230)
SELECT count(*)
FROM information_schema.columns
WHERE table_name = 'cdchead';

#empty new table to avoid duplicates on loading
TRUNCATE cdchead;

#double check that it is indeed empty
SELECT * FROM cdchead;

#Import full dataset into the table
LOAD DATA LOCAL INFILE '/private/tmp/CSV2018.csv'
INTO TABLE cdchead
FIELDS TERMINATED BY ',' ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 0 LINES ;