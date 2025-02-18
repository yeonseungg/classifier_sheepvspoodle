# 🐩 푸들 vs 양 분류기 🐏

![image](https://github.com/user-attachments/assets/0fb4a626-308e-4216-b8da-24ead608153e)
[완성된 페이지](https://classifiersheepvspoodle-vso5pv7pq4dtksxtjhtxd5.streamlit.app/)



## 📌 프로젝트 개요

이 프로젝트는 Keras 모델을 사용하여 업로드된 이미지를 분석하고, 해당 이미지가 푸들인지 양인지 분류하는 Streamlit 프로젝트입니다.  

  

  
## 🚀 주요 기능

이미지 업로드 지원: 사용자가 파일을 업로드하여 이미지를 분석 가능  

카메라 입력 지원: 실시간 촬영 후 바로 분석 가능  

딥러닝 기반 이미지 분류: Keras 모델(keras_model.h5)을 활용하여 이미지를 예측  

결과 출력: 예측된 클래스 및 신뢰도 표시  




## 🛠️ 기술 스택

Python 3.10  

TensorFlow / Keras  

Streamlit  

NumPy  

Pillow (PIL)  




## 🏷️ 요구 사항  

이 프로젝트는 Python 3.10 이하에서 실행해야 한다. Streamlit Cloud에서는 runtime.txt 파일을 설정해야 합니다.  



## ❗ 문제 해결 

### ✅ tensorflow==2.12 설치 오류 발생 시  

TensorFlow 2.12는 Python 3.10 이하에서만 작동합니다. Python 3.12 환경에서 실행하려면 tensorflow==2.17.1로 업그레이드하거나, Python 3.10 환경을 사용해야 합니다.
  
해결 방법 1: runtime.txt에 3.10 추가  
  
해결 방법 2: tensorflow==2.17.1로 버전 변경 후 pip install -r requirements.txt 실행  





