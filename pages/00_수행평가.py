import streamlit as st
import random

st.set_page_config(
    page_title="🎬 나이별 영화 추천기",
    page_icon="🍿",
)

st.title("🎬 나이별 영화 추천기")
st.write("나이를 입력하면 딱 맞는 영화를 추천해줄게! 🍿✨")

age = st.number_input(
    "🙋 나이를 입력해줘!",
    min_value=1,
    max_value=100,
    step=1
)

movies = {
    "child": [
        "겨울왕국 ❄️",
        "토이 스토리 🤠",
        "주토피아 🦊",
        "코코 🎸",
        "인사이드 아웃 😊"
    ],
    "teen": [
        "스파이더맨: 뉴 유니버스 🕷️",
        "해리 포터 ⚡",
        "인터스텔라 🚀",
        "너의 이름은 🌠",
        "어벤져스 💥"
    ],
    "young_adult": [
        "인셉션 🌀",
        "탑건: 매버릭 ✈️",
        "듄 🏜️",
        "기생충 🏠",
        "라라랜드 🎹"
    ],
    "adult": [
        "쇼생크 탈출 🔑",
        "포레스트 검프 🏃",
        "그린 북 🚗",
        "캐치 미 이프 유 캔 🎭",
        "보헤미안 랩소디 🎤"
    ]
}

if st.button("🎁 영화 추천받기"):
    if age <= 12:
        category = "child"
        message = "어린이에게 인기 많은 영화들이야! 🌈"
    elif age <= 19:
        category = "teen"
        message = "청소년이라면 재밌게 볼 만한 작품들이야! 😎"
    elif age <= 39:
        category = "young_adult"
        message = "몰입감 최고인 영화들을 골라봤어! 🔥"
    else:
        category = "adult"
        message = "오랫동안 사랑받은 명작들을 추천할게! 🎬"

    recommendation = random.choice(movies[category])

    st.success(f"✨ 추천 영화: {recommendation}")
    st.info(message)

    st.write("🍿 즐거운 영화 감상 시간 보내!")
