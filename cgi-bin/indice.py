'''
Created on 13 may. 2016

@author: Manuel
'''
import glob

from lib import athletemodel
from templates import yate

print(yate.start_response())

print(yate.include_header("<strong>Opciones disponibles:"))

print(yate.include_footer({"Mostrar tiempos de un atleta":
                               "/cgi-bin/generate_list.py"}))

print(yate.include_footer({"Mostrar comparativa de los tiempos de los atletas":
                          "/cgi-bin/TablaComparativa/MostrarComparacion.py"}))

print(yate.include_footer({"Añadir Atleta":
                               "/cgi-bin/AnadirAtleta/IndicarNombreAtleta.py"}))

print(yate.include_footer({"Añadir tiempo a un Atleta":
                               "/cgi-bin/AnadirTiempoAtleta/SeleccionarAtleta.py"}))

print(yate.include_footer({"Borrar tiempo de un atleta":
                               "/cgi-bin/BorrarTiempoAtleta/MostrarySeleccionarAtleta.py"}))

print(yate.include_footer({"Eliminar atleta":
                                "/cgi-bin/borrarAtleta/MostrarySeleccionarAtleta.py"}))

