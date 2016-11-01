'''import MySQLdb
from connectdb import connection
import json

def fword(lon,lat,radius,ids):
    #retrieve all datas in the vicinity of this point
    #filter the data to take off all existing ids
    #return a json string to init.py
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
			t["lat"] = row[3]
			t["long"] = row[2]
			words.append(t)
		result["words"] = words
		j_result = json.dumps(result)
		return j_result
	except Exception as e:
		return str(e)
'''
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