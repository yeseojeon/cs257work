-- Which earthquakes had a magnitude greater than 4 mb?
-- (involves 2 queries: Which earthquakes had a mag greater than 4, 
-- and which earthquakes had a magType of mb.)
SELECT * FROM earthquakes WHERE mag > 4
INTERSECT
SELECT * FROM earthquakes WHERE magType = 'mb';

-- Which earthquakes were at a negative longitude?
SELECT * FROM earthquakes WHERE longitude < 0;

-- Which earthquakes had a quakedepth of between 10 and 50?
SELECT * FROM earthquakes WHERE quakedepth BETWEEN 10 AND 50;