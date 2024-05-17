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

## Data Visualize / Final Dashboard Result
### Dataset 및 차트 생성
- deck.gl(mapbox)를 활용한 고속도로 지도 시각화
  
  ![Untitled](https://github.com/DE-Traffic-Analysis/traffic-analysis/assets/61622859/6fba37e9-669a-444f-ac64-e59ab8c677a0)
  
- 시간에 따른 차량 평균 속도 시각화

  ![%EA%B2%BD%EC%9D%B8%EC%84%A0-avg-spd-bar-chart](https://github.com/DE-Traffic-Analysis/traffic-analysis/assets/61622859/6fb9257b-54c5-42ea-90cf-7e77f53fa99e)
  
- 시간에 따른 교통량 시각화
  
  ![%EA%B2%BD%EC%9D%B8%EC%84%A0-avg-trff-area-chart](https://github.com/DE-Traffic-Analysis/traffic-analysis/assets/61622859/278be6e4-a601-420c-92f1-5c88020b2d5f)

- 시간에 따른 차량 종류별 교통량 시각화
  
  ![Untitled 1](https://github.com/DE-Traffic-Analysis/traffic-analysis/assets/61622859/b95d0e02-77a8-4f30-aabb-63697173793b)
  
- 시간에 따른 날씨(강수량-적설량) 시각화
  
  ![Untitled 2](https://github.com/DE-Traffic-Analysis/traffic-analysis/assets/61622859/12d95768-39f0-40be-8041-564d18453e32)

### 대시보드 구성 및 필터 생성
- 대시보드 구성
  
  ![Untitled 3](https://github.com/DE-Traffic-Analysis/traffic-analysis/assets/61622859/f50d9748-a034-4c6b-b223-bf0c42e5fd9c)
- 필터
  
  ![Untitled 4](https://github.com/DE-Traffic-Analysis/traffic-analysis/assets/61622859/915a8deb-f5ea-4e81-bd0a-cb68631f929d)
  
  - highway
    - 시각화할 고속도로의 이름을 필터링 합니다.
  - section
    - 고속도로 내의 IC/JC를 필터링 합니다.
  - date
    - 어떤 기간으로 날짜를 지정할지 필터링 합니다.

## 활용 기술
### 언어
<img src="https://img.shields.io/badge/Python-3776AB?style=flat&logo=Python&logoColor=white"> <img src="https://img.shields.io/badge/PostgreSQL-4169E1?style=flat&logo=PostgreSQL&logoColor=white">

### 대시보드
<img src="https://img.shields.io/badge/Superset-404040?style=flat&logo=Superset&logoColor=white">

### 데이터 레이크
<img src="https://img.shields.io/badge/Amazon S3-569A31?style=flat&logo=Amazon S3&logoColor=white">

### 데이터 웨어하우스
<img src="https://img.shields.io/badge/Amazon Redshift-8C4FFF?style=flat&logo=Amazon Redshift&logoColor=white">

### 커뮤니케이션 & 협업
<img src="https://img.shields.io/badge/GitHub-181717?style=flat&logo=GitHub&logoColor=white"> <img src="https://img.shields.io/badge/Gather-2535A0?style=flat&logo=Gather&logoColor=white"> <img src="https://img.shields.io/badge/Slack-4A154B?style=flat&logo=Slack&logoColor=white"> <img src="https://img.shields.io/badge/Notion-000000?style=flat&logo=Notion&logoColor=white">

# 참여자 정보
<table>
  <tbody>
    <tr>
      <td align="center"><a href="https://github.com/kdk0411"><img src="https://avatars.githubusercontent.com/u/99461483?v=4" width="100px;" alt=""/><br /><sub><b>김동기</b></sub></a><br /></td>
      <td align="center"><a href="https://github.com/zjacom"><img src="https://avatars.githubusercontent.com/u/112957047?v=4" width="100px;" alt=""/><br /><sub><b>김승훈</b></sub></a><br /></td>
      <td align="center"><a href="https://github.com/Kim-2301"><img src="https://avatars.githubusercontent.com/u/84478606?v=4" width="100px;" alt=""/><br /><sub><b>김승현</b></sub></a><br /></td>
      <td align="center"><a href="https://github.com/7xxogre"><img src="https://avatars.githubusercontent.com/u/61622859?v=4" width="100px;" alt=""/><br /><sub><b>김유민</b></sub></a><br /></td>
      <td align="center"><a href="https://github.com/namjang2"><img src="https://avatars.githubusercontent.com/u/166671899?v=4" width="100px;" alt=""/><br /><sub><b>남원우</b></sub></a><br /></td>
    </tr>
  </tbody>
</table>
