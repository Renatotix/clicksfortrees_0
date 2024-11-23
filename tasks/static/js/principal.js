const parrafos = [
    "Los árboles son esenciales para la vida en la Tierra, ya que producen oxígeno, regulan el clima, conservan la biodiversidad y ayudan a purificar el medioambiente. Su capacidad para absorber dióxido de carbono los hace un factor determinante en la lucha contra el cambio climático.",
    "Los árboles son fundamentales para el equilibrio ecológico del planeta. Absorben dióxido de carbono, liberando oxígeno esencial para la vida humana y animal. Su presencia contribuye a mitigar los efectos del cambio climático, ayudando a regular la temperatura y mejorar la calidad del aire.",
    "Además de ser generadores de oxígeno, los árboles desempeñan un papel crucial en la conservación del agua. Sus raíces ayudan a prevenir la erosión del suelo y a filtrar el agua, mejorando la calidad de los recursos hídricos y reduciendo el riesgo de inundaciones.",
    "Los árboles son vitales para la biodiversidad. Proporcionan hábitats y alimento a numerosas especies de flora y fauna, creando ecosistemas ricos que sostienen una amplia variedad de organismos. La preservación de los bosques es esencial para mantener el equilibrio de los ecosistemas naturales.",
    "Los árboles también actúan como reguladores del clima. A través del proceso de transpiración, liberan vapor de agua que contribuye a la formación de nubes y a la regulación de las precipitaciones. Esto ayuda a mantener el ciclo hidrológico en muchas regiones del mundo.",
    "La deforestación representa una amenaza creciente para el medio ambiente, ya que la pérdida de árboles reduce la capacidad de la Tierra para absorber carbono. Restaurar y proteger los bosques es crucial para luchar contra el calentamiento global y preservar un futuro sostenible para las próximas generaciones.",
    "Los árboles no solo contribuyen a la calidad del aire, sino que también mejoran el microclima de las áreas urbanas. Al ofrecer sombra, reducen el calor ambiental y ayudan a disminuir la necesidad de aire acondicionado, lo que a su vez reduce el consumo de energía.",
    "El papel de los árboles en la captura de carbono es esencial para combatir el cambio climático. A medida que los árboles crecen, almacenan carbono en sus troncos, raíces y hojas, actuando como sumideros de carbono y mitigando las emisiones de gases de efecto invernadero.",
    "La madera de los árboles también tiene una función importante. Cuando se usa de manera sostenible, puede reemplazar materiales más contaminantes en la construcción y la fabricación, ayudando a reducir la huella de carbono de diferentes industrias.",
    "Los árboles juegan un papel importante en la regulación del ciclo del nitrógeno en el suelo. A través de su capacidad para fijar este elemento, contribuyen a la fertilidad del suelo, lo que beneficia tanto a la flora como a la fauna que dependen de los recursos naturales.",
    "La conexión entre los seres humanos y los árboles es profunda. Además de sus beneficios ambientales, los árboles proporcionan espacios para el esparcimiento, la relajación y el bienestar emocional. Los parques y bosques urbanos mejoran la calidad de vida, fomentando la salud mental de las personas."
];

let indice = 0;

// Función para cambiar el párrafo
function cambiarTexto() {
    // Selecciona el elemento de texto
    const textoElemento = document.getElementById('miTexto');

    // Hacer que el texto actual desaparezca suavemente (con opacidad)
    textoElemento.style.opacity = 0;

    // Cambiar el texto después de 1 segundo (cuando la opacidad haya terminado)
    setTimeout(() => {
        indice++;
        if (indice >= parrafos.length) {
            indice = 0; // Resetea al primer párrafo cuando llega al final
        }
        textoElemento.textContent = parrafos[indice];

        // Volver a mostrar el texto con una transición de opacidad
        textoElemento.style.opacity = 1;
    }, 1000); // 1000 ms = 1 segundo (tiempo de transición)
}

// Cambiar el texto cada 5 segundos
setInterval(cambiarTexto, 9000); // Cambiar cada 5 segundos
const imagenes = document.querySelectorAll('.bosques'); // Selecciona todas las imágenes
let ind = 0; // Índice para llevar el control de la imagen actual

// Función para cambiar las imágenes con animación
function cambiarImagen() {
    // Quitar la clase 'visible' de la imagen actual
    imagenes[ind].classList.remove('visible');

    // Incrementar el índice y reiniciar si es necesario
    ind++;
    if (ind === imagenes.length) {
        ind = 0; // Reiniciar al principio
      }

      // Agregar la clase 'visible' a la nueva imagen
      imagenes[ind].classList.add('visible');
    }

    // Cambiar la imagen cada 3 segundos (3000 ms)
    setInterval(cambiarImagen, 4500);