-- Task 1: Examine the three tables
SELECT * 
FROM trips;

SELECT * 
FROM riders;

SELECT * 
FROM cars;

-- Task 2: The primary key for each table
-- The primary key of trips is id
-- The primary key of riders is id
-- The primary key of cars is id

-- Task 3: Cross join between riders and cars (Creates a Cartesian product; not very useful here)
SELECT 
  riders.first,
  riders.last,
  cars.model
FROM riders
JOIN cars ON 1=1;

-- Task 4: Left join trips and riders
SELECT 
  trips.*,
  riders.first,
  riders.last
FROM trips
LEFT JOIN riders
  ON trips.rider_id = riders.id;

-- Task 5: Inner join trips and cars
SELECT 
  trips.id,
  trips.date,
  trips.cost,
  cars.model
FROM trips
JOIN cars
  ON trips.car_id = cars.id;

-- Task 6: Stack table riders and table riders2
SELECT *
FROM riders

UNION 

SELECT *
FROM riders2;

-- Task 7: Find the average cost for a trip
SELECT 
    ROUND(
        AVG(cost), 
        2
    ) AS average_trip_cost
FROM trips;

-- Task 8: Find all the riders who have used Lyft less than 500 times
WITH all_riders AS (
  SELECT * 
  FROM riders

  UNION

  SELECT * 
  FROM riders2
)
SELECT *
FROM all_riders
WHERE total_trips < 500;

-- Task 9: Calculate the number of cars that are active
SELECT 
  COUNT(*) AS active_cars
FROM cars
WHERE status = 'active';

-- Task 10: Find two cars that have the highest trips_completed
SELECT 
    id,
    model,
    trips_completed
FROM cars
ORDER BY trips_completed DESC
LIMIT 2;
