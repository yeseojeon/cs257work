DROP TABLE IF EXISTS earthquakes;
CREATE TABLE earthquakes (
  quaketime time with time zone,
  latitude real,
  longitude real,
  quakedepth real,
  mag real,
  magType text,
  place text,
  horizontalError real,
  depthError real,
  magError real,
  magNst smallint
);