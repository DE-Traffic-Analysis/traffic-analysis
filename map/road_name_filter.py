import csv

road_name_mapping = {
    '구리포천지선': '구리포천선',
    '남해선(순천-부산)': '남해선(순천부산)',
    '남해선(영암-순천)': '남해선(영암순천)',
    '동해선(부산-포항)': '동해선',
    '동해선(삼척-속초)': '동해선(삼척속초)',
    '상주연천선': '상주영덕선',
    '제2경인선': '제2경인선(인천안양)',
    '중부내륙의지선': '중부내륙의 지선',
    '중앙선의지선': '중앙선의 지선',
    '통영대전선': '통영대전선/중부선',
    '호남선의지선': '호남선의 지선'
}

with open('node.csv', 'r', encoding='CP949') as file:
    reader = csv.DictReader(file)

    updated_data = []

    for row in reader:
        if row['도로명'] in road_name_mapping:
            row['도로명'] = road_name_mapping[row['도로명']]

        updated_data.append(row)

with open('updated_node.csv', 'w', newline='', encoding='CP949') as file:
    writer = csv.DictWriter(file, fieldnames=reader.fieldnames)
    writer.writeheader()
    writer.writerows(updated_data)
