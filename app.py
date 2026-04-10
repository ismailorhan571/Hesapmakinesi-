import streamlit as st
import streamlit.components.v1 as components

# Sayfa Ayarları (Galatasaray renklerini tema olarak alalım)
st.set_page_config(
    page_title="İsmail Stili Pro",
    page_icon="🔢",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# --- GALATASARAY ÖZEL HTML & JS KODU ---
calc_html = """
<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <style>
        body { background-color: #000; font-family: -apple-system, sans-serif; display: flex; justify-content: center; padding-top: 10px; overflow: hidden; }
        .calc-body { width: 330px; background-color: #000; border-radius: 20px; padding: 10px; position: relative; }
        
        /* Galatasaray Arması */
        .gs-logo {
            position: absolute; top: 10px; right: 10px;
            width: 40px; height: 40px;
            background-image: url('https://upload.wikimedia.org/wikipedia/en/thumb/4/49/Galatasaray_SK_football_logo.png/960px-Galatasaray_SK_football_logo.png');
            background-size: contain; background-repeat: no-repeat;
            border-radius: 50%;
            box-shadow: 0 0 10px rgba(255, 215, 0, 0.7), 0 0 20px rgba(255, 0, 0, 0.5);
            z-index: 100;
        }

        #display {
            width: 100%; height: 70px; background: #000; color: white;
            text-align: right; font-size: 40px; border: none; margin-bottom: 15px; outline: none;
        }
        .grid { display: grid; grid-template-columns: repeat(5, 1fr); gap: 8px; }
        button {
            height: 58px; width: 58px; border-radius: 50%; border: none;
            font-size: 16px; font-weight: bold; cursor: pointer; transition: 0.2s;
            display: flex; justify-content: center; align-items: center;
        }
        button:active { opacity: 0.6; }
        
        /* Sayı Butonları (Koyu Gri - Net Okunurluk) */
        .num { background-color: #333; color: white; }
        
        /* İşlem Butonları (KIRMIZI - Galatasaray) */
        .op { background-color: #FF0000; color: white; }
        
        /* Fonksiyon Butonları (SARI - Galatasaray) */
        .func { background-color: #FFD700; color: black; }
        
        /* Özel Fonksiyonlar (Üs, Kök) - Sarı Kenarlı */
        .spec { background-color: #1a1a1a; color: #FFD700; font-size: 14px; border: 1px solid #444; }
        .spec:active { border-color: #FFD700; }
        
        .equal { background-color: #FFFFFF; color: #000; font-size: 24px; }
    </style
