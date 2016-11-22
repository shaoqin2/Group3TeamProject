from passlib.hash import sha256_crypt
from flask import Flask, session
from connectdb import connection
from MySQLdb import escape_string as thwart
import gc

def register(username, password):
	c, conn = connection()
	hash_passwd = str(sha256_crypt.encrypt(password))
	
	x = c.execute("SELECT * FROM users WHERE username = (%s)", (thwart(username),))
	if int(x) > 0:
		return False
	else:
		c.execute("INSERT INTO users (username, password, collectedwords, totalscore) VALUES ( %s, %s, %s, %s )",(thwart(username) ,thwart(hash_passwd),0 ,0))
		conn.commit()
		c.close()
		conn.close()
		return True
	
def login(username, password):
	c, conn = connection()
	hash_passwd = str(sha256_crypt.encrypt(password))
	user = c.execute("SELECT * FROM users WHERE username = (%s)", (thwart(username),))
	if int(user)==0:
		return False
	user = c.fetchone()[2]
	if sha256_crypt.verify(password,user):
		gc.collect()
		return True
	else:
		gc.collect()
		return False
	