import streamlit as st

# 1. Sayfa Yapılandırması
st.set_page_config(page_title="Pro Hesap Makinesi", page_icon="🔢", layout="centered")

# 2. Modern Tasarım Ayarları (CSS)
st.markdown("""
    <style>
    .stButton>button {
        width: 100%;
        height: 65px;
        font-size: 24px !important;
        font-weight: bold;
        border-radius: 12px;
        background-color: #f8f9fa;
        color: #212529;
        border: 1px solid #dee2e6;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #e2e6ea;
        border-color: #adb5bd;
    }
    .stButton>button:active {
        background-color: #007bff;
        color: white;
    }
    div[data-testid="stExpander"] { border: none; }
    .display-box {
        background-color: #212529;
        color: #00ff00;
        padding: 25px;
        border-radius: 15px;
        font-size: 40px;
        text-align: right;
        font-family: 'Courier New', monospace;
        margin-bottom: 20px;
        min-height: 100px;
        word-wrap: break-word;
        border: 4px solid #343a40;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Hesap Makinesi Hafızası (Session State)
if 'ifade' not in st.session_state:
    st.session_state.ifade = ""

# Tuşlara basıldığında çalışacak fonksiyonlar
def tus_bas(deger):
    st.session_state.ifade += str(deger)

def temizle():
    st.session_state.ifade = ""

def sil():
    st.session_state.ifade = st.session_state.ifade[:-1]

def hesapla():
    try:
        # Görsel operatörleri Python operatörlerine çeviriyoruz
        islem = st.session_state.ifade.replace('×', '*').replace('÷', '/')
        sonuc = eval(islem)
        # Sonuç tam sayı ise .0 kısmını atalım
        if sonuc == int(sonuc):
            sonuc = int(sonuc)
        st.session_state.ifade = str(sonuc)
    except:
        st.session_state.ifade = "Hata"

# 4. Arayüz Oluşturma
st.markdown("<h1 style='text-align: center;'>🔢 Pro Hesap Makinesi</h1>", unsafe_allow_html=True)
st.markdown(f"<p style='text-align: center;'>Geliştirici: <b>İsmail Orhan</b></p>", unsafe_allow_html=True)

# Dijital Ekran
st.markdown(f'<div class="display-box">{st.session_state.ifade if st.session_state.ifade else "0"}</div>', unsafe_allow_html=True)

# 5. Buton Takımı (Grid Düzeni)
col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("AC"): temizle()
    if st.button("7"): tus_bas("7")
    if st.button("4"): tus_bas("4")
    if st.button("1"): tus_bas("1")
    if st.button("0"): tus_bas("0")

with col2:
    if st.button("DEL"): sil()
    if st.button("8"): tus_bas("8")
    if st.button("5"): tus_bas("5")
    if st.button("2"): tus_bas("2")
    if st.button("."): tus_bas(".")

with col3:
    if st.button("%"): tus_bas("/100")
    if st.button("9"): tus_bas("9")
    if st.button("6"): tus_bas("6")
    if st.button("3"): tus_bas("3")
    if st.button("00"): tus_bas("00")

with col4:
    if st.button("÷"): tus_bas("÷")
    if st.button("×"): tus_bas("×")
    if st.button("-"): tus_bas("-")
    if st.button("+"): tus_bas("+")
    # Eşittir butonu ana renkli olsun
    if st.button("=", type="primary"): hesapla()

st.divider()
st.info("💡 **Özellik:** İstediğiniz kadar sayıyı yan yana yazıp işlem yapabilirsiniz. İşlem önceliği otomatik hesaplanır.")
