import pandas as pd
high_ways = ["경인선", "고창담양선", "광주대구선", "구리포천선", "남해1지선", "남해2지선",
    "남해선(순천-부산)", "남해선(영암-순천)", "당진대전선", "대구포항선", "대전남부선",
    "동해선(부산-포항)", "동해선(삼척-속초)", "무안광주선", "봉담동탄선", "부산외곽선",
    "서울양양선", "서천공주선", "순천완주선", "오산화성선", "울산선","인천공항선", "제2경인선",
    "제2중부선", "중부내륙선", "중부선", "중앙선", "중앙선지선", "청주영덕선", "통영대전선",
    "평택제천선", "평택화성선", "호남선", "호남지선", "중부내륙선", "경부선", "영동선", "서해안선"
]

for way in high_ways:
    
    # 데이터 로드
    vds_info = pd.read_csv('{way}E.csv')
    node_info = pd.read_csv('node_check.csv')

    # 데이터 조인
    merged_df = pd.merge(vds_info, node_info, left_on=['도로명', '노드명'], right_on=['도로명','시작IC'], how='inner')

    # 결측치 제거
    merged_df = merged_df[(merged_df['평균속도'] != -1) & (merged_df['교통량'] != -1)]

    # 도로명과 노드명을 결합
    merged_df['section'] = merged_df.apply(lambda row: f"{row['도로명']}({row['시작IC']}-{row['종료IC']})", axis=1)
    merged_df.drop(['도로명', '시작IC', '종료IC', '이정', '노드명'], axis=1, inplace=True)

    # 평균계산 및 컬럼명 변경
    road_vds_df = merged_df.groupby(['section', '기준일', '기준시간']).agg({'교통량': 'mean', '평균속도': 'mean'}).reset_index()
    road_vds_df.rename(columns={'기준일':'date', '기준시간':'time','교통량': 'AVG_trff', '평균속도': 'AVG_spd_avg'}, inplace=True)

    # 평균값을 소수점 3자리까지 반올림하여 표시
    road_vds_df['AVG_trff'] = road_vds_df['AVG_trff'].round(3)
    road_vds_df['AVG_spd_avg'] = road_vds_df['AVG_spd_avg'].round(3)

    # CSV 저장
    output_path = '/Traffic/{way}E_AVG.csv'
    road_vds_df.to_csv(output_path, index=False)