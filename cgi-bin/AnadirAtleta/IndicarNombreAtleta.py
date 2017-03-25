from templates import yate


print(yate.start_response())

print(yate.include_header("Introducir el nombre del nuevo atleta"))

print(yate.start_form("IndicarTiempos.py"))

print(yate.text_field("nombre_atleta", "Introducir Nombre"))


print(yate.end_form("Aceptar"))

print(yate.include_footer({"Indice": "/cgi-bin/indice.py"}))