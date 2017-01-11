import MySQLdb
from connectdb import connection
from MySQLdb import escape_string as thwart
import json
import logging

logging.basicConfig(filename='operation_log.txt',level=logging.DEBUG)

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
        c.close()
        conn.close()
        return j
    except Exception as e:
        logging.info(str(e))

def pword(lat,lng,word,definition):
    try:
        c, conn = connection()
        c.execute("INSERT INTO wordlocation (word,longitude,latitude,definition,lang) VALUES(%s,%s,%s,%s,%s)",
        (thwart(word),lat,lng,thwart(definition),'english'))
        conn.commit()
        c.close()
        conn.close()
        return "success!"
    except Exception as e:
        logging.info(str(e))

def cword(word, username):
    try:
        c, conn = connection()
        blank_word = " " + word
        c.execute("UPDATE userstat SET completed=CONCAT(IFNULL(completed,''), %s) , score=score+1 WHERE username=%s;",(blank_word, username))
        conn.commit()
        c.close()
        conn.close()
        return "successful collect"
    except Exception as e:
        logging.info(str(e))

def stat(username):
    try:
        c, conn = connection()
        c.execute("SELECT * FROM userstat WHERE username=%s", (username,))
        dict = {}
        u = c.fetchone()
        dict['username'] = username
        dict['words'] = str(u[1]).split()
        dict['score'] = u[2]
        return json.dumps(dict)
    except Exception as e:
        logging.info(str(e))
