import sqlite3
import settings
import datetime

def get_names_from_store():
    print(settings.database_path)
    connection = sqlite3.connect(settings.database_path)
    cursor = connection.cursor()
    results = cursor.execute("SELECT name FROM athletes")
    # results.fetchall() return a list of list
    names_list = [row[0] for row in results.fetchall()]
    connection.close()
#    print(names_list)
    return(names_list)
#get_names_from_store()


def get_athlete_from_id(athlete_id):

    connection = sqlite3.connect(settings.database_path)
    cursor = connection.cursor()

    results = cursor.execute("SELECT name, dob FROM athletes WHERE id={}".format(athlete_id))
    (name, dob) = results.fetchone()

    results = cursor.execute("SELECT value FROM timing_data WHERE athlete_id={}".format(athlete_id))
    data = [row[0] for row in results.fetchall()]
    times_ordered = sorted(data)
    if len(times_ordered) >=3:
        top3 = times_ordered[0:3]
    else:
        top3 = times_ordered[0:]

    response = {'Name': name, 'DOB': dob, 'data': data, 'top3': top3}
    connection.close()

    return(response)

print(get_athlete_from_id("1"))

def get_namesID_from_store():
    connection = sqlite3.connect(settings.database_path)
    cursor = connection.cursor()
    results = cursor.execute("SELECT name, ID FROM athletes")
    response = results.fetchall()
    connection.close()

    athletes_info = []
    for athlete_info in response:
        new_athlete = {'ID': athlete_info[1],
                       'name':athlete_info[0]}
        athletes_info.append(new_athlete)

    return(athletes_info)


def add_new_time_to_athelte(ID, new_time):
    connection = sqlite3.connect(settings.database_path)
    cursor = connection.cursor()
    cursor.execute("INSERT INTO timing_data (athlete_id, value) VALUES ({0}, {1})"
                   .format(ID, new_time))
    connection.commit()
    connection.close()

def AnadirAthleteDDBB(name):
    connection = sqlite3.connect(settings.database_path)
    cursor = connection.cursor()

    dob = datetime.datetime.utcnow().strftime('%Y-%m-%d')
    cursor.execute("INSERT INTO athletes (name, dob) VALUES ('{0}', '{1}')"
                   .format(name, dob))

    connection.commit()

    id = cursor.lastrowid
    connection.close()

    return id


def BorraTiempoAtleta(ID, Tiempo):
    connection = sqlite3.connect(settings.database_path)
    cursor = connection.cursor()

    cursor.execute("DELETE FROM timing_data WHERE "
                   "athlete_id={0} AND value={1}"
                   .format(ID, Tiempo))

    connection.commit()
    connection.close()

def BorraTodosTiemposAtleta(ID):
    connection = sqlite3.connect(settings.database_path)
    cursor = connection.cursor()

    cursor.execute("DELETE FROM timing_data WHERE "
                   "athlete_id={0}"
                   .format(ID))

    connection.commit()
    connection.close()

def BorraAtleta(ID):
    connection = sqlite3.connect(settings.database_path)
    cursor = connection.cursor()

    cursor.execute("DELETE FROM athletes WHERE "
                   "id={0}"
                   .format(ID))

    connection.commit()
    connection.close()