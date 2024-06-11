#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from sqlalchemy import create_engine
import argparse

def main(args):
    # In[4]:

    # db connection

    # USERNAME = 'root'
    # PW = 'root'
    # # HOST = 'localhost'
    # HOST = 'db'
    # PORT = '5432'
    # DBNAME = 'ny_taxi_hw1'
    
    username = args.username
    pw = args.password
    hostname = args.hostname
    port = args.port
    dbname = args.dbname

    engine = create_engine(f'postgresql://{username}:{pw}@{hostname}:{port}/{dbname}')


    # In[92]:

    connection = engine.connect()

    # Gotta import the whole dataset into the db by iteration
    # 
    # !!! Notice how to create a iter df by assigning `iterator` and `chunksize` params.


    # In[11]:


    # create iter df
    green_tripdata_iter = pd.read_csv("green_tripdata_2019-09.csv", iterator=True, chunksize=10000)
    taxi_zone = pd.read_csv("taxi+_zone_lookup.csv")

    from time import time
    import logging

    logging.basicConfig(
        filename='./data/data-ingestion.log', 
        filemode='w',  # Set filemode to 'w' for write mode (overwrite)
        level=logging.INFO, 
        format='%(asctime)s - %(message)s', # timestamp of the log message + message body
        datefmt='%H:%M:%S',
    )

    logging.info('Start logging...')

    for i, iter in enumerate(green_tripdata_iter):
        action = 'append' if i else 'replace'

        date_columns = ['lpep_pickup_datetime', 'lpep_dropoff_datetime']
        iter[date_columns] = iter[date_columns].apply(pd.to_datetime)
        
        start_time = time()
        iter.to_sql(name='green_tripdata', con=engine, if_exists=action)
        end_time = time()
        time_span = end_time - start_time
        
        logging.info(f'Done with the chunk {i}. Took {time_span} seconds.')
        print(f'Done with the chunk {i}. Took {time_span} seconds.')
        
    taxi_zone.to_sql(name='taxi_zone', con=engine, if_exists='replace')
    logging.info(f'Done with the taxi_zone data.')
    print(f'Done with the taxi_zone data.')



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = 'Connect to Postgres and import your data.')
    
    parser.add_argument('--username', '-u', 
                        help= 'Username')
    parser.add_argument('--password', '-P',
                        help= 'Password')
    parser.add_argument('--hostname', '-H',
                        help= 'Hostname')
    parser.add_argument('--port', '-p',
                        help= 'Port number')
    parser.add_argument('--dbname', '-d',
                        help= 'Name of the database that you would like to connect to.')
    
    args = parser.parse_args()
    
    main(args)