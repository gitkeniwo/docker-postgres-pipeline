docker build --tag hw1:v1 .

#  -it is for interactive
# --rm = delete after it stops
docker run --rm -it --name homework1 \
            --network hw1_pgnetwork \
            -v ./container_volume/:/app/data \
            hw1:q3 \
            -u root \
            -P root \
            -H db \
            -p 5432 \
            -d ny_taxi_hw1

wget https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2019-09.csv.gz
wget https://s3.amazonaws.com/nyc-tlc/misc/taxi+_zone_lookup.csv
gunzip green_tripdata_2019-09.csv.gz


!jupyter nbconvert --to script upload-data.ipynb