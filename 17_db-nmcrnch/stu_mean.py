#iForgot (Derek Chan & Shin Bamba)
#SoftDev1 pd8
#K17 Average
#2018-10-09

import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O

DB_FILE="curbur.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops

#==========================================================
#INSERT YOUR POPULATE CODE IN THIS ZONE

# c.execute("DROP TABLE peeps;") # Gets rid of peeps table if it already exists
# c.execute("DROP TABLE courses;") # Gets rid of courses table if it already exists
# c.execute("DROP TABLE id_avg;")

def create_table(file_location, table_name, val1, val2, val3):
    c.execute("CREATE TABLE {0} ({1} TEXT, {2} INTEGER, {3} INTEGER);".format(table_name, val1, val2, val3))    #create peeps table
    with open(file_location) as csvfile: #opens the file for reading as a csvfile
        reader = csv.DictReader(csvfile, fieldnames = ("x", "y", "z"))
        next(reader)
        for row in reader:
            c.execute("INSERT INTO {0} VALUES( '{1}', {2}, {3});".format(table_name, row['x'], row['y'], row['z']))

create_table("data/peeps.csv", "peeps", "name", "age", "id")
create_table('data/courses.csv', "courses", "code", "mark", "id")

c.execute("SELECT name, peeps.id, mark FROM peeps, courses WHERE peeps.id = courses.id;")

def averager():
    id_avg = {}
    for thing in c:
        print(thing)
        if thing[1] in id_avg:
            id_avg[thing[1]].append(thing[2])
        else:
            id_avg[thing[1]] = [thing[2]]
    for id in id_avg.keys():
        id_avg[id] = sum(id_avg[id]) / float(len(id_avg[id]))
    return id_avg


id_avg = averager()

c.execute("CREATE TABLE {0} ({1} INTEGER, {2} INTEGER);".format("id_avg", "id", 'avg'))    #create peeps table
for key in id_avg.keys():
    c.execute("INSERT INTO {0} VALUES( '{1}', {2});".format("id_avg", key, id_avg[key]))

def add_row(course_name, mark, id):
    c.execute("INSERT INTO courses VALUES( '{0}', {1}, {2});".format(course_name, mark, id))

add_row('english', 901, 11)


# for x in c:
#    print(x)

#==========================================================

db.commit() #save changes
db.close()  #close database
