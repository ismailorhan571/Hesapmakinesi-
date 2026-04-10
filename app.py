import streamlit as st
import streamlit.components.v1 as components

# 1. Sayfa Ayarları
st.set_page_config(page_title="İsmail Stili Hesap Makinesi", page_icon="🦁", layout="centered")

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
        
        <div class="grid">
            <button class="spec" onclick="add('**')">xʸ</button>
            <button class="spec" onclick="sqrt()">√x</button>
            <button class="spec" onclick="add('**2')">x²</button>
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
            <button class="num" onclick="add('%')">%</button>
            <button class="op" onclick="add('-')">−</button>
            
            <button class="num" onclick="add('1')">1</button>
            <button class="num" onclick="add('2')">2</button>
            <button class="num" onclick="add('3')">3</button>
            <button class="num" onclick="add('.')">.</button>
            <button class="op" onclick="add('+')">+</button>
            
            <button class="num" style="grid-column: span 2; border-radius: 30px;" onclick="add('0')">0</button>
            <button style="visibility: hidden;"></button>
            <button class="equal" style="grid-column: span 2; border-radius: 30px;" onclick="calc()">=</button>
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
        function sqrt() { try { disp.value = Math.sqrt(eval(disp.value)).toFixed(2); } catch { disp.value = 'Hata'; } }
        function calc() {
            try { 
                let res = eval(disp.value);
                disp.value = Number.isInteger(res) ? res : res.toFixed(4);
            }
            catch { disp.value = 'Hata'; }
        }
    </script>
</body>
</html>
"""

# 3. Arayüz Başlığı
st.markdown("<h2 style='text-align: center; color: #FDB912; text-shadow: 0 0 10px #E30613;'>🦁 GALATASARAY HESAP MAKİNESİ 🦁 </h2>", unsafe_allow_html=True)

# 4. Hesap Makinesi
components.html(calc_html, height=480)

# 5. Alt İmza (Senin İstediğin Şekilde)
st.markdown("<h3 style='text-align: center; color: white; margin-top: 0;'>Geliştiren: İsmail Orhan</h3>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #888; font-size: 14px;'>🦁 Bursa / Gemlik - Şampiyonun Hesap Makinesi İSMAİL ORHAN </p>", unsafe_allow_html=True)
