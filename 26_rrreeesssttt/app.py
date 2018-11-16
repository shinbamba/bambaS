from flask import Flask, render_template
import urllib.request
from urllib.request import Request
import json
app = Flask(__name__)

def dictMaker(url):
	goodURL = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
	open = urllib.request.urlopen(goodURL)
	r = open.read()
	dict = json.loads(r)
	return dict


@app.route("/")
def yes():
	#MusixMatch API
	key0 = "00179cd70a622ee73f95af15a2d5c76f"
	url0 = "http://api.musixmatch.com/ws/1.1/track.lyrics.get?track_id=83015001&apikey="
	url_all0= url0 + key0

	dict0 = dictMaker(url_all0)
	
	#Pokemon TCG
	url1="https://api.pokemontcg.io/v1/cards?id=xyp-XY171"
	
	dict1 = dictMaker(url1)
	
	
	#Poem API
	url2= "https://www.poemist.com/api/v1/randompoems"
	dict2 = dictMaker(url2)
	print('------------------------------------------')
	print('PRINTING URL')
	print(url2)
	print('-------------------------------------------')
	print('PRINTING DICT')
	print(dict2)
	print('-------------------------------------------')
	print('-------------------------------------------')
	args = {}
	args["info0"] = dict0["message"]["body"]["lyrics"]["lyrics_body"]
	args['des0'] = "MUSIXMATCH API       Song name:       I Want it that Way"
	args['des1'] = "POKEMON TCG API      Pokemon name:   " + dict1['cards'][0]['name']
	args['info1'] = dict1['cards'][0]['imageUrl']
	args['des2'] = "POEM API      Poem name:   " + dict2[0]['title']
	args['info2'] = dict2[0]['content']
	
	
	
	return render_template("index.html", **args)



if __name__ == "__main__":
    app.debug = True
    app.run()
