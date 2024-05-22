-- Lists all items of the table second_table having a name value in my MySQL server.
-- Records are arraned in  descending score.
SELECT `score`, `name`
FROM `second_table`
WHERE `name` != ""
ORDER BY `score` DESC
