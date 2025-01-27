# Question 1

The Dockerfile in this repo prints out the pip version when building and running
```bash
docker build -t q1
docker run -it q1
```

# Question 2

> Answer: db:5432

The `db:` in the docker-compose file implicitly names this service's hostname. Since they are on the same network, there is no need to use the host mapping to connect to the socket of the service, so it is `5432`.




# Questions 3 - 5

## Setup 

```bash
docker compose up
python load_data.py
```

> [!NOTE] 
> Answers are also found within in this directory (using polars), the jupyter notebook named `eda.ipynb`.

## Question 3

```sql
SELECT 
    SUM(CASE 
        WHEN trip_distance <= 1 THEN 1 
        ELSE 0 
    END) AS trips_up_to_1_mile,
    SUM(CASE 
        WHEN trip_distance > 1 AND trip_distance <= 3 THEN 1 
        ELSE 0 
    END) AS trips_between_1_and_3_miles,
    SUM(CASE 
        WHEN trip_distance > 3 AND trip_distance <= 7 THEN 1 
        ELSE 0 
    END) AS trips_between_3_and_7_miles,
    SUM(CASE 
        WHEN trip_distance > 7 AND trip_distance <= 10 THEN 1 
        ELSE 0 
    END) AS trips_between_7_and_10_miles,
    SUM(CASE 
        WHEN trip_distance > 10 THEN 1 
        ELSE 0 
    END) AS trips_over_10_miles
FROM 
    green
WHERE 
    lpep_pickup_datetime >= '2019-10-01' 
    AND lpep_dropoff_datetime < '2019-11-01';
```

## Question 4

```sql
SELECT 
    trip_distance,
    lpep_pickup_datetime
FROM
    green
ORDER BY
    trip_distance DESC
```

## Question 5

```sql
SELECT 
    z."Zone", 
    SUM(g.total_amount) AS total_amount
FROM 
    green g 
JOIN 
    "zone" z 
ON 
    g."PULocationID" = z."LocationID"
WHERE 
    g.lpep_pickup_datetime >= '2019-10-18' 
    AND g.lpep_pickup_datetime < '2019-10-19'
GROUP BY 
    z."Zone"
ORDER BY 
    total_amount DESC
LIMIT 3;
```

## Question 6

```sql
SELECT 
    z."Zone", 
    MAX(tip_amount) AS tip_amount
FROM 
    green g 
JOIN 
    "zone" z 
ON 
    g."DOLocationID" = z."LocationID"
WHERE 
    g.lpep_pickup_datetime >= '2019-10-18' 
    AND g.lpep_pickup_datetime < '2019-10-19'
	AND z."Zone" = 'East Harlem North'
GROUP BY 
    z."Zone"
ORDER BY 
    tip_amount DESC
```
