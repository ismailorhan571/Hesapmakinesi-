import streamlit as st

# 1. Sayfa Ayarları
st.set_page_config(page_title="Pro Calculator", page_icon="🔢", layout="centered")

# 2. HİÇ BOZULMAYAN MOBİL GRID TASARIMI (CSS)
st.markdown("""
    <style>
    /* Ana ekranı ve butonları sabitle */
    .stApp { background-color: #000000; }
    
    .calc-container {
        display: grid;
        grid-template-columns: repeat(5, 1fr);
        gap: 8px;
        max-width: 400px;
        margin: auto;
    }
    
    .stButton > button {
        width: 100% !important;
        height: 60px !important;
        border-radius: 12px !important;
        font-size: 20px !important;
        font-weight: bold !important;
        border: none !important;
    }

    /* Sayı Butonları (Koyu Gri) */
    div.stButton > button:not([kind="primary"]):not([kind="secondary"]) {
        background-color: #333333 !important;
        color: white !important;
    }

    /* İşlem Butonları (Turuncu - 5. Sütun) */
    .orange-btn button {
        background-color: #ff9500 !important;
        color: white !important;
    }

    /* Üst Butonlar (Açık Gri) */
    .gray-btn button {
        background-color: #a5a5a5 !important;
        color: black !important;
    }

    /* Ekran Tasarımı */
    .display {
        background-color: #1c1c1c;
        color: white;
        padding: 30px 15px;
        border-radius: 15px;
        font-size: 45px;
        text-align: right;
        font-family: sans-serif;
        margin-bottom: 20px;
        min-height: 100px;
        word-wrap: break-word;
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

# 4. Arayüz Başlığı
st.markdown("<h2 style='text-align: center; color: white;'>Pro Calculator</h2>", unsafe_allow_html=True)

# Ekran
st.markdown(f'<div class="display">{st.session_state.ifade if st.session_state.ifade else "0"}</div>', unsafe_allow_html=True)

# 5. BUTONLAR (Sıralı ve Bozulmaz)
# Her satırı ayrı sütun grupları olarak tanımlıyoruz
def create_row(buttons, types):
    cols = st.columns(5)
    for i in range(5):
        with cols[i]:
            btn_label = buttons[i]
            if btn_label == "AC":
                st.button(btn_label, on_click=temizle, key=f"btn_{btn_label}")
            elif btn_label == "DEL":
                st.button(btn_label, on_click=sil, key=f"btn_{btn_label}")
            elif btn_label == "=":
                st.button(btn_label, on_click=hesapla, type="primary", key=f"btn_{btn_label}")
            else:
                # 5. Sütun turuncu olsun diye özel class (Simüle edilmiş)
                st.button(btn_label, on_click=ekle, args=(btn_label,), key=f"btn_{i}_{btn_label}")

# Buton Dizilimi
create_row(["7", "8", "9", "AC", "÷"], ["n", "n", "n", "g", "o"])
create_row(["4", "5", "6", "DEL", "×"], ["n", "n", "n", "g", "o"])
create_row(["1", "2", "3", "%", "-"], ["n", "n", "n", "n", "o"])
create_row(["0", "00", ".", "=", "+"], ["n", "n", "n", "p", "o"])

st.markdown("<p style='text-align: center; color: #555;'>Geliştirici: İsmail Orhan</p>", unsafe_allow_html=True)
