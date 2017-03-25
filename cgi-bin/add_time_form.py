import glob

from lib import athletemodel
from templates import yate

data_files = glob.glob("data/*.txt")
athletes_info = athletemodel.get_namesID_from_store()

print(yate.start_response())

print(yate.include_header("Coach Martin's List of Athletes"))

print(yate.start_form("adding_time.py"))

print(yate.para("Select an athlete from the list to add time:"))
for each_athlete in athletes_info:
    print(yate.radio_button("which_athlete", each_athlete['name'], each_athlete['ID']))

print(yate.text_field("athlete_new_time", "athlete_new_time"))

print(yate.end_form("Select"))

print(yate.include_footer({"Home": "/index.html", "Show timing athlete": "generate_list.py"}))




