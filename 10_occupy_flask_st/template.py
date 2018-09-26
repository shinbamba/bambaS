#Team Matcha Dog -- Shin Bamba, Joyce Liao
#SoftDev1 pd8
#K10 -- Jinja Tuning
#2018-09-22

from util import occupations
from flask import Flask ,  render_template
app = Flask(__name__) #instantiates the Flask class using a constructor


@app.route("/")
def homepage():
    return "Hello, please go to /occupations"
@app.route("/occupations")
def display_occ():
    return render_template("template.html",
                           title = "Occupations" ,
			   head = " Table containing information about occupations in the United States (courtesy of Mr. Brooks) -Mr.Brown",
                           randOccupation = occupations.pick_job(dictionary),
                           dict = dictionary)
	

dictionary = occupations.table('occupations.csv') #dictionary created from csv file	
	
if (__name__) == ("__main__"):
    app.debug = True
    app.run()
