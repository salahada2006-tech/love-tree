# app.py completo y final: Árbol del Amor Perfecto con Texto Fucsia Vibrante

from flask import Flask
import os

app = Flask(__name__)

# Diseño definitivo del "Árbol del Amor Progressivo y Legible con Texto Fucsia"
html_content = """
<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Nuestro Árbol del Corazón Perfecto ❤️ | Historia Fucsia</title>

<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;600&display=swap" rel="stylesheet">

<style>
    body {
        margin: 0;
        height: 100vh;
        display: flex;
        flex-direction: column; /* Alineación vertical para bajar el texto */
        align-items: center;
        justify-content: center;
        /* FONDO AZULITO (de tu imagen 9) */
        background: linear-gradient(135deg, #a7d8f5 0%, #d8effb 100%); 
        overflow: hidden;
    }

    .container {
        display: flex;
        flex-direction: column;
        align-items: center;
        width: 100%;
        max-width: 600px;
        position: relative;
    }

    /* EL ÁRBOL - Contenedor Principal (Como en image_8.png) */
    .tree-container {
        position: relative;
        width: 450px; /* Diámetro de la copa */
        height: 550px; /* Altura total del árbol */
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: flex-end; /* Tronco abajo */
    }

    /* TRONCO REALISTA CON RAMAS (Como en image_7.png) */
    .tree-trunk {
        width: 18px;
        height: 120px;
        background: linear-gradient(to right, #4d2600, #a0522d, #4d2600);
        border-radius: 8px;
        position: relative;
        z-index: 1; /* Los corazones aparecen entre las ramas */
        opacity: 0;
        animation: fadeInTree 2s ease-in forwards;
        animation-delay: 0.5s;
    }

    /* COPA DEL ÁRBOL - Contenedor invisible al inicio (SOBRE EL TRONCO) */
    /* Usamos la forma de la copa de image_8.png para que sea un corazón perfecto */
    .tree-top {
        position: absolute;
        bottom: 110px; /* Un poco sobre el tronco */
        width: 450px; /* Ancho de la copa */
        height: 450px; /* Altura de la copa (Círculo perfecto) */
        border-radius: 50%;
    }

    /* CORAZÓN INDIVIDUAL (Copa) */
    .heart-tree {
        position: absolute;
        width: 22px; /* Un poquito más grandes para que sean visibles */
        height: 22px;
        background: #ff0055; /* Color rojo vibrante */
        transform: rotate(-45deg) scale(0);
        opacity: 0;
        animation: heartGrow 1.5s ease-out forwards;
    }

    .heart-tree::before, .heart-tree::after {
        content: '';
        position: absolute;
        width: 22px;
        height: 22px;
        background: inherit;
        border-radius: 50%;
    }

    .heart-tree::before { top: -11px; left: 0; }
    .heart-tree::after { left: 11px; top: 0; }

    /* TEXTO CON MENSAJE ESPECIAL Y CONTADOR - ¡HACER RESALTAR! */
    .text-overlay {
        margin-top: -30px; /* Un poco más cerca del árbol */
        text-align: center;
        opacity: 0; /* Invisible al inicio */
        transition: opacity 2s ease-in; /* Transición suave */
        font-family: 'Poppins', sans-serif;
        width: 100%;
        z-index: 10; /* Por encima de todo */
    }

    /* Clase para mostrar el texto al final */
    .text-overlay.visible {
        opacity: 1;
    }

    /* MENSAJE PRINCIPAL - ¡HACER RESALTAR EN FUCSIA! */
    .text-overlay h2 {
        font-family: 'Dancing Script', cursive; /* APLICAMOS FUENTE BONITA */
        font-size: 2.8rem;
        font-weight: 700;
        margin: 0;
        
        /* --- ¡¡TEXTO FUCSIA VIBRANTE!! (Como pediste) --- */
        color: #ff007f; /* Color fucsia */
        text-shadow: 0 0 10px rgba(255, 0, 127, 0.5); /* Contorno fucsia suave */
    }

    /* MENSAJE ESPECIAL - ¡HACER RESALTAR! */
    .special-message {
        font-family: 'Poppins', sans-serif;
        font-size: 1.1rem;
        font-weight: 300;
        
        /* --- ¡¡TEXTO FUCSIA VIBRANTE!! --- */
        color: #ff007f;
        
        margin: 15px 0;
        line-height: 1.6;
        text-shadow: 0 0 5px rgba(255, 0, 127, 0.3); /* Contorno fucsia suave */
    }

    /* CONTADOR - Con fuente legible */
    #time {
        font-family: 'Poppins', sans-serif;
        font-size: 1.1rem;
        font-weight: 300;
        margin-top: 15px;
        color: #ff007f; /* Fucsia */
    }

    /* ANIMACIONES */
    @keyframes fadeInTree {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }

    @keyframes heartGrow {
        0% { transform: rotate(-45deg) scale(0); opacity: 0; }
        15% { opacity: 1; }
        100% { transform: rotate(-45deg) scale(1); opacity: 0.9; }
    }
</style>
</head>
<body>

<div class="container">
    <div class="tree-container">
        <div class="tree-top" id="tree-top"></div>
        <div class="tree-trunk"></div>
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

    // --- INICIAMOS LA CREACIÓN PROGRESIVA DE CORAZONES (EL ÁRBOL NACE) ---
    // Esperamos 1.5s para que el tronco se muestre primero
    setTimeout(() => {
        const heartInterval = setInterval(createHeart, INTERVAL_MS);
    }, 1500);

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
