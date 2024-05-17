import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# 본 파이썬 코드는 get_weather_data_by_api.py로 데이터를 모은 후 실행되어야 하는 코드입니다.

# highway_nearest_ws.csv는 ic별 가장 가까운 기상 관측소와 join된 데이터로 
# houly_highway_weather_data_processing.ipynb에서 한번 만들어져서 바뀌지 않음.
highway_nearest_ws = pd.read_csv("./highway_nearest_ws.csv")
weather = pd.read_csv("./weather_data_20240101_20240514_full.csv")

hourly_highway_weather = pd.merge(highway_nearest_ws, weather, 
                                  left_on='weather_station_id', right_on='id')\
                            .drop(columns = ['location', 'id'])

hourly_highway_weather.to_csv("./hourly_highway_weather.csv", index = False)