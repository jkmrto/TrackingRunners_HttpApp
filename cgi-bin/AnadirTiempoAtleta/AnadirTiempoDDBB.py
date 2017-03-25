import cgi
import cgitb

from lib import athletemodel
from templates import yate

cgitb.enable()

form_data = cgi.FieldStorage()

athlete_ID = form_data['ID'].value
new_time = form_data['tiempo'].value

print(yate.start_response())


yate.para(new_time + athlete_ID)
print(yate.include_header("Insertando el tiempo {0} del atleta {1}".format(
    new_time, athlete_ID)))

try:
    athletemodel.add_new_time_to_athelte(athlete_ID, new_time)
    print(yate.para("Nuevo tiempo: {0} insertado correctametne al atleta con ID: {1}"
                    .format(new_time, athlete_ID)))
except Exception as e:
    print(yate.para("Error añadiendo el nuevo tiempo" + str(e)))

print(yate.include_footer({"Indice": "/cgi-bin/indice.py"}))
