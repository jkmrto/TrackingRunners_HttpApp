import cgi
import cgitb
from templates import yate
from lib.Funciones import ObtenerValorNumericoSiEsPosible
from lib import athletemodel

cgitb.enable()
form_data = cgi.FieldStorage()
nombre = form_data["Nombre"].value

EtiquetasTiempo = ['tiempo1', 'tiempo2', 'tiempo3', 'tiempo4', 'tiempo5',
                   'tiempo6', 'tiempo7', 'tiempo8', 'tiempo9', 'tiempo10']

TiemposIndicados = []
for EtiquetaEvaluada in EtiquetasTiempo:
    try:
        ValorNumerico = ObtenerValorNumericoSiEsPosible(form_data[EtiquetaEvaluada].value)
        if isinstance(ValorNumerico, float):
             TiemposIndicados.append(ValorNumerico)
    except:
        pass

print(yate.start_response())

ID_asignado = athletemodel.AnadirAthleteDDBB(nombre)
print(yate.header("Añadido el atleta {0} con ID {1}".format(nombre, ID_asignado)))

for tiempo in TiemposIndicados:

    try:
        athletemodel.add_new_time_to_athelte(ID_asignado, tiempo)
        print(yate.para("Tiempo {} añadido correctamente".format(tiempo)))
    except:
        print(yate.para("Error añadiento el tiempo {}".format(tiempo)))

print(yate.include_footer({"Indice": "/cgi-bin/indice.py"}))
