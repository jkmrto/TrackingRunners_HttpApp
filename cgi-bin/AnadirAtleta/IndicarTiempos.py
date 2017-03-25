import cgi
import cgitb
from templates import yate

cgitb.enable()
form_data = cgi.FieldStorage()

nombre_atleta = form_data['nombre_atleta'].value

print(yate.start_response())

print(yate.include_header("Introducir las marcas de {}".format(nombre_atleta)))

print(yate.start_form("FinalAnadirAtletaDDBB.py"))

print(yate.hidden_input("Nombre", nombre_atleta))
print(yate.text_field("tiempo1", "Indicar tiempo"))
print(yate.text_field("tiempo2", "Indicar tiempo"))
print(yate.text_field("tiempo3", "Indicar tiempo"))
print(yate.text_field("tiempo4", "Indicar tiempo"))
print(yate.text_field("tiempo5", "Indicar tiempo"))
print(yate.text_field("tiempo6", "Indicar tiempo"))
print(yate.text_field("tiempo7", "Indicar tiempo"))
print(yate.text_field("tiempo8", "Indicar tiempo"))
print(yate.text_field("tiempo9", "Indicar tiempo"))
print(yate.text_field("tiempo10", "Indicar tiempo"))


print(yate.end_form("Aceptar"))

print(yate.include_footer({"Renombrar Atleta":
                               "/cgi-bin/AnadirAtleta/IndicarNombreAtleta.py"}))
print(yate.include_footer({"Indice": "/cgi-bin/indice.py"}))
