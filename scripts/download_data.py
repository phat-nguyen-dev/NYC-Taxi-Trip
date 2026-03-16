import io
from io import BytesIO

import pandas as pd
import requests

response = requests.get('https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2025-11.parquet')
byteio = BytesIO(response.content)
df = pd.read_parquet(byteio)
print(df.head())
