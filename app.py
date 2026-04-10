import streamlit as st

# 1. Sayfa Yapılandırması
st.set_page_config(page_title="İsmail Orhan Pro Calculator", page_icon="🔢", layout="centered")

# 2. Modern Tasarım ve Buton Düzeni (CSS)
st.markdown("""
    <style>
    .stButton>button {
        width: 100%;
        height: 60px;
        font-size: 22px !important;
        font-weight: bold;
        border-radius: 8px;
        margin-bottom: -10px;
    }
    /* Sayı Butonları */
    div[data-testid="stHorizontalBlock"] > div:nth-child(-n+4) button {
        background-color: #f1f3f4;
        color: #202124;
    }
    /* İşlem Butonları (5. Sütun) */
    div[data-testid="stHorizontalBlock"] > div:nth-child(5) button {
        background-color: #fbbc04;
        color: white;
    }
    .display-box {
        background-color: #202124;
        color: #8ab4f8;
        padding: 20px;
        border-radius: 12px;
        font-size: 45px;
        text-align: right;
        font-family: 'Consolas', monospace;
        margin-bottom: 20px;
        border: 2px solid #3c4043;
        min-height: 80px;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Hesap Makinesi Mantığı (Session State)
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
        # Matematiksel işlemleri Python diline çevir
        islem = st.session_state.ifade.replace('×', '*').replace('÷', '/')
        sonuc = eval(islem)
        if sonuc == int(sonuc): sonuc = int(sonuc)
        st.session_state.ifade = str(sonuc)
    except:
        st.session_state.ifade = "Hata"

# 4. Arayüz Başlığı
st.markdown("<h2 style='text-align: center;'>🔢 Pro Hesap Makinesi</h2>", unsafe_allow_html=True)
st.caption(f"<p style='text-align: center;'>Geliştirici: <b>İsmail Orhan</b></p>", unsafe_allow_html=True)

# Dijital Ekran
st.markdown(f'<div class="display-box">{st.session_state.ifade if st.session_state.ifade else "0"}</div>', unsafe_allow_html=True)

# 5. BUTON GRIDİ (Tam 5 Sütunlu Yapı)
c1, c2, c3, c4, c5 = st.columns(5)

# 1. SATIR
with c1: st.button("7", on_click=ekle, args=("7",))
with c2: st.button("8", on_click=ekle, args=("8",))
with c3: st.button("9", on_click=ekle, args=("9",))
with c4: st.button("AC", on_click=temizle)
with c5: st.button("÷", on_click=ekle, args=("÷",))

# 2. SATIR
with c1: st.button("4", on_click=ekle, args=("4",))
with c2: st.button("5", on_click=ekle, args=("5",))
with c3: st.button("6", on_click=ekle, args=("6",))
with c4: st.button("DEL", on_click=sil)
with c5: st.button("×", on_click=ekle, args=("×",))

# 3. SATIR
with c1: st.button("1", on_click=ekle, args=("1",))
with c2: st.button("2", on_click=ekle, args=("2",))
with c3: st.button("3", on_click=ekle, args=("3",))
with c4: st.button("%", on_click=ekle, args=("/100",))
with c5: st.button("-", on_click=ekle, args=("-",))

# 4. SATIR
with c1: st.button("0", on_click=ekle, args=("0",))
with c2: st.button("00", on_click=ekle, args=("00",))
with c3: st.button(".", on_click=ekle, args=(".",))
with c4: st.button("=", on_click=hesapla, type="primary")
with c5: st.button("+", on_click=ekle, args=("+",))

st.divider()
st.info("💡 **Profesyonel Kullanım:** İstediğiniz kadar sayıyı yan yana yazabilirsiniz. İşlem önceliği (çarpma/bölme önce yapılır) otomatik olarak dikkate alınır.")
