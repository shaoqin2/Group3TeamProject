from connectdb import connection
import MySQLdb
import random
import urllib2
import unirest
import json
def randomize_1000():
    c,conn = connection()
    baselong = 40.073410
    baselat = -88.304178
    count = 0
    for i in xrange(1900):
        templong = baselong + random.random()*0.06
        templat = baselat + random.random()*0.141
        word = str(urllib2.urlopen("http://randomword.setgetgo.com/get.php").read())
        url = 'https://wordsapiv1.p.mashape.com/words/' + 'incredible' + '/definitions'
        response = unirest.get("https://wordsapiv1.p.mashape.com/words/%s/definitions"%word,
          headers={
            "X-Mashape-Key": "sDU8ttxskJmshjTCNb5eIoOF6NQ3p1OylfwjsnQ7yJzrrzYe9o",
            "Accept": "application/json"
          }
        )
        try:
            defi =  response.body['definitions'][0]['definition']
            c.execute("INSERT INTO wordlocation (word,longitude,latitude,definition,lang) VALUES(%s,%s,%s,%s,%s)",(word,templong,templat,defi,'english'))
	    print count
	    count += 1
        except:
            continue
        
    conn.commit()
    c.close()
    return
randomize_1000()
