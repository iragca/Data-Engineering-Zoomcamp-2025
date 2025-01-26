FROM python:3.9

WORKDIR /app
COPY pipeline.py pipeline.py

RUN apt-get install wget
RUN pip install pandas sqlalchemy psycopg2 pyarrow

ENTRYPOINT [ "python", "pipeline.py" ]