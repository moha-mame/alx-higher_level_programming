-- Create a table called 'first_table'
-- 'first_table' should have (id INT) and (name VARCHAR(256))
-- db name will be passed as argument of mysql command
-- If table 'first_table' already exists, should not fail.
CREATE TABLE IF NOT EXISTS first_table (id INT, name VARCHAR(256));
