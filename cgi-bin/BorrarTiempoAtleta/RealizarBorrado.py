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
print(yate.include_header("Borrando la  marca {0}"
                          " para el atleta {1}".format(Tiempo, athlete_info['Name'])))
try:
    athletemodel.BorraTiempoAtleta(athlete_ID, Tiempo)
    print(yate.para(" El borrado se ha relizado correctamente"))
except Exception as e:
    print(yate.para("Error borrando el dato:" + str(e)))



print(yate.include_footer({"Indice": "/index.html"}))
