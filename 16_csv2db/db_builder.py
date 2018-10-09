# Team Nesquik - Shin Bamba & Derek Song
# Soft Dev - PD8
# K#16 - No Trouble
# 2018 - 10 - 4

import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O


DB_FILE = "discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops

#==========================================================
#INSERT YOUR POPULATE CODE IN THIS ZONE
c.execute("DROP TABLE peeps;") # Gets rid of peeps table if it already exists
c.execute("DROP TABLE courses;") # Gets rid of courses table if it already exists

c.execute("CREATE TABLE peeps(name TEXT, age INTEGER, id INTEGER);") # Create peeps
c.execute("CREATE TABLE courses(code TEXT, mark INTEGER, id INTEGER)") # Create courses

with open ('data/peeps.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for line in reader:
        c.execute("INSERT INTO peeps VALUES( '"+ line['name'] +"', "+ line['age'] +", " + line['id'] + ");")

with open ('data/courses.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for line in reader:
        c.execute("INSERT INTO courses VALUES( '"+ line['code'] +"', "+ line['mark'] +", " + line['id'] + ");")

    
#==========================================================

db.commit() #save changes
db.close()  #close database


