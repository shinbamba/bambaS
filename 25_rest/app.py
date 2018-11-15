from flask import Flask, render_template, request
import urllib
import json
app = Flask(__name__)

@app.route("/")
def yes():
	key = "872325fd34874a5f9525567053a9c3a3"
	url = "https://www.haloapi.com/metadata/h5/metadata/enemies?Accept-Language=en&subscription-key="
	url_all= url + key
	print('--------------------------------------------')
	print('PRINTING URL')
	print(url_all)
	print('--------------------------------------------')
	open = urllib.request.urlopen(url_all)
	r = open.read()
	dict = json.loads(r)
	print(json.loads(r))
	print('--------------------------------------------')
	print('--------------------------------------------')
	print(urllib.request.urlopen(url_all))
	return render_template("index.html", pic = dict[4]['largeIconImageUrl'], exp = "Halo 5 enemy: " + dict[4]['name'])



if __name__ == "__main__":
    app.debug = True
    app.run()
