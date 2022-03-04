> 머신 러닝 순서
Part 1. Import & Data Check
1. target 변수 분포 확인(히스토그램) : 단일 변수 따른 target 변수 변화는 영향을 줄 확률 높아 관련된 파생변수는 성능 향상 도움.

    + 결측치 정도와 처리 방안
    + 결과값과 각 항목 상관계수 확인
- 데이터 확인 
- 이상치 탐색 및 제거
    - 결측 데이터 확인
    - 날짜 관련 변수 날짜형 변환(
- Skewness(비대칭도) 확인
Part 2. EDA(탐색적 분석)
+ 사용 항목 선정 : 데이터 시각화
    - 질적 자료 : 1개변수는 바/파이 차트, 2개 변수는 히트맵, 스택드컬럼 차트
    - 양적 지료 : 1개 변수는 히스토그램, 박스플롯, 라인차트, QQ플롯, 2개 변수는 산점도
+ 분리된 데이터 머지 시 사용 항목 처리 방안
- Numerical Data 탐색
- Categorical Data 탐색
Part 3. Feature Engineering
+ 이상치, 결측치 처리(채우거나, 변경, 열 삭제)
+ 조건 맞게 항목 정리
- Log 변환
- 결측 데이터 처리
- 유의하지 않은 변수 삭제
- Categorical Data 수치형 변환
Part 4. Modeling & make submission
+ Ridge, Lasso : 선형회귀 방식, 성능 떨어지나, 데이터 적으면 강함.
- Model: XGBoost
- Submission