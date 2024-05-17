# 고속도로 VDS 기반 교통 데이터 분석 대시보드
----
# 프로젝트 개요

현대 사회에서는 교통 흐름을 효과적으로 관리하는 것이 필수적입니다. 특히 고속도로는 주요 교통 수단으로, 교통량과 차량 속도 정보를 시간에 따라 시각화하여 교통 체증을 판단하고, 효율적인 교통 관리를 계획할 수 있습니다. 본 프로젝트는 VDS가 수집한 데이터를 기반으로 날짜별, 고속도로별, 일부 구간별 다양한 데이터를 보여주는 대시보드를 구성했습니다. 특정 구간 또는 특정 도로의 교통량이 많다면 당시 평균 속도는 어떤지, 차의 종류는 무엇인지, 날씨 및 강수량과 연관 지어 확인할 수 있으며, 지도를 통해 어느 위치에 있는지 확인할 수 있습니다.


# 프로젝트 목표

- 수집한 데이터에서 필요한 데이터만 정리
- 정리된 데이터를 Redshift에 적재 후 Superset에 연결
- 연결된 데이터를 바탕으로 대시보드 구성 후 필터 생성


# 프로세스 설명

## Data Crawling / Data preprocessing

### 데이터 출처

- VDS 교통 데이터
  - [국가교통 데이터 오픈마켓](https://www.bigdata-transportation.kr/frn/prdt/detail?prdtId=PRDTNUM_000000000025)
- 날씨 데이터
  - [기상자료개방포털[데이터:기상관측:지상:종관기상관측(ASOS):자료]](https://data.kma.go.kr/data/grnd/selectAsosRltmList.do?pgmNo=36&openPopup=Y)
- 고속도로 좌표
    - 도로 좌표 데이터
      - [한국도로공사_도로중심선_이정_좌표_20210107](https://www.data.go.kr/data/15045608/fileData.do)
    - 노드(IC/JC) 데이터
      - [고속도로 공공데이터 포털](https://data.ex.co.kr/portal/docu/docuList?datasetId=716&serviceType=&keyWord=이정&searchDayFrom=2014.12.01&searchDayTo=2024.05.15&CATEGORY=&GROUP_TR=&sId=716)
- 차종별 데이터
  - [고속도로 공공데이터 포털](https://data.ex.co.kr/portal/fdwn/view?type=ETC&num=30&requestfrom=dataset#)

  
# 팀원 및 역할

- 김승훈: 고속도로 및 구간을 나타내는 지도 대시보드 생성
- 김승현: 고속도로 구간별 교통량 대시보드 생성
- 김동기: 고속도로 구간별 평균 속도 대시보드 생성
- 남원우: 고속도로 구간별 차종의 교통량 대시보드 생성
- 김유민: 고속도로 구간별 날씨(강수량 및 적설량) 대시보드 생성


# 활용 기술 및 프레임워크

### Language
- Python
- SQL

### Dashboard
- Superset
  
### DataLake
- AWS S3
  
### 데이터 웨어하우스
- AWS Redshift Serverless

### 커뮤니케이션 및 협업 도구
- Gather Town
- Git/GitHub
- Slack
- Notion
