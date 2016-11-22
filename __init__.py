from flask import Flask, request, url_for, session, redirect
from connectdb import connection
from findword import fword,pword
from userlogin import register as rg, login as lg

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
		
		
@app.route("/login",methods=["GET","POST"])
def login():
	try:
		if 'username' in request.args and 'password' in request.args:
			username = str(request.args['username'])
			password = str(request.args['password'])
			if lg(username,password):
				session['logged_in'] = True
				session['username'] = username
				return "User is now logged_in"
			else:
				return "wrong username or password"
		else:
			return "bad request"
	except Exception as e:
		return (str(e))
@app.route("/register",methods=["GET","POST"])
def register():
	try:
		if 'username' in request.args and 'password' in request.args:
			username = str(request.args['username'])
			password = str(request.args['password'])
			if rg(username,password):
				return ("User successfully registered as "+username)
			else:
				return ("Failed to register username")
		else:
			return("the parameters are wrong!")
	except Exception as e:
		return (str(e))
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	

