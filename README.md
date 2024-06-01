# Volleyball Action Detection

<br>

## 개요

- 세 가지 주요 액션을 감지하도록 학습되었습니다 : 서브(Serve), 스파이크(Spike), 블로킹(Block)
  
- 비디오 스트림 또는 미리 녹화된 비디오 파일에서 액션을 실시간으로 감지합니다.
  
- OpenCV 및 TensorFlow를 사용하여 모델을 통합하고 비디오에 텍스트로 표시합니다.

<br>
<br>

## 파일 구성

1. **data.py** : 데이터 전처리 및 데이터셋 생성 - 배구 경기를 촬영한 동영상 또는 이미지 데이터를 수집합니다.
   
2. **train_model.py** : 모델 학습 - 여러 합성곱 및 풀링 레이어와 밀집 레이어로 구성된 CNN 모델을 정의합니다. 모델은 전처리된 데이터셋을 사용하여 학습됩니다.
   
3. **Action_Detection.py** : 액션 감지 및 텍스트 표시 - 학습된 모델을 로드하여 주어진 동영상에서 액션을 감지합니다. 프레임 단위로 동영상을 처리하고, 각 프레임에 대해 학습된 모델을 적용하여 감지된 행동을 프레임에 주석으로 추가합니다.

<br>

## 사용법

1. **dataset 준비** : 데이터셋을 학습(train) 및 검증(validation) 디렉터리로 구성하고 각 행동(Serve, Spike, Block)에 대해 하위 디렉터리를 만듭니다.
   
2. **데이터 전처리** : `data.py`를 실행하여 데이터셋을 전처리 및 증강합니다.
   
3. **모델 학습** : `train_model.py`를 실행하여 CNN 모델을 학습시킵니다. 학습된 모델은 `volleyball_action_detection_model.h5` 파일로 저장됩니다.
   
4. **액션 감지** : `Action_Detection.py`를 실행하여 동영상에서 액션을 감지하고 주석을 추가합니다.

<br>
<br>

## 결과 분석
<img width="297" alt="image" src="https://github.com/JIAYOOON/Volleyball-Action-Detection/assets/113532368/ba2203b1-865b-4ab8-8af4-8d5b31577853"> 
<br>
[Serve 감지]  
<br> <br>
<img width="299" alt="image" src="https://github.com/JIAYOOON/Volleyball-Action-Detection/assets/113532368/829537ef-bcc0-432e-b9b2-35c6ec4036df"> 
<br>
[Spike 감지]
<br> <br>


![volleyball](https://github.com/JIAYOOON/Volleyball-Action-Detection/assets/113532368/41cf86ec-db8c-4e0a-8623-6a3700103822) 
<br>
[Spike, Block 감지]
<br>
* 스파이크와 블로킹, 두 액션은 종종 동시에 발생하여 구분하기 어려운 경우가 있어, 모델이 둘 중 하나만 감지하는 경우가 있다.

* 연속 프레임 간의 차이가 너무 작을 경우, 모델이 액션을 감지하지 못하는 경우가 있다.

* 서브와 스파이크 액션 자세가 비슷한 경우가 있어 둘의 구분 능력이 떨어진다.

<br>

## 개선 방안
* 각 행동의 예제를 더 많이 수집하고 레이블링하여 모델의 일반화 능력을 향상시킨다.
  
* 다양한 각도, 속도, 선수 자세를 포함하여 데이터셋을 다양화하여 구분 능력을 향상시킨다.
  
* 행동을 구분하는 특징을 강조하기 위해 고급 이미지 전처리 기법을 적용한다.
  
* 프레임 단위가 아닌 연속된 프레임을 분석한다.

<br>

## 참고 

[ChatGPT](https://chat.openai.com/) 

