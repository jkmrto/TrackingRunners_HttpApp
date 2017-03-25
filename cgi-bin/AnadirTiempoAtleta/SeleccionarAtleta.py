import glob

from lib import athletemodel
from templates import yate

data_files = glob.glob("data/*.txt")
athletes_info = athletemodel.get_namesID_from_store()

print(yate.start_response())

print(yate.include_header("Lista de Atletas:"))

print(yate.start_form("IndicarTiempo.py"))

print(yate.para("Seleccionar atleta al cual añadir el tiempo:"))
for each_athlete in athletes_info:
    print(yate.radio_button("ID", each_athlete['name'], each_athlete['ID']))

print(yate.end_form("Acepar"))

print(yate.include_footer({"Indice": "/cgi-bin/indice.py"}))



