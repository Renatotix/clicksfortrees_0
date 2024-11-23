let contador = 0;

function contar() {
  contador++;
  document.getElementById("contador").textContent = contador;
  
  ;
}
function efecto() {
  const effect = document.createElement("div");
  effect.classList.add("click-effect");
  effect.style.left = `${event.clientX}px`;
  effect.style.top = `${event.clientY}px`;
  document.body.appendChild(effect);
  effect.addEventListener("animationend", () => {
  effect.remove();
  })
}