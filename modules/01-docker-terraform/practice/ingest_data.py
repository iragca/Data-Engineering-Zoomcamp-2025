#!/usr/bin/env python
# coding: utf-8
import os
import argparse
import time
import pandas as pd
from sqlalchemy import create_engine


def main(params):
    user = params.user
    password = params.password
    host = params.host
    port = params.port
    db = params.db
    table_name = params.table_name
    url = params.url

    csv_name = "output.parquet"

    os.system(f"wget {url} -O {csv_name}")

    engine = create_engine(f"postgresql://{user}:{password}@{host}:{port}/{db}")
    df = pd.read_parquet(csv_name)

    engine.connect()
    print(f"Connected to Postgres DB: {db}")
    print(f"Writing data to {table_name} table")

    start_time = time.time()
    df.to_sql(table_name, con=engine, if_exists="replace", index=False)
    end_time = time.time()

    elapsed_time = end_time - start_time
    print(f"Data ingestion took {elapsed_time:.2f} seconds")
    print("Data written successfully")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Ingest CSV data into Postgres")

    parser.add_argument("--user", type=str, help="Postgres user", required=True)
    parser.add_argument("--password", type=str, help="Postgres password", required=True)
    parser.add_argument("--host", type=str, help="Postgres host", required=True)
    parser.add_argument("--port", type=str, help="Postgres port", required=True)
    parser.add_argument("--db", type=str, help="Postgres database", required=True)
    parser.add_argument(
        "--table_name", type=str, help="Postgres table name", required=True
    )
    parser.add_argument("--url", type=str, help="URL to the data", required=True)

    args = parser.parse_args()

    main(args)
