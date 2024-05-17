# pip install pandas

high_ways = ['경부선', '남해선(순천-부산)', '남해선(영암-순천)', '부산신항선', '광주대구선', '무안광주선', '고창담양선', '서해안선',
             '평택시흥선', '울산선', '평택화성선', '오산화성선', '대구포항선', '익산장수선', '호남선', '논산천안선', '순천완주선', '구리포천선',
             '청주영덕선', '당진대전선', '옥산오창선', '통영대전선', '중부선', '제2중부선', '평택제천선', '중부내륙선', '영동선', '광주원주선',
             '중앙선', '대구부산선', '서울양양선', '동해선(삼척-속초)', '부산울산선', '동해선(부산-포항)', '서울외곽순환선', '남해1지선', '남해2지선',
             '제2경인선', '인천대교선', '경인선', '인천공항선', '서천공주선', '용인서울선', '호남지선', '대전남부선', '상주영천선', '봉담동탄선', '인천김포선',
             '구리포천지선', '중부내륙지선', '중앙선지선', '부산외곽선']

import pandas as pd

columns = ['SUM_YRMTHDAT', 'SUM_HR', 'VDS_CD', 'TRFFCVLM', 'SPD_AVG']


def merge_data(col, classification):
	for way in high_ways:
		file_name = way+classification
		file_paths = [
			f'C:\\Users\\Administrator\\Desktop\\divide_csv\\1월csv\\{file_name}.csv',
			f'C:\\Users\\Administrator\\Desktop\\divide_csv\\2월csv\\{file_name}2.csv',
			f'C:\\Users\\Administrator\\Desktop\\divide_csv\\3월csv\\{file_name}3.csv',
			f'C:\\Users\\Administrator\\Desktop\\divide_csv\\4월csv\\{file_name}4.csv',
			f'C:\\Users\\Administrator\\Desktop\\divide_csv\\5월csv\\{file_name}5.csv'
		]
		dfs = []
		for file_path in file_paths:
			df = pd.read_csv(file_path, usecols=col)
			dfs.append(df)

		merged_df = pd.concat(dfs, ignore_index=True)

		merged_df.to_csv(f'C:\\Users\\Administrator\\Desktop\\divide_csv\\highway_S_csv\\{file_name}.csv',
		                 index=False)


merge_data(columns, 'E')
merge_data(columns, 'S')