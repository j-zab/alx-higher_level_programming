-- lists all California'n cities that can be found in the database hbtn_0d_usa
-- lists all rows of a column in the database
SELECT id, name FROM cities WHERE state_id = (SELECT id FROM states WHERE name = 'California') ORDER BY id ASC;
