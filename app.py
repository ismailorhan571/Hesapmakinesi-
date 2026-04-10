import streamlit as st
import streamlit.components.v1 as components

# Sayfa Ayarları
st.set_page_config(page_title="Pro Calculator", page_icon="🔢", layout="centered")

# --- HESAP MAKİNESİ HTML & JS KODU ---
calc_html = """
<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <style>
        body { background-color: #000; font-family: -apple-system, sans-serif; display: flex; justify-content: center; padding-top: 20px; }
        .calc-body { width: 320px; background-color: #000; border-radius: 20px; padding: 10px; }
        #display {
            width: 100%; height: 80px; background: #000; color: white;
            text-align: right; font-size: 50px; border: none; margin-bottom: 20px; outline: none;
        }
        .grid { display: grid; grid-template-columns: repeat(5, 1fr); gap: 10px; }
        button {
            height: 55px; width: 55px; border-radius: 50%; border: none;
            font-size: 18px; font-weight: bold; cursor: pointer; transition: 0.2s;
        }
        button:active { opacity: 0.7; }
        .num { background-color: #333; color: white; }
        .op { background-color: #ff9500; color: white; }
        .func { background-color: #a5a5a5; color: black; }
        .special { background-color: #333; color: white; font-size: 14px; }
    </style>
</head>
<body>
    <div class="calc-body">
        <input type="text" id="display" value="0" disabled>
        <div class="grid">
            <button class="num" onclick="add('7')">7</button>
            <button class="num" onclick="add('8')">8</button>
            <button class="num" onclick="add('9')">9</button>
            <button class="func" onclick="cls()">AC</button>
            <button class="op" onclick="add('/')">÷</button>
            
            <button class="num" onclick="add('4')">4</button>
            <button class="num" onclick="add('5')">5</button>
            <button class="num" onclick="add('6')">6</button>
            <button class="func" onclick="del()">DEL</button>
            <button class="op" onclick="add('*')">×</button>
            
            <button class="num" onclick="add('1')">1</button>
            <button class="num" onclick="add('2')">2</button>
            <button class="num" onclick="add('3')">3</button>
            <button class="special" onclick="add('/100')">%</button>
            <button class="op" onclick="add('-')">−</button>
            
            <button class="num" onclick="add('0')">0</button>
            <button class="num" onclick="add('00')">00</button>
            <button class="num" onclick="add('.')">.</button>
            <button class="op" style="background-color: #fff; color: #000;" onclick="calc()">=</button>
            <button class="op" onclick="add('+')">+</button>
        </div>
    </div>

    <script>
        let disp = document.getElementById('display');
        function add(v) { 
            if(disp.value == '0' || disp.value == 'Hata') disp.value = v;
            else disp.value += v;
        }
        function cls() { disp.value = '0'; }
        function del() { disp.value = disp.value.slice(0,-1); if(disp.value=='') disp.value='0'; }
        function calc() {
            try { disp.value = eval(disp.value); }
            catch { disp.value = 'Hata'; }
        }
    </script>
</body>
</html>
"""

# Arayüzü Başlat
st.markdown("<h2 style='text-align: center;'>Pro Calculator</h2>", unsafe_allow_html=True)
components.html(calc_html, height=500)
st.caption("<p style='text-align: center;'>Geliştirici: İsmail Orhan</p>", unsafe_allow_html=True)
