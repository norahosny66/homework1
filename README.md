# homework1
# q3:
SELECT COUNT(*)
FROM green_taxi_trips gtt 
WHERE DATE(CAST(lpep_pickup_datetime)) = '2019-09-18' 
AND DATE(CAST(lpep_dropoff_datetime)) = '2019-09-18' ;
# q4:
SELECT DATE(CAST(lpep_pickup_datetime AS TIMESTAMP)) AS pickup_day, MAX(CAST(trip_distance AS NUMERIC)) AS longest_distance
FROM green_taxi_trips
WHERE DATE(CAST(lpep_pickup_datetime AS TIMESTAMP)) IN ('2019-09-18', '2019-09-16', '2019-09-26', '2019-09-21')
GROUP BY DATE(CAST(lpep_pickup_datetime AS TIMESTAMP))
ORDER BY pickup_day;
# q5:
SELECT tzl.Borough, COUNT(*) AS pickup_count
FROM green_taxi_trips gtt
JOIN taxi_zone_lookup tzl ON gtt."PULocationID" = tzl."LocationID
GROUP BY tzl.Borough
ORDER BY pickup_count DESC
LIMIT 3;
# q6:
SELECT tzl."Zone", gtt.tip_amount
FROM green_taxi_trips gtt
JOIN taxi_zone_lookup tzl ON gtt."PULocationID" = tzl."LocationID"
ORDER BY gtt.tip_amount DESC
LIMIT 1;
