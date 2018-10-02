from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("page.html")

@app.route("/auth", methods = ["POST"])
def woah():
	print(app)
	print(request)
	print(request.method)
	print(request.form)
	if request.method == 'POST': 
		return render_template("response.html",
				username = "Username: " + request.form["username"],
				method = "Used " + request.method,
				message = "Welcome, " + request.form['username'])
	else:
		return render_template("response.html",
				username = "Please submit a username")
	
if __name__ == "__main__":
    app.debug = True
    app.run()
