# Volleyball Action Detection

<br>

- Serve, Spike, Block과 같은 주요 액션을 식별합니다.
- 비디오 스트림 또는 미리 녹화된 비디오 파일에서 액션을 실시간으로 감지합니다.
- OpenCV 및 TensorFlow를 사용하여 모델을 통합하고 비디오에 텍스트로 표시합니다.

<br>
<br>

## 프로젝트 구성 요소

1. **data.py** : 데이터 전처리 및 데이터셋 생성 - train 및 validation 데이터를 준비하는 스크립트입니다. 배구 경기를 촬영한 동영상 또는 이미지 데이터를 수집합니다.
데이터는 액션(서브, 스파이크, 블록)을 포함합니다.
2. **train_model.py** : 모델 학습 - 학습 데이터를 사용하여 CNN 모델을 학습시킨다.
4. **Action_Detection.py** : 액션 감지 및 텍스트 표시 - 학습된 모델을 사용하여 실시간 비디오 스트림에서 액션을 감지하고 텍스트로 표시하는 스크립트입니다.

<br>

## 사용법

1. **데이터 준비** : `data.py` 스크립트를 사용하여 학습 및 검증 데이터를 준비합니다.
2. **모델 학습** : `train_model.py` 스크립트를 실행하여 모델을 학습시킵니다.
3. 학습된 모델을 `volleyball_action_detection_model.h5` 파일로 저장합니다.
4. **액션 감지** : `Action_Detection.py` 스크립트를 실행하여 실시간 비디오 스트림에서 액션을 감지하고 텍스트로 표시합니다.

<br>
<br>

## 실행 결과
![volleyball](https://github.com/JIAYOOON/Volleyball-Action-Detection/assets/113532368/41cf86ec-db8c-4e0a-8623-6a3700103822) 


## 참고 

[ChatGPT](https://chat.openai.com/) 

