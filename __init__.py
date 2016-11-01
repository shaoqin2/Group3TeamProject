from flask import Flask, request
from connectdb import connection
from findword import fword
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


