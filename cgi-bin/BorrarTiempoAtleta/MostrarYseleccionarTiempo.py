'''
Created on 25 Enero. 2017

@author: jkmrto
'''
import cgi
import cgitb
import settings

from lib import athletemodel
from templates import yate
from images import GeneradorGraficas

cgitb.enable()

form_data = cgi.FieldStorage()
athlete_ID = form_data['ID'].value

athlete_info = athletemodel.get_athlete_from_id(athlete_ID)

print(yate.start_response())

print(yate.start_form("ConfirmarBorrado.py"))

print(yate.include_header("Tiempos para " + athlete_info['Name']))

print(yate.para("Seleccionar la marca que se quiere borrar:"))

for data in athlete_info['data']:
    print(yate.radio_button("Tiempo", "", data))


print(yate.hidden_input("ID", athlete_ID))

print(yate.end_form("Aceptar"))

print(yate.include_footer({"Seleccinar otro atleta": "/cgi-bin/BorrarTiempoAtleta/MostrarySeleccionarAtleta.py"}))
print(yate.include_footer({"Indice": "/cgi-bin/indice.py"}))