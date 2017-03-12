from passlib.hash import sha256_crypt
from flask import Flask, session
from connectdb import connection
from MySQLdb import escape_string as thwart
import gc


def register(username, password):
    c, conn = connection()
    hashed_password = str(sha256_crypt.encrypt(password))

    x = c.execute("SELECT * FROM users WHERE username = (%s)", (thwart(username),))
    # int(x) represents the number of users already registered under this username
    if int(x) > 0:
        return False
    else:
        c.execute("INSERT INTO users (username, password, collectedwords, totalscore) VALUES ( %s, %s, %s, %s )",
                  (thwart(username), thwart(hashed_password), 0, 0))
        c.execute("INSERT INTO userstat (username, completed, score ) VALUES (%s,%s,%s)", (thwart(username), "", 0))
        conn.commit()
        c.close()
        conn.close()
        return True


def login(username, password):
    c, conn = connection()
    hashed_password = str(sha256_crypt.encrypt(password))
    user = c.execute("SELECT * FROM users WHERE username = (%s)", (thwart(username),))
    if int(user) == 0:
        return False
    user = c.fetchone()[2]
    if sha256_crypt.verify(hashed_password, user):
        gc.collect()
        return True
    else:
        gc.collect()
        return False
