import streamlit as st
import streamlit.components.v1 as components

# Sayfa Ayarları
st.set_page_config(page_title="İsmail Stili", page_icon="🔢", layout="centered")

# --- HESAP MAKİNESİ HTML & JS KODU ---
calc_html = """
<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <style>
        body { background-color: #000; font-family: -apple-system, sans-serif; display: flex; justify-content: center; padding-top: 10px; }
        .calc-body { width: 330px; background-color: #000; border-radius: 20px; padding: 10px; }
        #display {
            width: 100%; height: 70px; background: #000; color: white;
            text-align: right; font-size: 40px; border: none; margin-bottom: 15px; outline: none;
        }
        .grid { display: grid; grid-template-columns: repeat(5, 1fr); gap: 8px; }
        button {
            height: 58px; width: 58px; border-radius: 50%; border: none;
            font-size: 16px; font-weight: bold; cursor: pointer; transition: 0.2s;
        }
        button:active { opacity: 0.6; }
        
        /* Sayı Butonları (Koyu Gri Kalsın, Okunurluk İçin) */
        .num { background-color: #333; color: white; }
        
        /* İşlem Butonları (Turuncu yerine KIRMIZI) */
        .op { background-color: #FF0000; color: white; }
        
        /* Fonksiyon Butonları (Gri yerine SARI) */
        .func { background-color: #FFD700; color: black; }
        
        /* Özel Fonksiyonlar (Üs ve Kök) */
        .spec { background-color: #222; color: #FFD700; font-size: 14px; border: 1px solid #444; }
        
        .equal { background-color: #FFFFFF; color: #000; font-size: 24px; }
    </style>
</head>
<body>
    <div class="calc-body">
        <input type="text" id="display" value="0" disabled>
        <div class="grid">
            <button class="spec" onclick="add('**')">xʸ</button>
            <button class="spec" onclick="sqrt()">√</button>
            <button class="spec" onclick="add('%')">%</button>
            <button class="func" onclick="cls()">AC</button>
            <button class="op" onclick="add('/')">÷</button>
            
            <button class="num" onclick="add('7')">7</button>
            <button class="num" onclick="add('8')">8</button>
            <button class="num" onclick="add('9')">9</button>
            <button class="func" onclick="del()">DEL</button>
            <button class="op" onclick="add('*')">×</button>
            
            <button class="num" onclick="add('4')">4</button>
            <button class="num" onclick="add('5')">5</button>
            <button class="num" onclick="add('6')">6</button>
            <button class="num" onclick="add('00')">00</button>
            <button class="op" onclick="add('-')">−</button>
            
            <button class="num" onclick="add('1')">1</button>
            <button class="num" onclick="add('2')">2</button>
            <button class="num" onclick="add('3')">3</button>
            <button class="num" onclick="add('.')">.</button>
            <button class="op" onclick="add('+')">+</button>
            
            <button class="num" style="grid-column: span 2; width: 125px; border-radius: 30px;" onclick="add('0')">0</button>
            <button class="num"
