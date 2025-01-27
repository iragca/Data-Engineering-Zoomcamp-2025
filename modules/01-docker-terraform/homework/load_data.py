import polars as pl
from sqlalchemy import create_engine

green = pl.read_csv("green_tripdata_2019-10.csv", try_parse_dates=True)
zone = pl.read_csv("taxi_zone_lookup.csv")

# DB connection
engine = create_engine("postgresql://postgres:postgres@localhost:5433/ny_taxi")

# Insert the DataFrame into PostgreSQL table
print("Inserting data into PostgreSQL...")
green.to_pandas().to_sql("green", engine, if_exists="replace", index=False)
zone.to_pandas().to_sql("zone", engine, if_exists="replace", index=False)
print("Data inserted successfully!")
