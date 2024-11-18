-- Create a table to store the CSV data
CREATE TABLE dadesAigues (
    id VARCHAR(100),
    tecnologia VARCHAR(100),
    uso VARCHAR(100),
    Tvivienda VARCHAR(100),
    diameter VARCHAR(100),
    date DATETIME,
    `index` INT
);

-- Load data from CSV file into the table
-- Make sure to replace 'path/to/your/file.csv' with the actual path to your CSV file
-- This example assumes you are using MySQL
LOAD DATA INFILE '/home/aina/UPC/CBI/CBI_Code/files/dades_dataChallenge.csv'
INTO TABLE dadesAigues
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(id, tecnologia, uso, Tvivienda, diameter, @date, `index`)
SET date = STR_TO_DATE(@date, '%d/%m/%Y %H:%i');