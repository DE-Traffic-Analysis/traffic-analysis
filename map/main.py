import pandas as pd

highway_df = pd.read_csv('highway.csv')
highway_df.to_parquet("highway.parquet", compression=None)
node_df = pd.read_csv('updated_node.csv', encoding='CP949')
node_df.to_parquet("node.parquet", compression=None)

columns = ['도로명', '구간', '이정']
mileage_df = pd.DataFrame(columns=columns)

# 해당 도로의 최대 이정을 찾는 함수
def find_cur_node_max_mileage(road_name):
    return highway_df[highway_df['도로명'] == road_name]['이정'].max()


for index in range(len(node_df) - 1):
    cur_node, nxt_node = node_df.loc[index], node_df.loc[index + 1]
    cur_node_mileage, nxt_node_mileage = round(cur_node['도로이정'], 1), round(nxt_node['도로이정'], 1)

    cur_road_name = cur_node['도로명']
    # 함수를 한 번 호출하여 변수에 담는 과정을 통해 여러 번 함수를 호출하지 않음
    cur_max_mileage = find_cur_node_max_mileage(cur_road_name)

    if pd.isnull(cur_max_mileage):
        continue
    
    if cur_road_name != nxt_node['도로명']:
        if cur_node_mileage >= cur_max_mileage:
            continue
        else:
            mileage_df = pd.concat([mileage_df, pd.DataFrame({
                '도로명': [cur_road_name],
                '구간': [cur_node['노드명'] + "-" + "도로의 끝"],
                '이정': [[cur_node_mileage, cur_max_mileage]]
            })], ignore_index=True)
    else:
        # 가져온 csv 파일에 같은 노드명이 연속 두 번 나오는 경우가 있어서 예외
        if cur_node['노드명'] == nxt_node['노드명']:
            continue
        # 가져온 csv 파일에 노드명이 (null)인 경우가 있어서 예외
        if cur_node['노드명'] == "(null)":
            continue
        # 만약 현재 노드의 이정이 다음 노드의 이정보다 크다면 예외
        if cur_node_mileage > nxt_node_mileage:
            continue
        mileage_df = pd.concat([mileage_df, pd.DataFrame({
            '도로명': [cur_road_name],
            '구간': [cur_node['노드명'] + "-" + nxt_node['노드명']],
            '이정': [[cur_node_mileage, nxt_node_mileage]]
        })], ignore_index=True)

# 팀원에게 도움이 되기 위한 코드
# mileage_df.to_csv('mileage_info.csv', sep=';', index=False)

columns = ['name', 'section', 'path_json']
df = pd.DataFrame(columns=columns)

# 그룹화된 DataFrame을 미리 만들어서 반복문에서 사용
# 그룹화된 DataFrame은 데이터를 미리 인덱싱하여 빠른 조회가 가능하고, 반복적인 필터링을 제거하여 성능을 향상시킨다.
highway_grouped = highway_df.groupby(['도로명', '이정'])

for index in range(len(mileage_df)):
    data = mileage_df.loc[index]
    road_name, section, mileage = data['도로명'], data['구간'], data['이정']
    coordinates = []

    for m in range(int(mileage[0] * 10), int(mileage[1] * 10 + 1)):
        key = (road_name, round(m, 1))
        if key in highway_grouped.groups:
            selected_rows = highway_grouped.get_group(key)
            x = selected_rows['X좌표값'].iloc[0]
            y = selected_rows['Y좌표값'].iloc[0]

            # 위도와 경도의 값이 바뀌어 있는 부분 처리
            if x > 100:
                coordinates.append([x, y])
            else:
                coordinates.append([y, x])
    if coordinates:
        df = pd.concat([df, pd.DataFrame({
            'name': [road_name],
            'section': [road_name + "(" + section + ")"],
            'path_json': [coordinates]
        })], ignore_index=True)

df.to_csv('map.csv', sep=';', index=False)
