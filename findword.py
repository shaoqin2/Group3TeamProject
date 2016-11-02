
import MySQLdb
from connectdb import connection
import json
def fword(lon,lat,radius,ids):
    try:
        result = {}
        c, conn = connection()
        c.execute("SELECT * FROM wordlocation WHERE ((longitude-%s)*(longitude-%s)+(latitude-%s)*(latitude-%s))<%s",(lon,lon,lat,lat,radius))
        words = []
        for row in c.fetchall():
            t = {}
            if row[0] in ids:
                continue
            t["name"] = row[1]
            t["definition"] = row[4]
            t["id"] = row[0]
            t["lat"] = row[2]
            t["long"] = row[3]
            words.append(t)
        result["words"] = words
        j = json.dumps(result)
        return j
    except Exception as e:
        return str(e)

def pword(lat,lng,word,definition):
	try:
		c, conn = connection()
		c.execute("INSERT INTO wordlocation (word,longitude,latitude,definition,lang) VALUES(%s,%s,%s,%s,%s)",
		(word,lat,lng,definition,'english'))
		conn.commit()
		return "success!"
	except Exception as e:
		return str(e)
