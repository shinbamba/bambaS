#Shin Bamba
#SoftDev pd 8
#08_lemme_flask_u_sumpm
#2018-09-19
from flask import Flask
app = Flask(__name__) #instantiates the Flask class using a constructor

@app.route('/route1') #route 1
def nameOfThing():
	return 'Please Work'

@app.route('/route2') #route 2
def anotherNameOfThing():
	return 'This another route'
	
@app.route('/route3') #route 3
def name3BecauseIHaveNoIdeasLeft():
	return 'I do believe this is route 3'
	
app.debug = True
app.run()
