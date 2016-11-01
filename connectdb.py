
import MySQLdb
def connection():
	conn = MySQLdb.connect(host="localhost",
				user="root",
				passwd="Bbysq981015",
				db="wordlocation")
	c = conn.cursor()
	return c,conn

