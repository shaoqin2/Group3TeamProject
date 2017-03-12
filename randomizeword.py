from connectdb import connection
import MySQLdb
import random
import urllib2
import unirest


def randomize(number):
    c, conn = connection()
    base_longitude = 40.073410
    base_latitude = -88.304178

    # there is a chance the retrieved word has no definition. count will keep track of the number of actual valid word
    count = 0
    for i in range(number):
        temp_longitude = base_longitude + random.random() * 0.06
        temp_latitude = base_latitude + random.random() * 0.141
        word = str(urllib2.urlopen("http://randomword.setgetgo.com/get.php").read())
        response = unirest.get("https://wordsapiv1.p.mashape.com/words/%s/definitions" % word,
                               headers={
                                   "X-Mashape-Key": "sDU8ttxskJmshjTCNb5eIoOF6NQ3p1OylfwjsnQ7yJzrrzYe9o",
                                   "Accept": "application/json"
                               }
                               )
        try:
            definition = response.body['definitions'][0]['definition']
            c.execute("INSERT INTO wordlocation (word,longitude,latitude,definition,lang) VALUES(%s,%s,%s,%s,%s)",
                      (word, temp_longitude, temp_latitude, definition, 'english'))
            count += 1
            if count % 50 == 0:   # print every 50 words to demonstrate the progress
                print(count)
        except Exception:
            # the word has no definition. Do nothing
            continue

    conn.commit()
    c.close()
    return


if __name__ == '__main__':
    number = int(input('Please input how many words you want to randomize on the map. Everyday limit is 500'))
    randomize(number)
