import streamlit as st
import streamlit.components.v1 as components

# Page Configuration
st.set_page_config(page_title="The Endless Cookie Trap", page_icon="🍪", layout="wide")

st.title("🍪 The Ultimate Cookie Trap")
st.write("Try to browse the web. I dare you.")

# Embedded HTML/JS Interactive Prank App
prank_html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <style>
        body {
            margin: 0;
            padding: 0;
            background-color: #0f172a;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            height: 100vh;
            overflow: hidden;
            display: flex;
            justify-content: center;
            align-items: center;
        }

        /* Popup Cookie Box */
        .cookie-box {
            position: absolute;
            width: 340px;
            padding: 25px;
            border-radius: 12px;
            box-shadow: 0 10px 25px rgba(0,0,0,0.5);
            color: #fff;
            text-align: center;
            transition: transform 0.3s ease, opacity 0.3s ease;
            z-index: 100;
        }

        .cookie-box h3 { margin-top: 0; font-size: 20px; }
        .cookie-box p { font-size: 14px; margin-bottom: 20px; opacity: 0.9; }

        .btn-group {
            display: flex;
            justify-content: space-around;
        }

        .cookie-btn {
            padding: 10px 18px;
            border: none;
            border-radius: 6px;
            font-weight: bold;
            cursor: pointer;
            font-size: 14px;
            transition: transform 0.1s;
        }

        .cookie-btn:active { transform: scale(0.95); }
        .accept-btn { background-color: #22c55e; color: white; }
        .reject-btn { background-color: #ef4444; color: white; }

        /* Explosion Effect */
        @keyframes explode {
            0% { transform: scale(1) rotate(0deg); opacity: 1; }
            100% { transform: scale(2) rotate(45deg); opacity: 0; }
        }
        .exploding {
            animation: explode 0.4s forwards ease-out;
        }

        /* CAPTCHA Screen */
        #captcha-container {
            display: none;
            background: #ffffff;
            color: #333;
            width: 380px;
            padding: 30px;
            border-radius: 8px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.4);
            text-align: center;
            z-index: 200;
        }

        .captcha-grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 8px;
            margin: 20px 0;
        }

        .captcha-tile {
            height: 90px;
            background: #e2e8f0;
            border-radius: 4px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 28px;
            cursor: pointer;
            border: 2px solid transparent;
        }

        .captcha-tile.selected {
            border-color: #3b82f6;
            background: #dbeafe;
        }

        .verify-btn {
            background: #3b82f6;
            color: white;
            border: none;
            padding: 10px 20px;
            font-weight: bold;
            border-radius: 4px;
            cursor: pointer;
            width: 100%;
        }

        /* Google Spin & Crash */
        #google-container {
            display: none;
            font-size: 72px;
            font-weight: 900;
            letter-spacing: 4px;
            z-index: 300;
            text-align: center;
        }

        @keyframes spinSequence {
            0% { transform: rotate(0deg); }
            50% { transform: rotate(360deg); }
            100% { transform: rotate(0deg); }
        }

        .spinning {
            animation: spinSequence 3s ease-in-out forwards;
        }

        /* Fake Blue Screen of Death (BSOD) */
        #bsod {
            display: none;
            position: fixed;
            top: 0; left: 0; width: 100vw; height: 100vh;
            background: #0078d7;
            color: white;
            font-family: 'Courier New', Courier, monospace;
            padding: 80px;
            box-sizing: border-box;
            z-index: 999;
        }

        #bsod h1 { font-size: 72px; margin-bottom: 20px; }
        #bsod p { font-size: 22px; line-height: 1.5; }
    </style>
</head>
<body>

    <!-- Cookie Popup Box -->
    <div id="cookie-popup" class="cookie-box">
        <h3 id="cookie-title">🍪 Cookie Consent Required</h3>
        <p id="cookie-desc">We use 4,000 trackers to monitor your clicks. Do you accept our terms?</p>
        <div class="btn-group">
            <button class="cookie-btn accept-btn" onclick="handleCookieClick()">Accept All</button>
            <button class="cookie-btn reject-btn" onclick="handleCookieClick()">Reject</button>
        </div>
    </div>

    <!-- CAPTCHA Screen -->
    <div id="captcha-container">
        <h3 id="captcha-header">Security Check</h3>
        <p>Select all squares with a <b>Cat</b> (Progress: <span id="captcha-progress">0</span>/5)</p>
        <div class="captcha-grid" id="grid"></div>
        <button class="verify-btn" onclick="verifyCaptcha()">Verify</button>
    </div>

    <!-- GOOGLE Spinning Text -->
    <div id="google-container">
        <span style="color: #4285F4;">G</span><span style="color: #EA4335;">O</span><span style="color: #FBBC05;">O</span><span style="color: #4285F4;">G</span><span style="color: #34A853;">L</span><span style="color: #EA4335;">E</span>
    </div>

    <!-- Fake BSOD Crash Screen -->
    <div id="bsod">
        <h1>:(</h1>
        <p>Your PC ran into a problem and needs to restart. We're just collecting some error info, and then we'll restart for you.</p>
        <p style="margin-top: 40px;"><strong>100% complete</strong></p>
        <p style="font-size: 16px; margin-top: 60px;">Stop code: CRITICAL_PRANK_FAILURE</p>
    </div>

    <script>
        let clickCount = 0;
        let captchaSuccessCount = 0;
        const colors = ['#1e293b', '#7c2d12', '#14532d', '#312e81', '#581c87', '#831843'];

        function getRandomColor() {
            return colors[Math.floor(Math.random() * colors.length)];
        }

        function movePopupRandomly() {
            const popup = document.getElementById('cookie-popup');
            const maxX = window.innerWidth - 360;
            const maxY = window.innerHeight - 220;
            const randomX = Math.floor(Math.random() * Math.max(10, maxX));
            const randomY = Math.floor(Math.random() * Math.max(10, maxY));
            
            popup.style.left = randomX + 'px';
            popup.style.top = randomY + 'px';
            popup.style.backgroundColor = getRandomColor();
        }

        function handleCookieClick() {
            const popup = document.getElementById('cookie-popup');
            popup.classList.add('exploding');
            clickCount++;

            setTimeout(() => {
                popup.classList.remove('exploding');
                if (clickCount < 5) {
                    movePopupRandomly();
                } else {
                    // Switch to CAPTCHA mode after 5 clicks
                    popup.style.display = 'none';
                    showCaptcha();
                }
            }, 400);
        }

        // Initialize first position
        movePopupRandomly();

        // CAPTCHA Logic
        const emojis = ['🐱', '🐶', '🚗', '🍕', '🐱', '🌳', '🐱', '🚲', '🍔'];
        function showCaptcha() {
            document.getElementById('captcha-container').style.display = 'block';
            generateNewGrid();
        }

        function generateNewGrid() {
            const grid = document.getElementById('grid');
            grid.innerHTML = '';
            for (let i = 0; i < 9; i++) {
                const tile = document.createElement('div');
                tile.className = 'captcha-tile';
                tile.innerText = emojis[Math.floor(Math.random() * emojis.length)];
                tile.onclick = function() {
                    tile.classList.toggle('selected');
                };
                grid.appendChild(tile);
            }
        }

        function verifyCaptcha() {
            captchaSuccessCount++;
            document.getElementById('captcha-progress').innerText = captchaSuccessCount;

            if (captchaSuccessCount < 5) {
                generateNewGrid();
            } else {
                // Success! Hide CAPTCHA and show GOOGLE spin
                document.getElementById('captcha-container').style.display = 'none';
                triggerGoogleSpin();
            }
        }

        function triggerGoogleSpin() {
            const googleDiv = document.getElementById('google-container');
            googleDiv.style.display = 'block';
            googleDiv.classList.add('spinning');

            // After 3 seconds (spin completes), crash the page
            setTimeout(() => {
                googleDiv.style.display = 'none';
                document.getElementById('bsod').style.display = 'block';
            }, 3000);
        }
    </script>
</body>
</html>
"""

# Render the interactive HTML app inside Streamlit
components.html(prank_html, height=650)