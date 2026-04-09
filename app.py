# app.py - Versión Árbol Realista con Copa de Corazón y Fondo Azul
from flask import Flask
import os

app = Flask(__name__)

html_content = """
<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Nuestro Árbol del Corazón Realista 💖</title>

<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&family=Playfair+Display:ital,wght@1,400&family=Poppins:wght@300;600&display=swap" rel="stylesheet">

<style>
    body {
        margin: 0;
        height: 100vh;
        display: flex;
        align-items: center;
        justify-content: center;
        /* --- FONDO AZULITO --- */
        background: linear-gradient(135deg, #a7d8f5 0%, #d8effb 100%); 
        overflow: hidden;
        position: relative;
    }

    /* --- NUBES EN FORMA DE CORAZÓN (SVG) --- */
    .nube-corazon {
        position: absolute;
        width: 150px;
        height: 150px;
        opacity: 0.5; /* Suave */
        animation: moverNubes 60s linear infinite;
        z-index: 1;
    }
    .nube-corazon path {
        fill: white;
    }

    @keyframes moverNubes {
        0% { transform: translateX(-150px); }
        100% { transform: translateX(calc(100vw + 150px)); }
    }

    .container {
        display: flex;
        flex-direction: column;
        align-items: center;
        width: 100%;
        max-width: 600px;
        position: relative;
        z-index: 5; /* Por encima de las nubes y la lluvia */
    }

    /* --- EL ÁRBOL Y LA COPA DE CORAZÓN --- */
    .tree-container {
        position: relative;
        width: 500px; /* Un poco más ancho para la copa grande */
        height: 550px;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: flex-end;
    }

    /* TRONCO Y RAMAS REALISTAS (SVG) */
    .tree-svg {
        position: absolute;
        bottom: 0;
        left: 50%;
        transform: translateX(-50%);
        width: 100%;
        height: 100%;
        z-index: 2;
        opacity: 0;
        animation: fadeIn 2s ease-in forwards;
        animation-delay: 0.5s;
    }
    .tree-svg path {
        fill: #5D4037; /* Color café más realista */
    }

    /* COPA DEL ÁRBOL EN FORMA DE CORAZÓN */
    .tree-top {
        position: absolute;
        top: 20px; /* Cerca del final de las ramas */
        width: 450px; /* Copa grande */
        height: 450px;
        /* background-color: rgba(255, 0, 0, 0.1); */ /* Descomenta para ver el área */
    }

    /* CORAZÓN INDIVIDUAL (Copa) */
    .heart-tree {
        position: absolute;
        width: 18px; /* Un poco más pequeños para definición */
        height: 18px;
        background: #ff0055;
        transform: rotate(-45deg) scale(0);
        opacity: 0;
        animation: heartGrow 1.5s ease-out forwards;
    }
    .heart-tree::before, .heart-tree::after {
        content: '';
        position: absolute;
        width: 18px;
        height: 18px;
        background: inherit;
        border-radius: 50%;
    }
    .heart-tree::before { top: -9px; left: 0; }
    .heart-tree::after { left: 9px; top: 0; }

    /* --- LLUVIA DE CORAZONES DESDE ARRIBA --- */
    .heart-rain {
        position: absolute;
        width: 12px;
        height: 12px;
        background: #ff0055;
        transform: rotate(-45deg);
        opacity: 0.6;
        animation: heartRainFall linear forwards;
        z-index: 3;
    }
    .heart-rain::before, .heart-rain::after {
        content: '';
        position: absolute;
        width: 12px;
        height: 12px;
        background: inherit;
        border-radius: 50%;
    }
    .heart-rain::before { top: -6px; left: 0; }
    .heart-rain::after { left: 6px; top: 0; }

    /* --- TEXTO CON MENSAJE --- */
    .text-overlay {
        color: #333; /* Color oscuro para el fondo azul */
        margin-top: -30px; /* Un poco más cerca del árbol */
        text-align: center;
        opacity: 0;
        transition: opacity 2s ease-in;
        font-family: 'Poppins', sans-serif;
        z-index: 10;
        width: 100%;
    }

    .text-overlay.visible { opacity: 1; }

    .text-overlay h2 {
        font-family: 'Dancing Script', cursive;
        font-size: 2.8rem;
        margin: 0;
    }

    .special-message {
        font-family: 'Playfair Display', serif;
        font-style: italic;
        font-size: 1.3rem;
        color: #666; /* Gris suave */
        margin: 15px 0;
        line-height: 1.5;
    }

    #time { font-size: 1.1rem; font-weight: 300; margin-top: 10px; }

    /* --- ANIMACIONES --- */
    @keyframes fadeIn {
        from { opacity: 0; transform: translate(-50%, 20px); }
        to { opacity: 1; transform: translate(-50%, 0); }
    }
    @keyframes heartGrow {
        0% { transform: rotate(-45deg) scale(0); opacity: 0; }
        100% { transform: rotate(-45deg) scale(1); opacity: 0.95; }
    }
    @keyframes heartRainFall {
        0% { transform: translateY(-50px) rotate(-45deg); opacity: 0.6; }
        100% { transform: translateY(110vh) rotate(-45deg); opacity: 0; }
    }
</style>
</head>
<body>

<svg class="nube-corazon" style="top: 5vh; animation-delay: 0s;" viewBox="0 0 512 512">
    <path d="M462.3 62.6C407.5 15.9 326 24.3 275.7 76.2L256 96.5l-19.7-20.3C186.1 24.3 104.5 15.9 49.7 62.6c-62.8 53.6-66.1 149.8-9.9 207.9l193.5 199.8c12.5 12.9 32.8 12.9 45.3 0l193.5-199.8c56.3-58.1 53-154.3-9.8-207.9z"/>
</svg>
<svg class="nube-corazon" style="top: 25vh; animation-delay: -20s; width: 100px; height: 100px;" viewBox="0 0 512 512">
    <path d="M462.3 62.6C407.5 15.9 326 24.3 275.7 76.2L256 96.5l-19.7-20.3C186.1 24.3 104.5 15.9 49.7 62.6c-62.8 53.6-66.1 149.8-9.9 207.9l193.5 199.8c12.5 12.9 32.8 12.9 45.3 0l193.5-199.8c56.3-58.1 53-154.3-9.8-207.9z"/>
</svg>
<svg class="nube-corazon" style="top: 15vh; animation-delay: -40s; width: 80px; height: 80px;" viewBox="0 0 512 512">
    <path d="M462.3 62.6C407.5 15.9 326 24.3 275.7 76.2L256 96.5l-19.7-20.3C186.1 24.3 104.5 15.9 49.7 62.6c-62.8 53.6-66.1 149.8-9.9 207.9l193.5 199.8c12.5 12.9 32.8 12.9 45.3 0l193.5-199.8c56.3-58.1 53-154.3-9.8-207.9z"/>
</svg>

<div class="container">
    <div class="tree-container">
        <svg class="tree-svg" viewBox="0 0 600 600" preserveAspectRatio="xMidYMid meet">
            <path d="M300,580 C290,500 280,480 270,450 S250,400 240,380 C230,360 210,340 180,330 S150,300 130,280 C110,260 90,230 100,200 C110,170 140,150 170,160 S200,190 220,210 C240,230 260,250 280,260 C300,270 320,260 340,250 C360,240 380,220 400,200 C420,180 440,160 470,170 C500,180 520,210 510,240 C500,270 480,290 460,310 S430,330 400,340 C370,350 350,370 340,390 C330,410 320,440 310,470 S305,520 300,580 Z M320,280 C330,270 340,260 350,250 S370,230 390,220 C410,210 430,190 450,200 S470,220 460,240 C450,260 430,280 410,290 S390,300 370,310 C350,320 330,300 320,280 Z M280,280 C270,270 260,260 250,250 S230,230 210,220 C190,210 170,190 150,200 S130,220 140,240 C150,260 170,280 190,290 S210,300 230,310 C250,320 270,300 280,280 Z"/>
        </svg>
        <div class="tree-top" id="tree-top"></div>
    </div>
    <div class="text-overlay" id="text-overlay">
        <h2>Nuestra historia... 💖</h2>
        <div class="special-message">
            para el amor de mi vida:<br>
            si pudiera elegir un lugar, seria a tu lado.<br>
            Cuanto mas tiempo estoy contigo mas te amo.
        </div>
        <div id="time"></div>
    </div>
</div>

<script>
    const treeTop = document.getElementById('tree-top');
    const textOverlay = document.getElementById('text-overlay');
    const colors = ['#ff0033', '#ff0055', '#ff3377', '#ff6699', '#fb6f92'];

    const TOTAL_HEARTS = 380; // Más corazones para una copa muy frondosa
    const TEXT_DELAY_MS = 32000; // Un poco más de tiempo para el árbol
    let heartsCreated = 0;

    // --- GEOMETRÍA DEL CORAZÓN (Fórmula Paramétrica) ---
    const a = 14; // Escala del corazón
    
    // Función para obtener las coordenadas X e Y en forma de corazón
    function getHeartPoint(t) {
        // Fórmula matemática del corazón (ajustada para que esté boca arriba)
        let x = a * (16 * Math.pow(Math.sin(t), 3));
        let y = -a * (13 * Math.cos(t) - 5 * Math.cos(2 * t) - 2 * Math.cos(3 * t) - Math.cos(4 * t));
        return { x, y };
    }

    function createTreeHeart() {
        if (heartsCreated >= TOTAL_HEARTS) {
            clearInterval(heartInterval);
            return;
        }

        const heart = document.createElement('div');
        heart.classList.add('heart-tree');
        
        // --- POSICIONAMIENTO DENTRO DEL CORAZÓN ---
        // 't' va de 0 a 2*PI para trazar el perímetro
        const t = Math.random() * Math.PI * 2; 
        const pointPerimetro = getHeartPoint(t);
        
        // Para rellenar el interior, multiplicamos por un factor aleatorio (0 a 1)
        // Usamos Math.sqrt para una distribución más uniforme en el centro
        const randomFactor = Math.sqrt(Math.random()); 
        
        // Centro de la copa (.tree-top)
        const centerX = 225; 
        const centerY = 200; // Ajustado para que el centro del corazón esté bien ubicado

        // Coordenadas Finales
        const x = centerX + pointPerimetro.x * randomRadiusFactor; // Usamos un factor menor (0.9) para no tocar el borde perfecto
        // En el eje Y, el progreso (heartsCreated) nos ayuda a "nacer desde abajo"
        const progressY = heartsCreated / TOTAL_HEARTS;
        // yRelativa va de baseY (radius) a -radius. Usamos Math.pow para subir rápido al principio.
        const baseY = centerY + (a * 17); // Punto más bajo del corazón
        const heightY = (a * 34); // Altura total
        const actualY = baseY - (heightY * Math.pow(progressY, 0.8)); // Crecimiento progresivo

        // Ahora acotamos X según esta Y (x² = r² - y²) - para que sea redondo perfecto
        const yRelativaCentro = actualY - centerY;
        const maxRadiusX = Math.sqrt(Math.pow(maxCopaRadius, 2) - Math.pow(yRelativaCentro, 2));
        
        // Si maxRadiusX no es un número (Y fuera del radio), no dibujamos
        if (isNaN(maxRadiusX)) {
             heartsCreated++; // Incrementamos para no quedarnos atascados
             return;
        }

        const randomRadiusX = Math.random() * maxRadiusX; 
        const angle = Math.random() * Math.PI * 2;
        
        const finalX = centerX + Math.cos(angle) * randomRadiusX;
        const finalY = actualY;

        heart.style.left = `${finalX - 9}px`; // Centramos el corazón (9px is half of 18px)
        heart.style.top = `${finalY - 9}px`;
        heart.style.backgroundColor = colors[Math.floor(Math.random() * colors.length)];
        
        const size = Math.random() * 8 + 14; // Variación de tamaño para naturalidad
        heart.style.width = `${size}px`;
        heart.style.height = `${size}px`;

        treeTop.appendChild(heart);
        heartsCreated++;
    }

    function createRainHeart() {
        const heart = document.createElement('div');
        heart.classList.add('heart-rain');
        heart.style.left = Math.random() * 100 + 'vw';
        heart.style.backgroundColor = colors[Math.floor(Math.random() * colors.length)];
        const fallDuration = Math.random() * 3 + 4;
        heart.style.animationDuration = `${fallDuration}s`;
        document.body.appendChild(heart);
        setTimeout(() => heart.remove(), fallDuration * 1000);
    }

    setTimeout(() => {
        const heartInterval = setInterval(createTreeHeart, 80); // Un corazón cada 80ms
    }, 2500); // Esperamos 2.5s para que se muestre el tronco realista

    setInterval(createRainHeart, 450); // Un corazón de lluvia cada 450ms

    setTimeout(() => {
        textOverlay.classList.add('visible');
    }, TEXT_DELAY_MS);

    const startDate = new Date("2025-01-01T00:00:00");
    function updateCounter() {
        const now = new Date();
        const diff = now - startDate;
        const d = Math.floor(diff / (1000 * 60 * 60 * 24));
        const h = Math.floor((diff / (1000 * 60 * 60)) % 24);
        const m = Math.floor((diff / (1000 * 60)) % 60);
        const s = Math.floor((diff / 1000) % 60);
        document.getElementById('time').innerHTML = `Juntos hace: ${d}d ${h}h ${m}m ${s}s`;
    }
    setInterval(updateCounter, 1000);
    updateCounter();
</script>

</body>
</html>
"""

@app.route('/')
def home():
    return html_content

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
