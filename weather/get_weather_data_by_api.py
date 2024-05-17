import requests
from datetime import datetime, timedelta
import time
from tqdm import tqdm
import numpy as np
import pandas as pd
with open("./aws_access_keys.txt", 'r') as f:
    keys = f.readlines()
    access_key = keys[0][:-1]
    secret_key = keys[1][:-1]
    
ws_info_df = pd.read_csv("./weather_station_long_lat.csv").loc[:, ["weather_station_id", "weather_station_name"]]

def str_to_float_for_weather_data(x):
    if x == '':
        return 0.0
    else:
        return np.float32(x)
def str_to_int_for_weather_data(x):
    if x == '':
        return 0
    else:
        return np.int32(x)

# API 키 불러오기
with open("./weather_api.txt", 'r') as f:
    api_key = f.readline().strip()
    
observer_results_dict = {}
start_date = datetime(2024,5,16).date()
today = datetime.now().date()
tq = tqdm(ws_info_df.values)
cnt = 1
for observer_code, observer_key in tq:
    now_date = start_date
    observer_results_dict[observer_code] = []
    while now_date < today:
        date_str = now_date.strftime("%Y%m%d")
        try:
            query_str = f"http://apis.data.go.kr/1360000/AsosHourlyInfoService/getWthrDataList?serviceKey={api_key}&numOfRows=24&pageNo=1&dataType=JSON&dataCd=ASOS&dateCd=HR&stnIds={observer_code}&endDt={date_str}&endHh=23&startHh=00&startDt={date_str}"
            res = requests.get(query_str)
            result_items = res.json()['response']['body']['items']['item']
            
            for item in result_items:
                tm = datetime.strptime(item['tm'], '%Y-%m-%d %H:%M')
                rn = str_to_float_for_weather_data(item['rn']) # 강수량
                dsnw = str_to_float_for_weather_data(item['dsnw']) # 적설
                dc10Tca = str_to_int_for_weather_data(item['dc10Tca']) # 전운량 -> 구름의 양 10분위..
                dmstMtphNo = item['dmstMtphNo'] # 기상 코드 -> 싸락눈(11) + 연무(40) -> 1140으로 붙여서 나오는 듯..?
                
                processed_weather_data = [tm, observer_code, observer_key, rn, dsnw, dc10Tca, dmstMtphNo]
                observer_results_dict[observer_code].append(processed_weather_data)
            now_date += timedelta(days = 1)
        except Exception as e:
            time.sleep(3.5)
        time.sleep(1)
        tq.set_description_str(f"{cnt}/{len(tq)} {observer_key} {now_date}/{today}")
    cnt += 1

total_result = []
for k, v in observer_results_dict.items():
    total_result += v
    

start_date_str, end_date_str = start_date.strftime("%Y%m%d"), today.strftime("%Y%m%d")


file_name = f"weather_data_{start_date_str}_{end_date_str}_full.csv"
total_result = pd.DataFrame(total_result, columns = ['tm', 'id', 'location', 'rain', 'snow', 'cloud', 'weather_code'])
total_result['weather_code'] = total_result['weather_code'].map(lambda x: None if x == '' else x)

total_result.to_csv(f"./{file_name}", index=False)