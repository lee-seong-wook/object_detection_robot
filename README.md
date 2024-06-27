# object-detection-robot
<div align="center">
<img width="500" alt="image" src="https://github.com/lee-seong-wook/object-detection-robot-/assets/130055880/68c49e59-2b6d-4b76-8db3-d72ced890d3f">

## 팀 소개

|     팀장: 이성욱       |         팀원: 이용진         |      팀원: 이경현         | 
| :------------------------------------------------------------------------------: | :---------------------------------------------------------------------------------------------------------------------------------------------------: | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: | 
|   <img width="160px" src="https://github.com/lee-seong-wook/object-detection-robot-/assets/130055880/81cae49a-dc9d-4fbd-81ad-cae715314337" />    |                      <img width="160px" src="https://github.com/lee-seong-wook/object-detection-robot-/assets/130055880/b032aa51-f0d0-4354-b310-d57b3549b58a" />    |                  <img width="160px" src="https://github.com/lee-seong-wook/object-detection-robot-/assets/130055880/01beb4ea-ef4f-4a5a-8c83-c5b6dc25552e"/>   |
| 대림대학교 메카트로닉스과 3학년 | 대림대학교 메카트로닉스과 3학년 | 대림대학교 메카트로닉스과 3학년 |
|  로봇 동작 제어 및 객체인식 개발     |  로봇 동작 제어 및 객체인식 개발   | 하드웨어 제작 및 모델링    |


HSV값으로 물건을 분류해 로봇팔을 움직이는 코드, YOLOv5 pt파일을 테스트하는 코드, 저희가 만든 모델을 사용해 학습한 객체를 분류하는 코드입니다.

라즈베리파이 환경에서 제작했으며 PCA9685서보모터 드라이버를 사용했습니다. 해당 모듈을 사용하려면 아래와같이 라이브러리를 설치해야합니다.

$ sudo apt-get install git build-essential python-dev

$ git clone https://github.com/adafruit/Adafruit_Python_PCA9685.git

$ cd Adafruit_Python_PCA9685

$ sudo python3 setup.py install

로봇암의 경우 3D프린터로 인쇄하여 사용했습니다.

팔의 각도는 물건 분류에 따른 위치선정 이외에 자동으로 위치를 잡는게 아니기 때문에 각 설정이 따로 필요 합니다.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------





데이터 수집후 증강(augmentaion) 기법을 사용하여 약 2200장의 사진을 수집 후 라벨링을 진행하였습니다.

![image](https://github.com/lee-seong-wook/object-detection-robot-/assets/130055880/2cee1a36-778c-4070-b86f-53e4de294afd)

--------------------------------------------------------------------------------------------------------------------------------------------------------------------





객체인식을 활용한 로봇팔의 로직도입니다.


![image](https://github.com/lee-seong-wook/object-detection-robot-/assets/130055880/7b675dbb-b868-46c8-8d8c-7f1a5ced238b)
