# pokemon_app
# 설명

1~8세대까지의 포켓몬 데이터를 분석한 웹대시보드입니다.

data에서 각 컬럼별 최대/최소 데이터를 선택하여 각 컬럼별 최강/최약 포켓몬을 알수 있습니다.

chart에서 plotly 차트를 활용하여 컬럼별 기준으로 히스토그램을 만들었으며. 파이차트도 보실수 있습니다.


마지막으로 영어로 포켓몬 이름을 검색하여 1세대 부터 8세대까지의 포켓몬 데이터를 검색해보실수 있습니다.

# 진행과정

## 1. jupyter notebook에서 진행한 내용

  - csv형식의 데이터를 jupyter notebook으로 불러 작업하였습니다.
  - 데이터를 가공하는 과정에서 기존 인덱스 번호를 포켓몬 번호 데이터에 맞게 인덱스를 수정하여 작업하였습니다.
  - 데이터의 상관분석과 차트를 만들어 진행하였습니다. 

## 2. visual studio code 에서 작업

  - visual studio code에서 작업하여 streamlit라이브러리로 웹대시보드를 로컬에서 생성하여 작업하였습니다.
  - 데이터를 설명하는 과정에서 포켓몬 공식사이트에서 이미지를 연결하여 어떤데이터에 어떤 포켓몬이 있는지 알수 있게 하였습니다.
  - 기존 plt차트에서 발전된 plotly차트를 사용하여 사용하는 유저가 차트에 데이터를 마우스만 올리면 볼 수 있게 하였습니다.
  - 상관분석을 통해 각 컬럼간에 데이터는 어떤 상관관계가 있는지 분석해보았고 분석 결과 상관관계가 높지 않아서 인공지능은 사용하지 않았습니다.
  - 마지막으로 포켓몬을 검색하는 과정에서 중복되는 번호의 데이터는 데이터 type를 분석분석 판다스시리즈인 것을 알았고 판다스시리즈를 분류하는 함수로      시리즈안에 데이터를 나눠 중복되는 포켓몬 없이 깔끔하게 검색하는 포켓몬의 데이터와 이미지를 한눈에 확인할 수 있게 하였습니다.

## 3. aws ec2에서 작업

  - aws에서 ec2를 생성하여 프리 티어 서버를 생성하였습니다.
  - 터미널 플랫폼 putty로 ec2에 접속하여 원격으로 작업하여 파이썬 환경을 구축하여 streamlit를 서버에서도 실행할 수 있게 하였습니다.
  - Ec2 서버에서 서버 연결이 끊겨도 접속이 가능하게 하였습니다.





# 스크린샷

![image](https://user-images.githubusercontent.com/120348521/208610779-1300276a-bc0e-4ffe-9990-466e0cf19690.png)

![image](https://user-images.githubusercontent.com/120348521/208610934-c8985851-b045-4139-895c-b5a82c4188db.png)

![image](https://user-images.githubusercontent.com/120348521/208620599-1e7169a5-4a91-4c5b-92d4-b3b622461bc8.png)

![image](https://user-images.githubusercontent.com/120348521/209062948-84aaffce-06f8-48bb-8b80-dd2cafb91458.png)


















# 데이터 레퍼런스

https://www.kaggle.com/datasets/mariotormo/complete-pokemon-dataset-updated-090420?select=pokedex_%28Update_05.20%29.csv
