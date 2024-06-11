FROM python:3.9

WORKDIR /app 
# set up workdir

COPY data-ingesting.py requirements.txt /app/

RUN pip install psycopg2
RUN pip install -r requirements.txt
RUN mkdir data

# add will automatically unzip
ADD https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2019-09.csv.gz .
ADD https://s3.amazonaws.com/nyc-tlc/misc/taxi+_zone_lookup.csv .
RUN gunzip green_tripdata_2019-09.csv.gz

VOLUME [ "/app/data" ]

ENTRYPOINT [ "python", "data-ingesting.py" ] 
# ENTRYPOINT [ "bash" ]