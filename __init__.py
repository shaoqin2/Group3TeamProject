from flask import Flask, request, session
from operation import get_all_word, post_word, collect_word, get_user_statistics
from userlogin import register, login
import logging

# TODO the connectdb module should be implemented when deploying on the server
# from connectdb import connection

app = Flask(__name__)
BAD_REQUEST_INFO = '''
bad request parameters, please refer to documentation at
https://github.com/shaoqin2/Group3TeamProject.git
'''


@app.route('/getWord', methods=['GET'])
def get_all_word_endpoint():
    """
    the endpoint that handles get word endpoint. Will query the database and return
    a json string representing all word within the current radius. If ids are specified,
    the specified IDs will not be returned

    :return: the json representation of all the word
    """
    if all(arg in request.args for arg in ['longitude', 'latitude', 'radius', 'ids']):
        longitude = float(request.args['longitude'])
        latitude = float(request.args['latitude'])
        radius = float(request.args['radius'])
        ids = request.args.getlist('ids')
        return get_all_word(longitude, latitude, radius, ids)
    else:
        return BAD_REQUEST_INFO


@app.route('/postWord', methods=['GET', 'POST'])
def post_word_endpoint():
    """
    the endpoint that handles the post word endpoint. Allow user to post a word on the map

    :return: a string representing if the word is successfully posted on the map
    """
    if all(arg in request.args for arg in ['longitude', 'latitude', 'word', 'definition']):
            longitude = float(request.args['longitude'])
            latitude = float(request.args['latitude'])
            word = request.args['word']
            definition = request.args['definition']
            return post_word(longitude, latitude, word, definition)
    else:
        return BAD_REQUEST_INFO


@app.route('/login', methods=['GET', 'POST'])
def login_endpoint():
    """
    the endpoint that handles user login.

    :return: return a string representing if the user is successfully logged in
    """
    if all(arg in request.args for arg in ['username', 'password']):
        username = str(request.args['username'])
        password = str(request.args['password'])
        if login(username, password):
            session['logged_in'] = True
            session['username'] = username
            return 'User successfully logged in as ' + username
        else:
            return 'wrong username or password'
    else:
        return BAD_REQUEST_INFO


@app.route('/register', methods=['GET', 'POST'])
def register_endpoint():
    """
    the endpoint that handles user registration. Will check if the username is already
    taken

    :return: a string message representing if the user is successfully registered
    """
    if all(arg in request.args for arg in ['username', 'password']):
        username = str(request.args['username'])
        password = str(request.args['password'])
        if register(username, password):
            return 'User successfully registered as ' + username
        else:
            return 'username already taken'
    else:
        return BAD_REQUEST_INFO


@app.route('/collect', methods=['GET', 'POST'])
def collect_word_endpoint():
    """
    the endpoint that let the user collect a word

    :return: a string representing if the collection is successful
    """
    if all(arg in request.args for arg in ['username', 'password']):
        username = str(request.args['username'])
        password = str(request.args['password'])
        return collect_word(username, password)
    else:
        return BAD_REQUEST_INFO


@app.route('/getstat', methods=['GET'])
def get_stat_endpoint():
    """
    the endpoint that returns all the user statistic

    :return:  a json representation of all the user statistics
    """
    if 'username' in request.args:
        username = request.args['username']
        return get_user_statistics(username)
    else:
        return BAD_REQUEST_INFO


if __name__ == '__main__':
    app.run(debug=True)
    logging.basicConfig(filename='/home/logs.txt', level=logging.DEBUG)
