import streamlit as st
from streamlit_lottie import st_lottie
import requests
import json
import time
from datetime import datetime, timedelta
import random

# Page configuration
st.set_page_config(
    page_title="Para Mi Amor Cris por su día",
    page_icon="❤️",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Custom CSS
st.markdown("""
<style>
    .main {
        background: linear-gradient(135deg, #ffafbd, #ffc3a0);
    }
    h1, h2, h3 {
        color: #d81b60;
        text-align: center;
    }
    .stButton button {
        background-color: #d81b60;
        color: white;
        border-radius: 20px;
        padding: 10px 20px;
        font-size: 18px;
        border: none;
    }
    .stButton button:hover {
        background-color: #ad1457;
    }
    .message-box {
        background-color: rgba(255, 255, 255, 0.7);
        padding: 20px;
        border-radius: 15px;
        margin: 20px 0;
        text-align: center;
    }
    .heart-container {
        display: flex;
        justify-content: center;
        margin: 20px 0;
    }
</style>
""", unsafe_allow_html=True)

# Function to load Lottie animations
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Load animations
heart_animation = load_lottieurl("https://d1jj76g3lut4fe.cloudfront.net/saved_colors/115797/mvgHZEjtCt5H5twH.json")
love_animation = load_lottieurl("https://d1jj76g3lut4fe.cloudfront.net/saved_colors/115797/Rkwtm9eDZPnp3PCP.json")
flying_hearts = json.load(open("amor1.json"))

# Love messages
love_messages = [
    "Eres fuerte, hermosa y única amor.",
    "Amarte es mi mayor suerte. Feliz Día de la mujer mi amor.",
    "En tus ojitos encontré mi lugar favorito.",
    "Eres el amor que siempre estoy encantado de haber encontrado.",
    "Eres un ejemplo de amor y valentía mi amor.",
    "Eres la mejor persona que he conocido en mi vida."
]

# Header with animation
st.markdown("<h1>Para Mi Amor Cris por su día ❤️</h1>", unsafe_allow_html=True)

# Main animation
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st_lottie(love_animation, height=300, key="main_animation")

# Current date and time
now = datetime.now()
st.markdown(f"<h3>Hoy es {now.strftime('%d/%m/%Y')}(era para el 8 uu) y quiero decirte...</h3>", unsafe_allow_html=True)

# Love message section
if 'message_index' not in st.session_state:
    st.session_state.message_index = 0

if st.button("💖 Nuevo Mensaje de Amor 💖"):
    st.session_state.message_index = (st.session_state.message_index + 1) % len(love_messages)
    st.balloons()

message = love_messages[st.session_state.message_index]
st.markdown(f"""
<div class="message-box">
    <h2>{message}</h2>
</div>
""", unsafe_allow_html=True)

# Flying hearts animation
st_lottie(flying_hearts, height=200, key="flying_hearts")

# Interactive section
st.markdown("<h3>¿Cuánto te quiero?</h3>", unsafe_allow_html=True)
love_level = st.slider("", 1, 100, 100)

if love_level == 100:
    st.markdown("<h2>¡Te quiero infinitamenteeee!(más que tu uu :'D) ❤️</h2>", unsafe_allow_html=True)
    st.markdown("<div class='heart-container'>", unsafe_allow_html=True)
    st_lottie(heart_animation, height=150, key="heart_full")
    st.markdown("</div>", unsafe_allow_html=True)
else:
    st.markdown(f"<h2>Te quiero {love_level}% (¡En realidad 100%! jajs solo quería practicar a hacer la barrita xd)</h2>", unsafe_allow_html=True)

# Photo gallery section
st.markdown("<h3>Nuestros Fotoooos</h3>", unsafe_allow_html=True)
st.markdown("""
<div style="text-align: center; padding: 20px; background-color: rgba(255, 255, 255, 0.7); border-radius: 15px;">
    <p>Aquí puedes añadir nuestras fots juntos jeje(videos no uu :').</p>
</div>
""", unsafe_allow_html=True)

# Upload photo option
uploaded_file = st.file_uploader("Sube una foto amor", type=["jpg", "jpeg", "png"])
if uploaded_file is not None:
    st.image(uploaded_file, caption="Nuestro foto", use_container_width=True)

# Special date counter
st.markdown("<h3>Nuestro Amor contado de nuevo :D</h3>", unsafe_allow_html=True)

# You can set this to your actual anniversary date
anniversary_date = st.date_input("Fecha en que comenzamos", datetime(2022, 8, 25))
today = datetime.now().date()
days_together = (today - anniversary_date).days

if days_together >= 0:
    st.markdown(f"""
    <div class="message-box">
        <h2>Llevamos {days_together} días juntos (celebramos los mil en uruguayyy!)</h2>
        <p>Disculpame por hacerte enorjar uu.</p>
    </div>
    """, unsafe_allow_html=True)
else:
    st.markdown(f"""
    <div class="message-box">
        <h2>Nuestra historia de amor comenzará en {abs(days_together)} días</h2>
        <p>Aqui es una prueba(para cambiar nuestra fecha y no caiga 25 siempre jsj).</p>
    </div>
    """, unsafe_allow_html=True)


st.markdown("<h3>Fechas Importantes</h3>", unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    special_date = st.date_input("Fecha especial", datetime(2025, 8, 25))
with col2:
    event_name = st.text_input("Nombre del evento", "Nuestro Aniversario")

days_until = (special_date - today).days

if days_until > 0:
    st.markdown(f"""
    <div class="message-box">
        <h2>Faltan {days_until} días para {event_name}</h2>
        <div class="progress-container" style="background-color: #f3f3f3; border-radius: 13px; height: 20px;">
            <div class="progress-bar" style="background-color: #d81b60; height: 20px; border-radius: 13px; width: {100*days_until/365}%"></div>
        </div>
    </div>
    """, unsafe_allow_html=True)



# Footer
st.markdown("""
<div style="text-align: center; margin-top: 50px; padding: 20px;">
    <p>Hecho con ❤️ y python para ti :D</p>
</div>
<div style="text-align: center; margin-top: 50px; padding: 20px;">
    <p> Aqui falta una animacion de python pero aun no acabo jeje</p>
</div>
""", unsafe_allow_html=True)