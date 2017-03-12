import MySQLdb
from connectdb import connection
from MySQLdb import escape_string as thwart
import json
import logging

logging.basicConfig(filename='operation_log.txt', level=logging.DEBUG)


def get_all_word(longitude, latitude, radius, ids):
    try:
        result = {}
        c, conn = connection()
        c.execute("SELECT * FROM wordlocation WHERE ((longitude-%s)*(longitude-%s)+(latitude-%s)*(latitude-%s))<%s",
                  (longitude, longitude, latitude, latitude, radius))
        words = []
        for row in c.fetchall():
            word = {}
            if row[0] in ids:
                continue
            word["name"] = row[1]
            word["definition"] = row[4]
            word["id"] = row[0]
            word["lat"] = row[2]
            word["long"] = row[3]
            words.append(word)
        result["words"] = words
        json_response = json.dumps(result)
        c.close()
        conn.close()
        return json_response
    # this is a general catch all because there aren't enough insight what can go wrong in a db operation
    except Exception as e:
        logging.info(str(e))


def post_word(longitude, latitude, word, definition):
    try:
        c, conn = connection()
        c.execute("INSERT INTO wordlocation (word,longitude,latitude,definition,lang) VALUES(%s,%s,%s,%s,%s)",
                  (thwart(word), longitude, latitude, thwart(definition), 'english'))
        conn.commit()
        c.close()
        conn.close()
        return "success!"
    except Exception as e:
        logging.info(str(e))


def collect_word(word, username):
    try:
        c, conn = connection()
        blank_word = " " + word
        c.execute("UPDATE userstat SET completed=CONCAT(IFNULL(completed,''), %s) , score=score+1 WHERE username=%s;",
                  (blank_word, username))
        conn.commit()
        c.close()
        conn.close()
        return "successful collect"
    except Exception as e:
        logging.info(str(e))


def get_user_statistics(username):
    try:
        c, conn = connection()
        c.execute("SELECT * FROM userstat WHERE username=%s", (username,))
        response = {}
        user_info = c.fetchone()
        response['username'] = username
        response['words'] = str(user_info[1]).split()
        response['score'] = user_info[2]
        return json.dumps(response)
    except Exception as e:
        logging.info(str(e))
