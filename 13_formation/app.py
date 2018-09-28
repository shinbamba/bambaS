from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("page.html")

@app.route("/auth")
def woah():
	print(app)
	print(request)
	print(request.args)
	print(request.args['username'])
	print(request.headers)
	print(request.method)
	return "This is your username: " + request.args['username'] + "<br> Greetings Earthling. Welcome to this page." + "<br> used " + request.method
app.debug = True
app.run()
