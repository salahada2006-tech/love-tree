from flask import Flask
import os

app = Flask(__name__)

# Aquí pegamos tu diseño
html_content = """
<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<title>Love Tree 💖</title>
<style>
body{
    margin:0;
    font-family: 'Segoe UI', sans-serif;
    background: linear-gradient(#ffd6e0, #ffeaf4);
    overflow:hidden;
}
.nube{
    position:absolute;
    background:#fff;
    border-radius:50%;
    opacity:0.6;
}
.nube1{ width:120px; height:60px; top:50px; left:50px;}
.nube2{ width:150px; height:70px; top:120px; right:60px;}
.card{
    position:absolute;
    top:50%;
    left:50%;
    transform:translate(-50%,-50%);
    background:rgba(255,255,255,0.8);
    backdrop-filter: blur(10px);
    padding:25px;
    border-radius:20px;
    width:340px;
    box-shadow:0 15px 30px rgba(255,182,193,0.4);
    text-align:center;
    color:#ff4d88;
}
.card p{ font-size:15px; }
.tree{
    position:relative;
    width:200px;
    height:200px;
    margin:20px auto;
}
.trunk{
    position:absolute;
    bottom:0;
    left:50%;
    transform:translateX(-50%);
    width:20px;
    height:60px;
    background:#a0522d;
    border-radius:5px;
}
.heart{
    position:absolute;
    width:15px;
    height:15px;
    transform:rotate(45deg);
}
.heart::before, .heart::after{
    content:"";
    position:absolute;
    width:15px;
    height:15px;
    background:inherit;
    border-radius:50%;
}
.heart::before{ top:-7px; left:0;}
.heart::after{ left:-7px; top:0;}
@keyframes flotar {
    0%{ transform: translateY(0) rotate(45deg);}
    50%{ transform: translateY(-12px) rotate(45deg);}
    100%{ transform: translateY(0) rotate(45deg);}
}
@keyframes caer {
    0%{ transform: translateY(-50px) rotate(45deg); opacity:1;}
    100%{ transform: translateY(300px) rotate(45deg); opacity:0;}
}
</style>
</head>
<body>
<div class="nube nube1"></div>
<div class="nube nube2"></div>
<div class="card">
    <p>
        Para el amor de mi vida 💖<br><br>
        Eres mi lugar seguro, mi paz y mi felicidad.<br>
        Cada día te amo más... ✨
    </p>
    <div class="tree" id="tree">
        <div class="trunk"></div>
    </div>
    <p id="time"></p>
</div>
<script>
const tree = document.getElementById("tree");
const colors = ["#ff4d88","#ff66a3","#ff99cc","#ffb3d9","#ffcce6"];
function crearCorazones(){
    for(let i=0;i<120;i++){
        let heart = document.createElement("div");
        heart.className = "heart";
        heart.style.left = Math.random()*180 + "px";
        heart.style.top = Math.random()*140 + "px";
        heart.style.background = colors[Math.floor(Math.random()*colors.length)];
        heart.style.animation = `flotar ${2+Math.random()*3}s infinite`;
        heart.style.animationDelay = Math.random()*2 + "s";
        tree.appendChild(heart);
    }
}
crearCorazones();
function lluvia(){
    let heart = document.createElement("div");
    heart.className = "heart";
    heart.style.left = Math.random()*window.innerWidth + "px";
    heart.style.top = "-20px";
    heart.style.background = colors[Math.floor(Math.random()*colors.length)];
    heart.style.position = "absolute";
    heart.style.animation = "caer 3s linear";
    document.body.appendChild(heart);
    setTimeout(()=>heart.remove(),3000);
}
setInterval(lluvia,300);
const startDate = new Date("2025-01-01");
function updateTime(){
    const now = new Date();
    let diff = now - startDate;
    let d = Math.floor(diff / (1000*60*60*24));
    let h = Math.floor((diff/(1000*60*60))%24);
    let m = Math.floor((diff/(1000*60))%60);
    let s = Math.floor((diff/1000)%60);
    document.getElementById("time").innerHTML =
        `Te amo desde hace... 💕<br>
        ${d} días ${h}h ${m}m ${s}s`;
}
setInterval(updateTime,1000);
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
