import cgi
import cgitb

from templates import yate

cgitb.enable()

form_data = cgi.FieldStorage()

athlete_ID = form_data['ID'].value

print(yate.start_response())

print(yate.include_header("Introducir el nueovo tiempo"))

print(yate.start_form("AnadirTiempoDDBB.py"))

print(yate.para("Añadir tiempo para el atleta con ID: {}".format(athlete_ID)))

print(yate.text_field("tiempo","Introducir Tiempo"))

print(yate.hidden_input("ID", athlete_ID))

print(yate.end_form("Aceptar"))

print(yate.include_footer({"Indice": "/cgi-bin/indice.py"}))
