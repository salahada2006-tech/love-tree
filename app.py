# app.py final con tronco realista, copa de corazón y texto rápido/legible

from flask import Flask
import os

app = Flask(__name__)

# Diseño definitivo del "Árbol del Amor Progressivo y Legible con Mensaje"
html_content = """
<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Nuestro Árbol del Amor con Mensaje Especial 💖</title>

<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@1,400&display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;600&display=swap" rel="stylesheet">

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
    }

    .container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: flex-start;
        width: 100%;
        max-width: 600px; /* Un poco más ancho para el árbol realista */
        position: relative;
    }

    /* EL ÁRBOL - Contenedor Principal */
    .tree-container {
        position: relative;
        width: 400px; /* Ancho para el tronco con ramas */
        height: 500px; /* Alto del árbol */
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: flex-end; /* Tronco abajo */
    }

    /* --- TRONCO CON RAMAS REALISTAS (SVG) --- */
    .tree-svg {
        position: absolute;
        bottom: 0;
        left: 50%;
        transform: translateX(-50%);
        width: 100%;
        height: 100%;
        z-index: 2; /* Por encima de la copa invisible */
        opacity: 0;
        animation: fadeInTree 2s ease-in forwards;
        animation-delay: 0.5s; /* Aparece primero */
    }
    .tree-svg path {
        fill: #5D4037; /* Color café más realista */
    }

    /* COPA DEL ÁRBOL - Contenedor invisible al inicio (SOBRE EL TRONCO) */
    .tree-top {
        position: absolute;
        bottom: 95px; /* Un poco sobre el tronco */
        width: 300px; /* Diámetro de la copa */
        height: 300px; /* Altura de la copa (esférica) */
        z-index: 1; /* Los corazones aparecen entre las ramas */
    }

    /* CORAZÓN INDIVIDUAL (Copa) */
    .heart-tree {
        position: absolute;
        width: 20px;
        height: 20px;
        background: #ff0055;
        transform: rotate(-45deg) scale(0);
        opacity: 0;
        animation: heartGrow 1.5s ease-out forwards;
    }

    .heart-tree::before, .heart-tree::after {
        content: '';
        position: absolute;
        width: 20px;
        height: 20px;
        background: inherit;
        border-radius: 50%;
    }

    .heart-tree::before { top: -10px; left: 0; }
    .heart-tree::after { left: 10px; top: 0; }

    /* CORAZÓN LLUVIA (Por toda la pantalla) */
    .heart-rain {
        position: absolute;
        width: 12px;
        height: 12px;
        background: #ff0055;
        transform: rotate(-45deg);
        opacity: 0.8;
        animation: heartRainFall linear forwards;
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

    /* TEXTO CON MENSAJE ESPECIAL Y CONTADOR - Aparece RÁPIDO */
    .text-overlay {
        color: white; /* Color blanco para el fondo azul */
        margin-top: 10px;
        text-align: center;
        opacity: 0; /* Invisible al inicio */
        text-shadow: 0 0 15px rgba(255, 77, 136, 0.8);
        transition: opacity 1.5s ease-in; /* Transición suave */
        position: relative;
        width: 100%;
        font-family: 'Poppins', sans-serif;
    }

    /* Clase para mostrar el texto al final (Aparece más rápido) */
    .text-overlay.visible {
        opacity: 1;
    }

    /* TÍTULO PRINCIPAL - ¡HACER RESALTAR! */
    .text-overlay h2 {
        font-family: 'Dancing Script', cursive; /* APLICAMOS FUENTE BONITA Y LEGIBLE */
        font-size: 2.8rem;
        font-weight: 700; /* ¡¡NEGRILLA!! para resaltar */
        margin: 0;
        text-shadow: 0 0 10px rgba(0,0,0,0.3); /* Contorno suave para legibilidad */
    }

    /* MENSAJE ESPECIAL - ¡HACER RESALTAR! */
    .special-message {
        font-family: 'Playfair Display', serif; /* FUENTE POÉTICA Y LEGIBLE */
        font-style: italic;
        font-size: 1.4rem; /* Más grande para legibilidad */
        color: #fff; /* Blanco */
        margin: 15px 0;
        line-height: 1.6;
        text-shadow: 0 0 8px rgba(0,0,0,0.2); /* Contorno suave */
    }

    /* CONTADOR - Con fuente legible */
    #time {
        font-size: 1.1rem;
        font-weight: 300;
        margin-top: 15px;
        font-family: 'Poppins', sans-serif;
        color: white;
    }

    /* ANIMACIONES */
    @keyframes fadeInTree {
        from { opacity: 0; transform: translate(-50%, 20px); }
        to { opacity: 1; transform: translate(-50%, 0); }
    }

    @keyframes heartGrow {
        0% { transform: rotate(-45deg) scale(0); opacity: 0; }
        15% { opacity: 1; }
        100% { transform: rotate(-45deg) scale(1); opacity: 0.9; }
    }

    @keyframes heartRainFall {
        0% { transform: translateY(-50px) rotate(-45deg); opacity: 0.8; }
        100% { transform: translateY(110vh) rotate(-45deg); opacity: 0; }
    }
</style>
</head>
<body>

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

    // Configuración de la animación progresiva
    const TOTAL_HEARTS = 300; // Corazones totales para formar el árbol
    const INTERVAL_MS = 100; // Un corazón cada 100ms
    const TEXT_DELAY_MS = 18000; // --- ¡¡TEXTO RÁPIDO!! --- Esperar solo 18 segundos (antes 28)

    let heartsCreated = 0;

    function createTreeHeart() {
        if (heartsCreated >= TOTAL_HEARTS) {
            clearInterval(heartInterval);
            return;
        }

        const heart = document.createElement('div');
        heart.classList.add('heart-tree');
        
        // --- LÓGICA DE DISTRIBUCIÓN ESFÉRICA PERFECTA (COPA REDONDA) ---
        // Radio de la copa (mitad del diámetro de .tree-top)
        const radiusCopa = 150; 
        
        // Lógica de crecimiento ascendente (nace desde abajo)
        const currentProgress = heartsCreated / TOTAL_HEARTS; // Valor de 0 a 1
        
        // 1. Calculamos la altura (Y) progresivamente, pero dentro de la esfera
        const baseY = 280; 
        const heightFactor = 2 * radiusCopa; // Diámetro
        const y_esfera = (baseY - radiusCopa) + radiusCopa - (heightFactor * currentProgress); 

        // 2. Calculamos el Radio X Máximo en esta altura Y (Fórmula de la Esfera)
        const yRelativaCentroEsfera = y_esfera - (baseY - radiusCopa); 
        const maxRadiusX = Math.sqrt(Math.pow(radiusCopa, 2) - Math.pow(yRelativaCentroEsfera, 2));

        // 3. Posicionamiento Aleatorio Circular pero acotado por maxRadiusX
        const angle = Math.random() * Math.PI * 2;
        
        // Radio real X se acota para no salir de la esfera
        const randomRadiusFactor = Math.random() * 0.9; 
        const actualRadiusX = maxRadiusX * randomRadiusFactor;
        
        // Coordenadas Finales
        const x_final = (radiusCopa) + Math.cos(angle) * actualRadiusX; 
        const y_final = y_esfera;

        // --- APLICAMOS COORDENADAS ---
        heart.style.left = `${x_final}px`;
        heart.style.top = `${y_final}px`;
        heart.style.backgroundColor = colors[Math.floor(Math.random() * colors.length)];
        
        // Tamaño aleatorio para naturalidad
        const size = Math.random() * 12 + 10;
        heart.style.width = `${size}px`;
        heart.style.height = `${size}px`;

        treeTop.appendChild(heart);
        heartsCreated++;
    }

    // --- LLUVIA DE CORAZONES POR TODA LA PANTALLA ---
    function createRainHeart() {
        const heart = document.createElement('div');
        heart.classList.add('heart-rain');
        
        // Posicionamiento horizontal aleatorio por todo el ancho de la pantalla
        heart.style.left = Math.random() * 100 + 'vw';
        
        // Color aleatorio
        heart.style.backgroundColor = colors[Math.floor(Math.random() * colors.length)];
        
        // Velocidad aleatoria para naturalidad (caída entre 3 y 6 segundos)
        const fallDuration = Math.random() * 3 + 3;
        heart.style.animationDuration = `${fallDuration}s`;

        document.body.appendChild(heart);

        // Eliminamos el corazón cuando termina su caída para no saturar la memoria
        setTimeout(() => {
            heart.remove();
        }, fallDuration * 1000);
    }

    // --- INICIAMOS LA CREACIÓN PROGRESIVA DE CORAZONES (EL ÁRBOL NACE) ---
    // Esperamos 2s para que se muestre el tronco realista
    setTimeout(() => {
        const heartInterval = setInterval(createTreeHeart, INTERVAL_MS);
    }, 2000);

    // --- INICIAMOS LA LLUVIA DE CORAZONES ---
    setInterval(createRainHeart, 400);

    // --- LÓGICA DEL TEXTO DIFERIDO (¡¡RÁPIDO!!) ---
    // Mostramos el texto tras el retraso corto configurado
    setTimeout(() => {
        textOverlay.classList.add('visible');
    }, TEXT_DELAY_MS);

    // Contador de tiempo (sin cambios)
    const startDate = new Date("2025-01-01T00:00:00");
    function updateCounter() {
        const now = new Date();
        const diff = now - startDate;
        const d = Math.floor(diff / (1000 * 60 * 60 * 24));
        const h = Math.floor((diff / (1000 * 60 * 60)) % 24);
        const m = Math.floor((diff / (1000 * 60)) % 60);
        const s = Math.floor((diff / 1000) % 60);
        document.getElementById('time').innerHTML = 
            `Juntos hace: ${d}d ${h}h ${m}m ${s}s`;
    }
    setInterval(updateCounter, 1000);
    updateCounter(); // Primera actualización inmediata
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
     
