-- List all magnitues for earthquakes with an epicenter deeper than 50 kilometers 
SELECT mag FROM earthquakes WHERE quakedepth > 50;

-- Find all the places that have had earthquakes above matnitude 5 where the epicenter was more than 100 kilometers deep
SELECT place FROM earthquakes WHERE quakedepth > 100 INTERSECT SELECT place FROM earthquakes WHERE mag > 5;

-- Find the quaketime, magnitude, and place for all earthquakes in the United States
SELECT quaketime,mag,place FROM earthquakes WHERE latitude BETWEEN 24.9 AND 49.6 AND longitude BETWEEN -125 AND -66.9;
