-- lists all the cities of California that can be found in the database hbtn_0d_usa
-- where name = California 

SELECT id, name FROM cities WHERE state_id = (SELECT id FROM states WHERE name = "California");
