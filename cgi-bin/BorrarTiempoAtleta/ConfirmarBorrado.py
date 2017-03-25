'''
Created on 25 Enero. 2017

@author: jkmrto
'''
import cgi
import cgitb

from lib import athletemodel
from templates import yate
cgitb.enable()

form_data = cgi.FieldStorage()
athlete_ID = form_data['ID'].value
Tiempo = form_data['Tiempo'].value

athlete_info = athletemodel.get_athlete_from_id(athlete_ID)

print(yate.start_response())

print(yate.start_form("RealizarBorrado.py"))

print(yate.include_header("Esta seguro que desea realizar el borrado de la marca {0}"
                          " para el atleta {1}".format(Tiempo, athlete_info['Name'])))

print(yate.hidden_input("Tiempo", Tiempo))
print(yate.hidden_input("ID", athlete_ID))

print(yate.end_form("Aceptar"))

print(yate.include_footer({"Indice": "/cgi-bin/indice.py"}))
