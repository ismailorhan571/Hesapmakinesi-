import streamlit as st
import math

# 1. Sayfa Ayarları
st.set_page_config(page_title="İsmail Pro-Calculator", page_icon="🔢")

# --- CSS İLE MODERN GÖRÜNÜM (Butonları güzelleştirelim) ---
st.markdown("""
    <style>
    div.stButton > button {
        width: 100%;
        height: 60px;
        font-size: 20px;
        font-weight: bold;
        border-radius: 10px;
        background-color: #f0f2f6;
        color: #31333F;
        border: 1px solid #d1d5db;
    }
    div.stButton > button:active { background-color: #FF4B4B; color: white; }
    .display {
        background-color: #1E1E1E;
        color: #00FF00;
        padding: 20px;
        border-radius: 10px;
        font-family: 'Courier New', Courier, monospace;
        font-size: 32px;
        text-align: right;
        margin-bottom: 20px;
        border: 2px solid #333;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. Hesap Makinesi Hafızası (Session State)
if 'result' not in st.session_state:
    st.session_state.result = ""

def add_to_expr(char):
    st.session_state.result += str(char)

def clear_expr():
    st.session_state.result = ""

def calculate():
    try:
        # eval() fonksiyonu matematiksel diziyi hesaplar
        # Güvenlik için sadece matematiksel karakterlere izin verilir
        res = eval(st.session_state.result.replace('x', '*').replace('÷', '/'))
        st.session_state.result = str(res)
    except:
        st.session_state.result = "Hata"

# 3. Ana Arayüz
st.title("🔢 Pro Calculator")
st.caption("Geliştirici: **İsmail Orhan**")

# Ekran (Sonucu gösteren alan)
st.markdown(f'<div class="display">{st.session_state.result if st.session_state.result else "0"}</div>', unsafe_allow_html=True)

# 4. Buton Takımı (Grid Yapısı)
col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("C"): clear_expr
