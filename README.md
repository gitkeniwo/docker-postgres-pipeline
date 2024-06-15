# Answers
# Q1 

`docker run --rm`: Automatically remove the container when it exits

# Q2

`docker run -it --entrypoint=bash python:3.9`

version of `wheel`: 0.43.0

# Q3

Todo: 
- [x] Implement Commandline args parsing for the py script

```ps
root@localhost:ny_taxi_hw1> SELECT COUNT(*)
 FROM green_tripdata
 WHERE lpep_dropoff_datetime >= '2019-09-18 00:00:00'
     AND lpep_dropoff_datetime <= '2019-09-18 23:59:59'
     AND lpep_pickup_datetime >= '2019-09-18 00:00:00'
     AND lpep_pickup_datetime <= '2019-09-18 23:59:59';
+-------+
| count |
|-------|
| 15612 |
+-------+
SELECT 1
Time: 0.045s
```

# Q4

```ps
root@localhost:ny_taxi_hw1> SELECT lpep_pickup_datetime FROM green_tripdata
 WHERE trip_distance = (SELECT MAX(trip_distance) FROM green_tripdata);
+----------------------+
| lpep_pickup_datetime |
|----------------------|
| 2019-09-26 19:32:52  |
+----------------------+
SELECT 1
Time: 0.078s
```

# Q5 

```ps
root@localhost:ny_taxi_hw1> SELECT count(
     case when lpep_pickup_datetime >= '2019-09-18 00:00:00'
         and lpep_pickup_datetime <= '2019-09-18 23:59:59'
         then 1 end
 ) as count, borough
 FROM (
     SELECT g.lpep_pickup_datetime, t."Borough" as borough
     FROM green_tripdata as g
         LEFT JOIN taxi_zone as t
         ON g."PULocationID" = t."LocationID") AS joined
 GROUP BY borough
 ORDER BY count DESC
 ;
+-------+---------------+
| count | borough       |
|-------+---------------|
| 5575  | Manhattan     |
| 4458  | Brooklyn      |
| 4393  | Queens        |
| 1308  | Bronx         |
| 24    | Unknown       |
| 9     | Staten Island |
| 0     | EWR           |
+-------+---------------+
SELECT 7
Time: 0.100s
```


# Q6
```sql
SELECT t."Zone"
FROM green_tripdata as g
    LEFT JOIN taxi_zone as t 
    ON g."DOLocationID" = t."LocationID"
WHERE tip_amount = (
    SELECT MAX(tip_amount)
    FROM green_tripdata
    WHERE "PULocationID" = (
        SELECT "LocationID"
        FROM taxi_zone
        WHERE "Zone" = 'Astoria'
    )
)
;

+-------------+
| Zone        |
|-------------|
| JFK Airport |
+-------------+
SELECT 1
Time: 0.076s
```

