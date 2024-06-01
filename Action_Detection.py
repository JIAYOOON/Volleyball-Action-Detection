import cv2
import numpy as np
from tensorflow.keras.models import load_model

# 학습된 모델 로드
model = load_model('volleyball_action_detection_model.h5')

# 액션 목록
actions = ['Serve', 'Spike', 'Block']

def preprocess_frame(frame):
    resized_frame = cv2.resize(frame, (150, 150))
    normalized_frame = resized_frame / 255.0
    return np.expand_dims(normalized_frame, axis=0)

# 이전 프레임
prev_action = None

video_path = 'C:/Users/yoonj/volleyball3.mp4' 
cap = cv2.VideoCapture(video_path)

# 비디오 저장
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  
out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (int(cap.get(3)), int(cap.get(4))))

# 비디오 프레임의 너비 가져오기
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))

# ROI 설정 (세로로 3등분하여 중앙 영역 선택)
left = frame_width // 3  
right = frame_width * 2 // 3  
top = 0  
bottom = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))  

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # ROI 설정
    roi = frame[top:bottom, left:right]

    # 현재 프레임
    preprocessed_frame = preprocess_frame(roi)
    predictions = model.predict(preprocessed_frame)
    action_index = np.argmax(predictions[0])
    action = actions[action_index]

    if action != prev_action:
        # 텍스트
        cv2.putText(frame, action, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
        prev_action = action

    # 비디오 저장 
    out.write(frame)

    # 화면에 표시
    cv2.imshow('Volleyball Action Detection', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()