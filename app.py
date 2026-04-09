from flask import Flask
import os

app = Flask(__name__)

html_content = """
<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Nuestro Árbol del Amor Progressivo 💖</title>
<style>
    body {
        margin: 0;
        height: 100vh;
        display: flex;
        align-items: center;
        justify-content: center;
        background-color: #000; /* Fondo negro para máximo contraste */
        font-family: 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
        overflow: hidden;
    }

    .container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        width: 100%;
        max-width: 500px;
    }

    /* EL ÁRBOL */
    .tree {
        position: relative;
        width: 320px;
        height: 400px;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: flex-end; /* Para que el tronco esté abajo */
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
        animation-delay: 0.5s; /* Empieza a aparecer a los 0.5s */
    }

    /* COPA DEL ÁRBOL - Contenedor invisible al inicio */
    .tree-top {
        position: absolute;
        bottom: 90px; /* Justo sobre el tronco */
        width: 100%;
        height: 300px;
    }

    /* CORAZÓN INDIVIDUAL */
    .heart {
        position: absolute;
        width: 20px;
        height: 20px;
        background: #ff0055;
        transform: rotate(-45deg) scale(0);
        opacity: 0;
        animation: heartGrow 1.5s ease-out forwards;
    }

    .heart::before, .heart::after {
        content: '';
        position: absolute;
        width: 20px;
        height: 20px;
        background: inherit;
        border-radius: 50%;
    }

    .heart::before { top: -10px; left: 0; }
    .heart::after { left: 10px; top: 0; }

    /* TEXTO CON EL CONTADOR - Aparece al final */
    .text-overlay {
        color: white;
        margin-top: 30px;
        text-align: center;
        opacity: 0; /* Invisible al inicio */
        text-shadow: 0 0 15px rgba(255, 77, 136, 0.8);
        transition: opacity 2s ease-in; /* Transición suave */
    }

    /* Clase para mostrar el texto al final */
    .text-overlay.visible {
        opacity: 1;
    }

    #time {
        font-size: 1.3rem;
        font-weight: bold;
        margin-top: 10px;
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
</style>
</head>
<body>

<div class="container">
    <div class="tree">
        <div class="tree-top" id="tree-top"></div>
        <div class="trunk"></div>
    </div>
    
    <div class="text-overlay" id="text-overlay">
        <h2>Nuestra historia... 💖</h2>
        <div id="time"></div>
    </div>
</div>

<script>
    const treeTop = document.getElementById('tree-top');
    const textOverlay = document.getElementById('text-overlay');
    const colors = ['#ff0033', '#ff0055', '#ff3377', '#ff6699', '#fb6f92'];

    // Configuración de la animación progresiva
    const TOTAL_HEARTS = 250; // Corazones totales para formar el árbol
    const INTERVAL_MS = 100; // Un corazón cada 100ms
    const TEXT_DELAY_MS = 25000; // Esperar 25 segundos antes de mostrar el texto

    let heartsCreated = 0;

    function createHeart() {
        if (heartsCreated >= TOTAL_HEARTS) {
            clearInterval(heartInterval);
            return;
        }

        const heart = document.createElement('div');
        heart.classList.add('heart');
        
        // 1. LÓGICA DE CRECIMIENTO ASCENDENTE (EL ÁRBOL NACE DESDE ABAJO)
        const currentProgress = heartsCreated / TOTAL_HEARTS; // Valor de 0 a 1
        
        // El radio máximo de la copa del árbol (se expande con el tiempo)
        const maxRadius = 130;
        
        // Usamos currentProgress para que los primeros corazones (y=0)
        // estén más cerca del tronco, y los últimos (y=1) formen la cima.
        
        // Posicionamiento circular que se expande hacia arriba
        const angle = Math.random() * Math.PI * 2;
        
        // Radio aleatorio, pero el máximo aumenta con el progreso
        const radius = Math.random() * maxRadius * currentProgress; 
        
        const x = Math.cos(angle) * radius + 160; // Centro X (mitad de la copa)
        
        // La altura (Y) se calcula progresivamente desde abajo (0) hacia arriba (300)
        // Agregamos un poco de aleatoriedad para naturalidad
        const baseY = 280; // Altura base (justo sobre el tronco)
        const maxTreeHeight = 250;
        const heightVariation = Math.random() * 50; // Variación aleatoria
        
        // Calculamos Y: empieza cerca de baseY y sube (resta) hasta la cima
        const y = baseY - (maxTreeHeight * currentProgress) - heightVariation;

        heart.style.left = `${x}px`;
        heart.style.top = `${y}px`;
        heart.style.backgroundColor = colors[Math.floor(Math.random() * colors.length)];
        
        // Tamaño aleatorio para naturalidad (algunos pequeños, otros medianos)
        const size = Math.random() * 12 + 10;
        heart.style.width = `${size}px`;
        heart.style.height = `${size}px`;

        treeTop.appendChild(heart);
        heartsCreated++;
    }

    // 2. INICIAMOS LA CREACIÓN PROGRESIVA DE CORAZONES (EL ÁRBOL NACE)
    // Esperamos 1.5s para que el tronco se muestre primero
    setTimeout(() => {
        const heartInterval = setInterval(createHeart, INTERVAL_MS);
    }, 1500);

    // 3. LÓGICA DEL TEXTO DIFERIDO (LAS LETRAS SALEN AL FINAL)
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
