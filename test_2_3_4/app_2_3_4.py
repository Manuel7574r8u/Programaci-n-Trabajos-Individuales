# Importamos la función para manejar plantillas
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/coleccion")
def ver_coleccion():
    # Creamos una lista de diccionarios con datos de prueba
    mis_favoritos = [
        {"deporte": "Fúbol", "equipo": "Sevilla"},
        {"deporte": "Baloncesto", "equipo": "Los Lakers"},
        {"deporte": "Fútbol Sala", "equipo": "Cibeles FS"}
    ]
    # Enviamos la lista completa a la plantilla con el nombre 'favoritos'
    return render_template("galeria.html", favoritos=mis_favoritos)

    # Comprobamos si el script se está ejecutando directamente (y no importado como módulo)
if __name__ == "__main__":
    # Arrancamos el servidor en modo debug para que se reinicie solo al guardar cambios
    app.run(debug=True)