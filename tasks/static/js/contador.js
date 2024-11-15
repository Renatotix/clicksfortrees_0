let contador = 0;

function contar() {
  contador++;
  document.getElementById("contador").textContent = contador;
  if (contador % 1000 === 0) {
    const mensaje = document.getElementById("mensaje");
    mensaje.classList.remove("mensaje-oculto");


    setTimeout(() => {
      mensaje.classList.add("mensaje-oculto");
    }, 3000);
  }
}
