import sqlite3
from lib import athletemodel

connection = sqlite3.connect('../coachdata.sqlite')
cursor = connection.cursor()
athletes = athletemodel.get_from_store()
for each_ath in athletes:
    name = athletes[each_ath].name
dob = athletes[each_ath].dob
print(name, " - ", dob)
cursor.execute("SELECT id from athletes WHERE name=? AND dob=?", (name, dob))
the_current_id = cursor.fetchone()[0]  # fetchone() return a list
print(the_current_id)
for each_time in athletes[each_ath].clean_data:
    print(the_current_id, each_time)
cursor.execute("INSERT INTO timing_data (athlete_id, value) VALUES (?, ?)",
               (the_current_id, each_time))
connection.commit()
connection.close()
