from connectdb import connection
import MySQLdb
import random
import urllib2
def randomize_1000():
	try:	
		c,conn = connection()
		baselong = 40.073410
		baselat = -88.304178
		for i in xrange(15):
			templong = baselong + random.random()*0.06
			templat = baselat + random.random()*0.141
			word = str(urllib2.urlopen("http://randomword.setgetgo.com/get.php").read())
			c.execute("INSERT INTO wordlocation (word,longitude,latitude,definition,lang) VALUES(%s,%s,%s,%s,%s)",
			(word,templong,templat,'I honestly dont know','english'))
		conn.commit()
		c.execute("SELECT * FROM wordlocation")
		for row in c.fetchall():
			print str(row)
		c.close()
		return
	except Exception as e:
		return str(e)
randomize_1000()
