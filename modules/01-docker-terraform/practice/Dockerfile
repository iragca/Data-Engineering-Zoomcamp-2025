FROM python:3.9

RUN pip install pandas

WORKDIR /app
COPY pipeline.py /scripts/pipeline.py

ENTRYPOINT [ "python", "/scripts/pipeline.py" ]