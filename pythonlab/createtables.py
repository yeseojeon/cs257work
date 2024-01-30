DROP TABLE IF EXISTS states;
CREATE TABLE states (
  state text,
  abbreviation text
);

DROP TABLE IF EXISTS us_cities;
CREATE TABLE us_cities (
  city text,
  state text,
  population int,
  lat real,
  lon real
);
