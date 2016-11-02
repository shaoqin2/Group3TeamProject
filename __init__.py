from flask import Flask, request
from connectdb import connection
from findword import fword,pword
app = Flask(__name__)

if __name__ == "__main__":
    app.run(debug=True)
@app.route("/")
def hello():
	return "this bad boy is working!"
@app.route("/getWord", methods=['GET'])
def getWord():
	if 'long' in request.args and 'lat' in request.args and 'radius' in request.args and 'ids' in request.args:
		longitude = float(request.args["long"])
		latitude = float(request.args["lat"])
		radius = float(request.args["radius"])
		ids = request.args.getlist("ids")
		try:
			j = fword(longitude,latitude,radius,ids)
			return j
		except Exception as e:
			return str(e)
	else:
		return "bad request"

@app.route("/postWord",methods=["GET","POST"])
def postWord():
	if 'lat' in request.args and 'long' in request.args and 'word' in request.args and 'definition' in request.args:
		try:
			lat = float(request.args['lat'])
			lng = float(request.args['long'])
			word = str(request.args['word'])
			definition = str(request.args['definition'])
			return pword(lat,lng,word,definition)
		except Exception as e:
			return str(e)
	else:
		return "badPost"

