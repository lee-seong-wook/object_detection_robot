import time
import Adafruit_PCA9685
import cv2
import numpy as np

# 색상 범위 (BGR 포맷)  블라드 스키 박사도 BGR로 사용하는 데는 다른 이유가 있던 것이 아니라 OpenCV를 만들던 초창기 카메라 산업 개발자들이 BGR을 많이 썼기 때문에 그 자신도 그냥 아무 이유 없이 BGR을 선택하게 된 것

lower_color = np.array([100, 50, 50])
upper_color = np.array([130, 255, 255])

# 웹캠에서 영상을 가져오기
cap = cv2.VideoCapture(0)

robot_handle=Adafruit_PCA9685.PCA9685()
servoMin=150
servoMax=550

def map(value,min_angle,max_angle,min_pulse,max_pulse):
    angle_range=max_angle-min_angle
    pulse_range=max_pulse-min_pulse
    scale_factor=float(angle_range)/float(pulse_range)
    return min_pulse+(value/scale_factor)

def set_angle(channel,angle):
    pulse=int(map(angle,0,180,servoMin,servoMax))
    robot_handle.set_pwm(channel,0,pulse)
    
robot_handle.set_pwm_freq(50)

while True:
    # 비디오 프레임 읽기
    ret, frame = cap.read()

    # BGR을 HSV로 변환
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # 색상 범위에 해당하는 마스크 생성
    mask = cv2.inRange(hsv, lower_color, upper_color)

    # 마스크를 이용하여 원본 이미지에서 색상 영역 추출
    res = cv2.bitwise_and(frame, frame, mask=mask)

    # 이미지 출력
    cv2.imshow('res', res)

    # 'q' 키를 누르면 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    set_angle(0,90)
    time.sleep(2)
    set_angle(5,160)
    time.sleep(2)
    set_angle(1,150)
    time.sleep(2)
    set_angle(2,45)
    set_angle(4,140)
    time.sleep(2)
    set_angle(5,70)
    time.sleep(2)
    set_angle(1,90)
    time.sleep(2)
    
    if cv2.countNonZero(mask) > 0:
        set_angle(0,10)
        time.sleep(2)
    else:
        set_angle(0,170)
        time.sleep(2)

    set_angle(1,130)
    time.sleep(2)
    set_angle(5,165)
    time.sleep(2)
    set_angle(1,80)
    time.sleep(2)
    set_angle(4,90)
    time.sleep(2)
    
# 리소스 해제
cap.release()
cv2.destroyAllWindows()
