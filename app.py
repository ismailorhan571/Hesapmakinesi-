import streamlit as st
import streamlit.components.v1 as components

# 1. Sayfa Ayarları
st.set_page_config(page_title="İsmail Stili Pro", page_icon="🦁", layout="centered")

# 2. HTML ve JS Kodu
calc_html = """
<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <style>
        body { background-color: #000; font-family: -apple-system, sans-serif; display: flex; justify-content: center; padding-top: 5px; overflow: hidden; margin: 0; }
        .calc-body { width: 330px; background-color: #000; border-radius: 20px; padding: 10px; position: relative; }
        
        /* LOGO: Çerçevesiz ve Sol Üstte Tam Konumlanmış */
        .gs-logo {
            position: absolute; top: 10px; left: 10px;
            width: 55px; height: 55px;
            background-image: url('https://upload.wikimedia.org/wikipedia/en/thumb/4/49/Galatasaray_SK_football_logo.png/960px-Galatasaray_SK_football_logo.png');
            background-size: contain; background-repeat: no-repeat;
            z-index: 100;
        }

        #display {
            width: 100%; height: 85px; background: #000; color: white;
            text-align: right; font-size: 48px; border: none; margin-bottom: 10px; outline: none;
            padding-right: 10px; box-sizing: border-box;
        }
        .grid { display: grid; grid-template-columns: repeat(5, 1fr); gap: 8px; }
        button {
            height: 58px; width: 100%; border-radius: 50%; border: none;
            font-size: 16px; font-weight: bold; cursor: pointer; transition: 0.1s;
            display: flex; justify-content: center; align-items: center;
        }
        button:active { opacity: 0.6; transform: scale(0.92); }
        
        /* Renkler */
        .num { background-color: #333333; color: white; }
        .op { background-color: #E30613; color: white; font-size: 22px; } 
        .func { background-color: #FDB912; color: black; font-size: 18px; } 
        .spec { background-color: #1a1a1a; color: #FDB912; font-size: 14px; border: 1px solid #444; }
        .equal { background-color: #FFFFFF; color: #000; font-size: 24px; }
    </style>
</head>
<body>
    <div class="calc-body">
        <div class="gs-logo"></div>
        <input type="text" id="display" value="0" disabled>
