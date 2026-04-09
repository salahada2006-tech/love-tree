# app.py final con el mensaje completo y fuentes bonitas

from flask import Flask
import os

app = Flask(__name__)

# Diseño definitivo del "Árbol Redondo Progressivo y Lluvia con Mensaje Especial"
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
        background-color: #000; /* Fondo negro para máximo contraste */
        overflow: hidden;
    }

    .container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: flex-start;
        width: 100%;
        max-width: 500px;
        position: relative;
    }

    /* EL ÁRBOL - Contenedor Principal */
    .tree-container {
        position: relative;
        width: 320px;
        height: 400px;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: flex-end; /* Tronco abajo */
    }

    /* TRONCO - Aparece primero */
    .trunk {
        width: 16px;
        height: 100px;
        background: linear-gradient(to right, #4d2600, #a0522d, #4d2600);
        border-radius: 8px;
        position: relative;
        z-index: 1;
        opacity: 0;
        animation: fadeIn 1s ease-in forwards;
        animation-delay: 0.5s;
    }

    /* COPA DEL ÁRBOL - Contenedor invisible al inicio (SOBRE EL TRONCO) */
    .tree-top {
        position: absolute;
        bottom: 85px; /* Un poco sobre el tronco */
        width: 300px; /* Diámetro de la copa */
        height: 300px; /* Altura de la copa (iguala al diámetro para ser esférica) */
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
        width: 15px;
        height: 15px;
        background: #ff0055;
        transform: rotate(-45deg);
        opacity: 0.8;
        animation: heartRainFall linear forwards;
    }

    .heart-rain::before, .heart-rain::after {
        content: '';
        position: absolute;
        width: 15px;
        height: 15px;
        background: inherit;
        border-radius: 50%;
    }

    .heart-rain::before { top: -7.5px; left: 0; }
    .heart-rain::after { left: 7.5px; top: 0; }

    /* TEXTO CON EL MENSAJE ESPECIAL Y CONTADOR - Aparece al final */
    .text-overlay {
        color: white;
        margin-top: 20px;
        text-align: center;
        opacity: 0; /* Invisible al inicio */
        text-shadow: 0 0 15px rgba(255, 77, 136, 0.8);
        transition: opacity 2s ease-in; /* Transición suave */
        position: relative;
        width: 100%;
        font-family: 'Poppins', sans-serif;
    }

    /* Clase para mostrar el texto al final */
    .text-overlay.visible {
        opacity: 1;
    }

    /* TÍTULO PRINCIPAL (Bonito) */
    .text-overlay h2 {
        font-family: 'Dancing Script', cursive; /* APLICAMOS FUENTE BONITA */
        font-size: 2.2rem;
        font-weight: 700;
        margin: 0;
    }

    /* MENSAJE ESPECIAL (Cursivo/Poético) */
    .special-message {
        font-family: 'Playfair Display', serif; /* FUENTE POÉTICA */
        font-style: italic;
        font-size: 1.2rem;
        color: #ffb3c1;
        margin: 20px 0;
        line-height: 1.6;
        opacity: 0;
        transition: opacity 1.5s ease-in;
        transition-delay: 1.5s; /* Aparece justo después del título */
    }

    .text-overlay.visible .special-message {
        opacity: 1;
    }

    /* CONTADOR - Con fuente legible */
    #time {
        font-size: 1.1rem;
        font-weight: 300;
        margin-top: 15px;
        font-family: 'Poppins', sans-serif;
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

<div class="container">
    <div class="tree-container">
        <div class="tree-top" id="tree-top"></div>
        <div class="trunk"></div>
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

    function createTreeHeart() {
        if (heartsCreated >= TOTAL_HEARTS) {
            clearInterval(heartInterval);
            return;
        }

        const heart = document.createElement('div');
        heart.classList.add('heart-tree');
        
        // --- LÓGICA DE DISTRIBUCIÓN ESFÉRICA PERFECTA (COPA REDONDA) ---
        // Radio de la copa (iguala al tamaño de .tree-top)
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
        const heartInterval = setInterval(createTreeHeart, INTERVAL_MS);
    }, 1500);

    // --- INICIAMOS LA LLUVIA DE CORAZONES ---
    // Un corazón de lluvia cada 400ms
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
