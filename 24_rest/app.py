from flask import Flask, render_template, request
import urllib
import json
app = Flask(__name__)

@app.route("/")
def yes():
	key = "https://api.nasa.gov/planetary/apod?date=2018-11-10&api_key=gpIAYj6MqHViKv7ezcm7fLB7uFykIcONmM1SpOF3"
	url = urllib.request.urlopen(key)
	r = url.read()
	dict = json.loads(r)
	print(json.loads(r))
	print(urllib.request.urlopen(key))
	return render_template("index.html", pic = dict['url'], exp = dict['explanation'])



if __name__ == "__main__":
    app.debug = True
    app.run()
