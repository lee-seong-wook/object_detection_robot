# object-detection-robot-

HSV값으로 물건을 분류해 로봇팔을 움직이는 코드, YOLOv5 pt파일을 테스트하는 코드, pt파일을 사용해 인식한 객체를 분류하는 코드입니다.

라즈베리파이 환경에서 제작했으며 PCA9685서보모터 드라이버를 사용했습니다. 해당 모듈을 사용하려면 아래와같이 라이브러리를 설치해야합니다.

$ sudo apt-get install git build-essential python-dev

$ git clone https://github.com/adafruit/Adafruit_Python_PCA9685.git

$ cd Adafruit_Python_PCA9685

$ sudo python3 setup.py install

로봇암의 경우 3D프린터로 인쇄하여 사용했습니다.

팔의 각도는 물건 분류에 따른 위치선정 이외에 자동으로 위치를 잡는게 아니기 때문에 각 설정이 따로 필요 합니다.



객체인식을 활용한 로봇팔의 로직도입니다.


![image](https://github.com/lee-seong-wook/object-detection-robot-/assets/130055880/7b675dbb-b868-46c8-8d8c-7f1a5ced238b)
