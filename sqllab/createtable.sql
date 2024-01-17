DROP TABLE IF EXISTS earthquakes;
CREATE TABLE earthquakes (
  quaketime timestamp with time zone,
  latitude real,
  longitude real,
  quakedepth real,
  mag real,
  magtype text,
  id text,
  updated timestamp with time zone,
  place text,
  status text
);
