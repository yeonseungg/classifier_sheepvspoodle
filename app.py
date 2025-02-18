# 3.10 버전이하에서만 작동합니다.
# conda create -n test2 python=3.10
#  model.py에 streamlit만 포함시킨 것

import streamlit as st
from keras.models import load_model
from PIL import Image, ImageOps
import numpy as np

# Streamlit 앱 설정
st.set_page_config(page_title="푸들 vs 양 분류기", page_icon="🐶", layout="centered")
st.title("🐩 푸들 vs 양 분류기 🐏")
st.markdown("### 이미지를 업로드하여 판별해보세요!")

# 사이드바에서 이미지 입력 방식 선택
st.sidebar.header("이미지 입력 방식 선택")
input_method = st.sidebar.radio("", ["📂 파일 업로드", "📸 카메라 사용"])

# 파일 업로드 화면에서만 예시 이미지 표시
if input_method == "📂 파일 업로드":
    st.markdown("#### 예시 이미지")
    col1, col2 = st.columns([1, 1])
    with col1:
        st.image("푸푸sheep.jpg",caption="예시 양푸들 1  \n출처: 정명희 강아지 푸푸씨", width=180)
    with col2:
        st.image("치즈sheep.jpg", caption="예시 양푸들 2 치즈씨", width=230)
    
    # 파일 업로드 UI
    img_file_buffer = st.file_uploader("이미지 파일 업로드 (png, jpg, jpeg)", type=["png", "jpg", "jpeg"])
else:
    img_file_buffer = st.camera_input("정중앙에 사물을 위치하고 사진을 찍어주세요!")

# 이미지 처리 및 모델 예측
if img_file_buffer is not None:
    image = Image.open(img_file_buffer).convert('RGB')
    image = ImageOps.fit(image, (224, 224), Image.Resampling.LANCZOS)
    image_array = np.asarray(image)
    normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    data[0] = normalized_image_array

    # 예측 수행
    model = load_model('keras_model.h5', compile=False)
    class_names = open('labels.txt', 'r').readlines()
    prediction = model.predict(data)
    index = np.argmax(prediction)
    class_name = class_names[index].strip()
    confidence_score = prediction[0][index]

    # 결과 출력
    st.image(image, caption="업로드한 이미지", use_container_width =True)
    st.markdown("## 📌 예측 결과")
    st.markdown(f"### ▶️ {class_name[2:]} 🏷️")
    st.markdown(f"#### ✅ 신뢰도: {confidence_score:.2%}")
    
    if confidence_score > 0.8:
        st.success("🔍 높은 신뢰도로 예측되었습니다!")
    else:
        st.warning("⚠️ 신뢰도가 낮습니다. 더 선명한 이미지를 사용해보세요!")