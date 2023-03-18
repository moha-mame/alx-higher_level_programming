-- List all records of 'second_table' of db 'hbtn_0c_0'
-- Results should display score and name
-- Records should be listed descending score
SELECT score, name
FROM second_table
HAVING name IS NOT NULL
ORDER BY score DESC;
