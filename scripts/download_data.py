import io
from io import BytesIO
import time

import pandas as pd
import requests

base_url = 'https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2025'
month = 11

def write_file(requests, file_path):
    try:
        with open(file_path, 'wb') as f:
            for chunk in requests.iter_content(chunk_size=1024*1024):
                f.write(chunk)

    except Exception as e:
        print(f"Error: {e}")
    
    time.sleep(5)


if __name__ == "__main__":
    for m in range(1, month+1):
        url = f'{base_url}-{m:02d}.parquet'
        file_path = f'data/raw/yellow/yellow_taxi_2025-{m:02d}.parquet'

        response = requests.get(url, stream=True)
        write_file(response, file_path)
