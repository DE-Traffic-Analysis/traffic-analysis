import pandas as pd
import time

highway_df = pd.read_csv('highway.csv')
node_df = pd.read_csv('updated_node.csv', encoding='CP949')

columns = ['도로명', '구간', '이정']
mileage_df = pd.DataFrame(columns=columns)

# 해당 도로의 최대 이정을 찾는 함수
def find_cur_node_max_mileage(road_name):
    return highway_df[highway_df['도로명'] == road_name]['이정'].max()


for index, _ in node_df.iterrows():
    if index == len(node_df) - 1:
        break

    cur_node, nxt_node = node_df.loc[index], node_df.loc[index + 1]
    cur_node_mileage, nxt_node_mileage = round(cur_node['도로이정'], 1), round(nxt_node['도로이정'], 1)

    # 고속도로 데이터에서의 최대 이정 값이 null이면 노드 데이터에는 있지만 고속도로 데이터에는 없는 도로이므로 continue
    if pd.isnull(find_cur_node_max_mileage(cur_node['도로명'])):
        continue
    
    if cur_node['도로명'] != nxt_node['도로명']:
        # 만약 현재 행의 도로이정 값이 고속도로 데이터에서도 최대값이라면 continue
        if cur_node_mileage >= find_cur_node_max_mileage(cur_node['도로명']):
            continue
        else:
            # 최대값이 아니라면 최대 값을 가져와서 도로의 끝을 표시
            mileage_df = pd.concat([mileage_df, pd.DataFrame({'도로명': [cur_node['도로명']],
                                            '구간': [cur_node['노드명'] + "-" + "도로의 끝"],
                                            '이정': [[cur_node_mileage, find_cur_node_max_mileage(cur_node['도로명'])]]})], ignore_index=True)
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
        mileage_df = pd.concat([mileage_df, pd.DataFrame({'도로명': [cur_node['도로명']],
                                        '구간': [cur_node['노드명'] + "-" + nxt_node['노드명']],
                                        '이정': [[cur_node_mileage, nxt_node_mileage]]})], ignore_index=True)

mileage_df.to_csv('mileage_info.csv', sep=';', index=False)

columns = ['name', 'section', 'path_json']
df = pd.DataFrame(columns=columns)

for index, _ in mileage_df.iterrows():
    data = mileage_df.loc[index]
    road_name, section, mileage = data['도로명'], data['구간'], data['이정']
    coordinates = []

    for m in range(int(mileage[0] * 10), int(mileage[1] * 10 + 1)):
        m /= 10
        selected_rows = highway_df[(highway_df['도로명'] == road_name) & (highway_df['이정'] == m)]
        if not selected_rows.empty:
            x = selected_rows['X좌표값'].iloc[0]
            y = selected_rows['Y좌표값'].iloc[0]

            # 위도와 경도의 값이 바뀌어 있는 부분 처리
            if x > 100:
                coordinates.append([x, y])
            else:
                coordinates.append([y, x])
    if coordinates:
        df = pd.concat([df, pd.DataFrame({'name': [road_name],
                                        'section': [road_name + "(" + section + ")"],
                                        'path_json': [coordinates]})], ignore_index=True)

df.to_csv('map.csv', sep=';', index=False)
        