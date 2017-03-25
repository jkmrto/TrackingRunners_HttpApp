'''
Created on 15 dic. 2016

@author: Manuel
'''
import glob
import sqlite3

from old_lib_pickle import athletemodel

connection = sqlite3.connect('../coachdata.sqlite')
cursor = connection.cursor()
data_files = glob.glob("../data/*.txt")

athletes = athletemodel.put_to_store(data_files)

for each_ath in athletes:
    name = athletes[each_ath].name
    dob = athletes[each_ath].dob
    cursor.execute("INSERT INTO athletes (name, dob) VALUES (?, ?)", 
                   (name, dob))
    connection.commit()

connection.close()
