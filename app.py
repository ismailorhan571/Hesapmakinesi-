import streamlit as st

# Sayfa Ayarları
st.set_page_config(page_title="İsmail Orhan Hesap Makinesi", page_icon="🔢")

# --- GELİŞTİRİCİ KISMI DÜZELTİLMİŞ HALİ ---
# 'renk' yerine 'color' ve 'gri' yerine 'gray' kullanıyoruz
st.markdown("<h4 style='text-align: center; color: gray;'>🚀 Bu program <b>İSMAİL ORHAN</b> tarafından geliştirilmiştir</h4>", unsafe_allow_html=True)

st.title("🔢 Profesyonel Hesap Makinesi")
st.markdown("---")

# Sayı girişleri
s1 = st.number_input("1. Sayı", value=0.0)
s2 = st.number_input("2. Sayı", value=0.0)

islem = st.selectbox("Yapılacak İşlem", ["Toplama (+)", "Çıkarma (-)", "Çarpma (*)", "Bölme (/)"])

st.write("")

if st.button("HESAPLA", use_container_width=True, type="primary"):
    if "Toplama" in islem:
        sonuc = s1 + s2
    elif "Çıkarma" in islem:
        sonuc = s1 - s2
    elif "Çarpma" in islem:
        sonuc = s1 * s2
    elif "Bölme" in islem:
        sonuc = s1 / s2 if s2 != 0 else "Hata: 0'a Bölme!"
    
    st.success(f"### Sonuç: {sonuc}")
    if not isinstance(sonuc, str):
        st.balloons()
