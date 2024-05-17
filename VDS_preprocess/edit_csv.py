df = pd.read_csv('mileage_info.csv',sep=';')

# 컬럼 분리
df[['시작IC', '종료IC']] = df['구간'].str.split('-', expand=True)
df = df[['도로명', '시작IC', '종료IC', '이정']]

df.to_csv('node_check.csv', index=False)