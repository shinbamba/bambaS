from flask import Flask, render_template, request
import urllib
app = Flask(__name__)

@app.route("/")
def yes():
    key = "https://api.nasa.gov/planetary/apod?api_key=gpIAYj6MqHViKv7ezcm7fLB7uFykIcONmM1SpOF3"
    print(urllib.request.urlopen(key))
    return render_template("index.html")




if __name__ == "__main__":
    app.debug = True
    app.run()
