# app.py final y estable: Tronco Sencillo, Copa de Corazón y Ambiente Completo ❤️

from flask import Flask
import os

app = Flask(__name__)

# Diseño definitivo del "Árbol con Tronco Sencillo y Ambiente Romántico"
html_content = """
<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Nuestro Árbol del Corazón con Ambiente ❤️</title>

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
        flex-direction: column; /* Alineación vertical */
        align-items: center;
        justify-content: center;
        /* --- FONDO AZULITO (Como en image_11.png) --- */
        background: linear-gradient(135deg, #a7d8f5 0%, #d8effb 100%); 
        overflow: hidden;
        position: relative;
    }

    /* --- NUBES EN FORMA DE CORAZÓN (SVG) - Recuperadas --- */
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
        justify-content: flex-start;
        width: 100%;
        max-width: 500px;
        position: relative;
        z-index: 5; /* Por encima de las nubes y la lluvia */
    }

    /* --- EL ÁRBOL - Contenedor Principal (Como en image_11.png) --- */
    .tree-container {
        position: relative;
        width: 300px; /* Ancho para la copa de image_11 */
        height: 400px; /* Altura total */
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: flex-end; /* Tronco abajo */
    }

    /* --- TRONCO SENCILLO Y RECTO (Recuperado de image_11.png) --- */
    .trunk-sencillo {
        width: 16px; /* Como en image_11 */
        height: 100px; /* Altura del tronco */
        background: linear-gradient(to right, #4d2600, #a0522d, #4d2600);
        border-radius: 8px; /* Contorno suave */
        position: relative;
        z-index: 2; /* Los corazones aparecen entre el tronco */
        opacity: 0;
        animation: fadeIn 1s ease-in forwards;
        animation-delay: 0.5s; /* Aparece primero */
    }

    /* COPA DEL ÁRBOL - Contenedor invisible al inicio (SOBRE EL TRONCO) */
    /* Mantenemos la lógica de image_8.png para que sea un corazón perfecto */
    .tree-top {
        position: absolute;
        bottom: 85px; /* Un poco sobre el tronco */
        width: 300px; /* Diámetro de la copa */
        height: 300px; /* Altura de la copa */
    }

    /* CORAZÓN INDIVIDUAL (Copa) */
    .heart-tree {
        position: absolute;
        width: 20px;
        height: 20px;
        background: #ff0055; /* Color rojo vibrante */
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

    /* --- LLUVIA DE CORAZONES POR TODA LA PANTALLA - Recuperada --- */
    .heart-rain {
        position: absolute;
        width: 12px;
        height: 12px;
        background: #ff0055;
        transform: rotate(-45deg);
        opacity: 0.8;
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

    /* TEXTO CON MENSAJE ESPECIAL Y CONTADOR - ¡HACER RESALTAR EN FUCSIA! */
    .text-overlay {
        margin-top: 10px;
        text-align: center;
        opacity: 0; /* Invisible al inicio */
        transition: opacity 2s ease-in; /* Transición suave */
        position: relative;
        width: 100%;
        font-family: 'Poppins', sans-serif;
        z-index: 10;
    }

    /* Clase para mostrar el texto al final */
    .text-overlay.visible {
        opacity: 1;
    }

    /* TÍTULO PRINCIPAL BONITO Y LEGIBLE FUCSIA */
    .text-overlay h2 {
        font-family: 'Dancing Script', cursive; /* APLICAMOS FUENTE BONITA Y LEGIBLE */
        font-size: 2.8rem;
        font-weight: 700; /* ¡¡NEGRILLA!! para resaltar */
        margin: 0;
        
        /* --- ¡¡TEXTO FUCSIA VIBRANTE!! (Como en image_11) --- */
        color: #ff007f; /* Color fucsia */
        text-shadow: 0 0 10px rgba(255, 0, 127, 0.5); /* Contorno fucsia suave */
    }

    /* MENSAJE ESPECIAL POÉTICO Y LEGIBLE */
    .special-message {
        font-family: 'Playfair Display', serif; /* FUENTE POÉTICA */
        font-style: italic;
        font-size: 1.2rem;
        color: #ff007f; /* Fucsia */
        margin: 15px 0;
        line-height: 1.6;
        text-shadow: 0 0 8px rgba(255, 0, 127, 0.3); /* Contorno suave */
    }

    /* CONTADOR - Con fuente legible */
    #time {
        font-size: 1.1rem;
        font-weight: 300;
        margin-top: 15px;
        font-family: 'Poppins', sans-serif;
        color: #ff007f; /* Fucsia */
    }

    /* ANIMACIONES */
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
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
        <div class="trunk-sencillo"></div>
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
    const TEXT_DELAY_MS = 28000; // Esperar 28 segundos antes de mostrar el texto (ajustable)

    let heartsCreated = 0;

    function createHeart() {
        if (heartsCreated >= TOTAL_HEARTS) {
            clearInterval(heartInterval);
            return;
        }

        const heart = document.createElement('div');
        heart.classList.add('heart-tree');
        
        // --- LÓGICA DE DISTRIBUCIÓN ESFÉRICA PERFECTA (COPA REDONDA de image_8) ---
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
    // Esperamos 1.5s para que el tronco se muestre primero
    setTimeout(() => {
        const heartInterval = setInterval(createHeart, INTERVAL_MS);
    }, 1500);

    // --- INICIAMOS LA LLUVIA DE CORAZONES ---
    setInterval(createRainHeart, 400);

    // --- LÓGICA DEL TEXTO DIFERIDO (LAS LETRAS SALEN AL FINAL) ---
    // Mostramos el texto después del retraso configurado
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
