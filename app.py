from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    persona = Persona()

    texto = 'Hello, '
    texto = texto + persona.nombre

    return createhtml(persona)

def createhtml(persona):
    html  = "<center>"
    html += "<br />"
    html += "<img src='" + persona.urlfoto + "' style='width: 200px;' />"
    html += "<br />"
    html += "<b>" + persona.nombre + "</b>"
    html += "<br />"
    html += persona.profesion
    html += "<br /><br />"
    html += "<div style='text-align: left; width: 700px;'>"
    html += "<legend><b>Estudios</b></legend>"
    html += persona.getestudios()
    html += "</div>"

    html += "<div style='text-align: left; width: 700px;'>"
    html += "<legend><b>Experiencia Laboral</b></legend>"
    html += persona.getexperiencias()
    html += "</div>"

    return html

class Persona:

    nombre = "Ian Sebastian Martinez Rey"
    profesion = "Ingeniero en Sistemas"
    foto = "/foto.jpeg"
    urlfoto = "https://ldbn.is.escuelaing.edu.co/events/cloudnative/img/ian.jpg"


    def getestudios(self):
        html =  "<ul>"
        html += "<li>Mestria en informatica (Actualmente) / Escuela colombiana de Ingenieria</li>"
        html += "<li>Ingenieria en Sistemas / UNAD</li>"
        html += "<li>Tecnico en analisis y programacion de sistemas / Corporacion Tencologica Empresarial</li>"
        html += "<li>Bachiller Academico / IED El Japon</li>"
        html += "</ul>"
        return html


    def getexperiencias(self):
        html =  "<ul>"
        html += "<li>"
        html += "Applications Lead Engineer <br />"
        html += "<b>Icontec</b>"
        html += "</li>"

        html += "<li>"
        html += "Application and Infraestructure Lead<br />"
        html += "<b>Lg Electronics</b>"
        html += "</li>"

        html += "<li>"
        html += "Developer<br />"
        html += "<b>Lg Electronics</b>"
        html += "</li>"

        html += "<li>"
        html += "Developer<br />"
        html += "<b>Adecco Colombia</b>"
        html += "</li>"

        html += "</ul>"
        return html
