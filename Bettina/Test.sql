#Load the Schema, replace with your named schema
use CDC_baby;

#needed for loading
SHOW GLOBAL VARIABLES LIKE 'local_infile';

ALTER TABLE CSV2018test MODIFY DMAR TEXT;

#after import wizarding the head file, view to see it's all there.
SELECT * FROM CSV2018test;

DROP TABLE IF EXISTS cdc_2018;

#Create a new table like CSV2018head
CREATE TABLE cdc_2018 LIKE CSV2018test;
#AS (SELECT *
#    FROM csv2018head);
    
#double check cdc_2018, just header
SELECT *
FROM cdc_2018;

#empty new table to avoid duplicates on loading
#TRUNCATE cdc_2018;

#double check that it is indeed empty
#SELECT * FROM cdc_2018;

#Import full dataset into the table
LOAD DATA LOCAL INFILE '/private/tmp/CSV2018test.csv' IGNORE
INTO TABLE cdc_2018
FIELDS TERMINATED BY ',' ENCLOSED BY '"'
#ESCAPED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

SELECT *
FROM cdc_2018;


