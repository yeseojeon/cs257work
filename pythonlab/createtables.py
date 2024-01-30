DROP TABLE IF EXISTS states;
CREATE TABLE states (
  state text,
  abbreviation text
);

DROP TABLE IF EXISTS us cities;
CREATE TABLE us cities (
  city text,
  state text,
  population int,
  lat real,
  lon real
);
