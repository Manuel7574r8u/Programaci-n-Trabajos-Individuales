window.onload = function() {

    const boton = document.getElementById("btn");
    const parrafo = document.getElementById("texto");

    // Al hacer clic
    boton.addEventListener("click", function() {
        parrafo.textContent = "¡Día fantástico para Manuel! (Ref: MPG)";
        parrafo.style.color = "orange";
    });

    // Al pasar el ratón
    boton.addEventListener("mouseenter", function() {
        boton.textContent = "¡Púlsame, Paradas!";
    });

};