let contador = 0;

function contar() {
  contador++;
  document.getElementById("contador").textContent = contador;
  if (contador % 100 === 0) {
    const mensaje = document.getElementById("mensaje");
    mensaje.classList.remove("mensaje-oculto");


    setTimeout(() => {
      mensaje.classList.add("mensaje-oculto");
    }, 4000);
  }
  const effect =
    document.createElement("div");
  effect.classList.add("click-effect");
  effect.style.left = `${event.clientX}px`;
  effect.style.top = `${event.clientY}px`;
  document.body.appendChild(effect);
  effect.addEventListener("animationend", () => {
    effect.remove();
  });
}
