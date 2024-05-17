import pandas as pd

values = [
    ('0010', '경부선'),
    ('0100', '남해선(순천-부산)'),
    ('0101', '남해선(영암-순천)'),
    ('0105', '부산신항선'),
    ('0120', '광주대구선'),
    ('0121', '무안광주선'),
    ('0140', '고창담양선'),
    ('0150', '서해안선'),
    ('0153', '평택시흥선'),
    ('0160', '울산선'),
    ('0170', '평택화성선'),
    ('0171', '오산화성선'),
    ('0200', '대구포항선'),
    ('0201', '익산장수선'),
    ('0251', '호남선'),
    ('0252', '논산천안선'),
    ('0270', '순천완주선'),
    ('0290', '구리포천선'),
    ('0300', '청주영덕선'),
    ('0301', '당진대전선'),
    ('0320', '옥산오창선'),
    ('0351', '통영대전선'),
    ('0352', '중부선'),
    ('0370', '제2중부선'),
    ('0400', '평택제천선'),
    ('0450', '중부내륙선'),
    ('0500', '영동선'),
    ('0520', '광주원주선'),
    ('0550', '중앙선'),
    ('0552', '대구부산선'),
    ('0600', '서울양양선'),
    ('0650', '동해선(삼척-속초)'),
    ('0651', '부산울산선'),
    ('0652', '동해선(부산-포항)'),
    ('1000', '서울외곽순환선'),
    ('1020', '남해1지선'),
    ('1040', '남해2지선'),
    ('1100', '제2경인선'),
    ('1102', '인천대교선'),
    ('1200', '경인선'),
    ('1300', '인천공항선'),
    ('1510', '서천공주선'),
    ('1710', '용인서울선'),
    ('2510', '호남지선'),
    ('3000', '대전남부선'),
    ('3010', '상주영천선'),
    ('3300', '제3경인선'),
    ('4000', '봉담동탄선'),
    ('4001', '인천김포선'),
    ('4002', '구리포천지선'),
    ('4510', '중부내륙지선'),
    ('5510', '중앙선지선'),
    ('6000', '부산외곽선')
]

for vds_id, highway in values:

    filtered_dfs = []
    for i in range(101, 516):
        file_path = f'/Users/kimseunghyun/Traffic/divide_csv/new/0{i}.csv'
        df = pd.read_csv(file_path)
        
        filtered_df = df[['기준일', '기준시간', 'VDS_ID', '교통량', '평균속도','노드명','도로명']]
        filtered_df = filtered_df[filtered_df['VDS_ID'].str.startswith(f'{vds_id}VDE')]
        filtered_dfs.append(filtered_df)
    
    result_df = pd.concat(filtered_dfs, ignore_index=True)
    result_df.to_csv(f'{highway}En.csv', index=False)
    
    filtered_dfs = []
    for i in range(101, 516):
        file_path =  f'/Users/kimseunghyun/Traffic/divide_csv/new/0{i}.csv'
        df = pd.read_csv(file_path)

        filtered_df =  df[['기준일', '기준시간', 'VDS_ID', '교통량', '평균속도','노드명','도로명']]
        filtered_df = filtered_df[filtered_df['VDS_ID'].str.startswith(f'{vds_id}VDS')]
        filtered_dfs.append(filtered_df)
        
    result_df = pd.concat(filtered_dfs, ignore_index=True)
    result_df.to_csv(f'{highway}Sn.csv', index=False)
    
