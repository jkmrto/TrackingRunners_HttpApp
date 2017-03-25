'''
Created on 13 may. 2016

@author: Manuel
'''
import glob

from lib import athletemodel
from templates import yate

data_files = glob.glob("data/*.txt")
athletes_info = athletemodel.get_namesID_from_store()

print(yate.start_response())   
    
print(yate.include_header("Registro de atletas"))

print(yate.start_form("generate_timing_data.py"))

print(yate.para("Selecciona el atleta del cual deseas ver los tiempos:"))
for each_athlete in athletes_info:
    print(yate.radio_button("ID", each_athlete['name'], each_athlete['ID']))

print(yate.end_form("Aceptar"))

print(yate.include_footer({"Indice": "/cgi-bin/indice.py"}))

