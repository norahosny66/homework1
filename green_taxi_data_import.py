
import pandas as pd
from sqlalchemy import create_engine
import os
import gzip

# Function to download and extract CSV files
def download_and_extract(url, filename):
    # Download the file
    os.system(f"wget {url}")
    
    # Extract if it's a gzip file
    if filename.endswith(".gz"):
        with gzip.open(filename, 'rb') as f_in:
            with open(filename[:-3], 'wb') as f_out:
                f_out.write(f_in.read())
        os.remove(filename)
        filename = filename[:-3]
    
    return filename

# URLs and filenames
green_taxi_url = "https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2019-09.csv.gz"
green_taxi_filename = "green_tripdata_2019-09.csv.gz"
zones_url = "https://s3.amazonaws.com/nyc-tlc/misc/taxi+_zone_lookup.csv"
zones_filename = "taxi+_zone_lookup.csv"

# Download and extract files
green_taxi_filename = download_and_extract(green_taxi_url, green_taxi_filename)
zones_filename = download_and_extract(zones_url, zones_filename)

# Create the database engine (replace with your own credentials)
# Format: 'postgresql://username:password@host:port/database'
engine = create_engine('postgresql://postgres:noura@localhost:5432/mydatabase')

# Load the datasets
green_taxi_df = pd.read_csv(green_taxi_filename)
zones_df = pd.read_csv(zones_filename)

# Import the data into PostgreSQL
green_taxi_df.to_sql('green_taxi_trips', engine, if_exists='append', index=False)
zones_df.to_sql('taxi_zone_lookup', engine, if_exists='append', index=False)

# Clean up by removing the CSV files
os.remove(green_taxi_filename)
os.remove(zones_filename)

print("Data import complete!")
