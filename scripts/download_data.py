import io
from io import BytesIO
import os
import time

import pandas as pd
import requests

from common.logger import write_log

base_url = 'https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2025'
month = 11

def write_file(response, url, file_path):
    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        response.raise_for_status()
    
        with open(file_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=1024*1024):
                f.write(chunk)
        write_log(message=f'Download data from {url} success, adding to {file_path}')

    except Exception as e:
        write_log(message=f"Error while download {file_path}: {e}")
        raise
    
    time.sleep(0.5)


if __name__ == "__main__":
    for m in range(1, month+1):
        url = f'{base_url}-{m:02d}.parquet'
        file_path = f'data/raw/yellow/yellow_taxi_2025-{m:02d}.parquet'

        response = requests.get(url, stream=True, timeout=10)
        write_file(response, url, file_path)
