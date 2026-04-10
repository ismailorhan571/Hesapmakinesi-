import streamlit as st

# 1. Sayfa Ayarları
st.set_page_config(page_title="Pro Calculator", page_icon="🔢", layout="centered")

# 2. MOBİLDE SÜTUNLARIN BOZULMASINI ENGELLEYEN ÖZEL CSS
st.markdown("""
    <style>
    /* Sütunların mobilde alt alta gelmesini engelle */
    [data-testid="column"] {
        width: calc(20% - 10px) !important;
        flex: 1 1 calc(20% - 10px) !important;
        min-width: calc(20% - 10px) !important;
    }
    
    /* Buton Tasarımları */
    .stButton>button {
        width: 100%;
        height: 55px;
        font-size: 18px !important;
        font-weight: bold;
        border-radius: 10px;
        border: none;
        margin-bottom: -15px;
    }
    
    /* Ekran Tasarımı */
    .display-box {
        background-color: #1a1a1a;
        color: #ffffff;
        padding: 20px;
        border-radius: 15px;
        font-size: 35px;
        text-align: right;
        font-family: 'Courier New', monospace;
        margin-bottom: 20px;
        border: 2px solid #333;
        min-height: 70px;
        word-wrap: break-word;
    }
    
    /* İşlem Butonları (Turuncu) */
    div[data-testid="stHorizontalBlock"] > div:nth-child(5) button {
        background-color: #ff9500;
        color: white;
    }
    
    /* Sayı Butonları */
    div[data-testid="stHorizontalBlock"] > div:nth-child(-n+4) button {
        background-color: #333333;
        color: white;
    }

    /* Temizleme Butonu */
    button[kind="secondary"] {
        background-color: #a5a5a5 !important;
        color: black !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Hesap Makinesi Mantığı
if 'ifade' not in st.session_state:
    st.session_state.ifade = ""

def ekle(tus):
    st.session_state.ifade += str(tus)

def temizle():
    st.session_state.ifade = ""

def sil():
    st.session_state.ifade = st.session_state.ifade[:-1]

def hesapla():
    try:
        islem = st.session_state.ifade.replace('×', '*').replace('÷', '/')
        sonuc = eval(islem)
        if sonuc == int(sonuc): sonuc = int(sonuc)
        st.session_state.ifade = str(sonuc)
    except:
        st.session_state.ifade = "Hata"

# 4. Arayüz
st.markdown("<h2 style='text-align: center; color: white;'>Pro Calculator</h2>", unsafe_allow_html=True)
st.markdown(f'<div class="display-box">{st.session_state.ifade if st.session_state.ifade else "0"}</div>', unsafe_allow_html=True)

# 5. BUTON TAKIMI (HİÇ BOZULMAYAN GRID
