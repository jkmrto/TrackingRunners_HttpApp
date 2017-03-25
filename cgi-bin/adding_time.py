import cgi
import cgitb

from lib import athletemodel
from templates import yate

cgitb.enable()

form_data = cgi.FieldStorage()

athlete_ID = form_data['which_athlete'].value
athlete_new_time = form_data['athlete_new_time'].value

print(yate.start_response())

print(yate.include_header("Coach Martin's List of Athletes"))



try:
    athletemodel.add_new_time_to_athelte(athlete_ID, athlete_new_time)
    print(yate.para("New time: {0} added correctly to athleteID: {1}"
                    .format(athlete_new_time, athlete_ID)))
except Exception as e:
    print(yate.para("Error adding new time" + str(e)))

print(yate.include_footer({"Home": "/index.html",
                           "Add timing to athlete": "add_time_form.py",
                           "Show time of athlete":""}))