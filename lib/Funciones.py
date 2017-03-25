from lib import athletemodel

def ObtenerValorNumericoSiEsPosible(valor):
    try:
        return float(valor)
    except:
        return None


def ObtenerDatosComparacion():
    list_athlete_ID = athletemodel.get_namesID_from_store()
    list_dictionaries_athletes = []

    for athlete in list_athlete_ID:
        athlete_aux = athletemodel.get_athlete_from_id(athlete['ID'])
        athlete_aux['data'] = [float(dato) for dato in athlete_aux['data']]
        athlete_aux['top3'] = [float(dato) for dato in athlete_aux['top3']]
        athlete_aux['mean_top3'] = sum(athlete_aux['top3']) / len(athlete_aux['top3'])
        list_dictionaries_athletes.append(athlete_aux)


    list_ordered = sorted(list_dictionaries_athletes, key=lambda x: x['top3'][0])
    mejor_tiempo = list_ordered[0]['top3'][0]

    list_ordered_media_mejores = sorted(list_dictionaries_athletes, key=lambda x: x['mean_top3'])
    mejor_media = list_ordered_media_mejores[0]['mean_top3']

    lista_final = []
    for atleta in list_ordered:
        lista_aux = []
        lista_aux.append(atleta['Name'])
        lista_aux.append(atleta['top3'][0])
        lista_aux.append(atleta['top3'][0] - mejor_tiempo)
        lista_aux.append(atleta['mean_top3'])
        lista_aux.append(atleta['mean_top3'] - mejor_media)
        lista_final.append(lista_aux)

    return lista_final
