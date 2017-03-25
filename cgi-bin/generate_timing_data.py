'''
Created on 8 dic. 2016

@author: Manuel
'''
import cgi
import cgitb

from lib import athletemodel
from templates import yate
from images.GeneradorGraficas import GenerarGraficasTiempos

cgitb.enable()

form_data = cgi.FieldStorage()
athlete_ID = form_data['ID'].value

athlete_info = athletemodel.get_athlete_from_id(athlete_ID)

print(yate.start_response())   
    
print(yate.include_header("Datos de tiempo para: " + athlete_info['Name']))

print(yate.para("The top times for this athlete are:"))
print(yate.u_list(athlete_info['top3']))

GenerarGraficasTiempos(athlete_info, "images/tiempos.png")

print(yate.para("Grafica de Evolucion de sus tiempos:"))
print(yate.simple_plot("/images/tiempos.png"))

print(yate.include_footer({"Indice": "/cgi-bin/indice.py"}))
print(yate.include_footer({"Seleccionar otro atleta":"generate_list.py"}))