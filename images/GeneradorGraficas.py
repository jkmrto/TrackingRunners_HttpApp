import matplotlib.pyplot as plt


def GenerarGraficasTiempos(athlete_info, path):

    X = list(range(1, len(athlete_info['data']) + 1, 1))

    plt.plot(X, athlete_info['data'], 'ro')

    plt.xlabel('Numero  de Marca')
    plt.ylabel('Tiempo (min)')
    plt.title('Evolución de las marcas de {}'.format(athlete_info['Name']))
    plt.xticks(X)
    plt.savefig(path)


#GenerarGraficasTiempos(["1.3", "2.3", "4.5"], "hola")