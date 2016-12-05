from flask import Flask, request, url_for, session, redirect
from connectdb import connection
from operation import fword, pword, cword, stat
from userlogin import register as rg, login as lg

app = Flask(__name__)

if __name__ == "__main__":
    app.run(debug=True)
@app.route("/")
def hello():
    try:
        if session['logged_in']:
            return (session['username'])
    except Exception as e:
        return str(e)
	return ("this bad boy is working!")

@app.route("/getWord", methods=['GET'])
def getWord():
	if 'long' in request.args and 'lat' in request.args and 'radius' in request.args and 'ids' in request.args:
		try:
			longitude = float(request.args["long"])
			latitude = float(request.args["lat"])
			radius = float(request.args["radius"])
			ids = request.args.getlist("ids")
		except:
			return "Bad Request Parameters"
		try:
			allwords_json = fword(longitude,latitude,radius,ids)
			return allwords_json
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
				return "User successfully logged in as "+username
			else:
				return "wrong username or password"
		else:
			return "bad request"
	except Exception as e:
		return (str(e))

@app.route("/register", methods=["GET","POST"])
def register():
	try:
		if 'username' in request.args and 'password' in request.args:
			username = str(request.args['username'])
			password = str(request.args['password'])
			if rg(username,password):
				return ("User successfully registered as "+username)
			else:
				return ("username already taken")
		else:
			return("the parameters are wrong!")
	except Exception as e:
		return (str(e))


@app.route("/collect", methods=["GET","POST"])
def collect():
	try:
		if 'word' in request.args and session['logged_in']:
			try:
				return cword(request.args['word'], session['username'])
			except Exception as e:
				return str(e)
		else:
			return "bad request"
	except Exception as e:
		return str(e)

@app.route("/getstat", methods=["GET","POST"])
def getstat():
    try:
        if session['logged_in']:
			stat_json = stat(session['username'])
			return stat_json
        else:
            return "bad request"
    except Exception as e:
        return str(e)
