'''
Created on 13 may. 2016

@author: jkmrto
'''
import glob
from lib import Funciones

from lib import athletemodel
from templates import yate

data_files = glob.glob("data/*.txt")
athletes_info = athletemodel.get_namesID_from_store()

print(yate.start_response())

print(yate.include_header("Tabla comparativa de atletas"))

Titulos = ["Nombre", "Mejor Tiempo", "Diferencia de tiempo con el mejor", "Media de los 3 mejores tiempos",
           "Diferencia con la mejor media de tiempos"]
Tabla = Funciones.ObtenerDatosComparacion()
Tabla.insert(0, Titulos)

print(yate.simple_table(Tabla))

print(yate.include_footer({"Indice": "/cgi-bin/indice.py"}))
