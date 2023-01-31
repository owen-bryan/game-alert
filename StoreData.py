import csv
import pymongo

import os
from dotenv import load_dotenv, find_dotenv

def writeToFile (data, platform = ""):
    with open (platform +".csv", 'w', newline='') as csvfile:
        dataWritter = csv.writer (csvfile)
        
        for game in data:
            dataWritter.writerow([game.title, game.releaseDate])

def storeInDB (data, platform = ""):
    try:
        load_dotenv(find_dotenv())
        mongo_url = os.getenv('MONGO_URL')

        print ("USING DATABASE AT {0}".format(mongo_url))

        client = pymongo.MongoClient (mongo_url)
        GameAlert = client ['GameAlert']
        releaseDates = GameAlert ['ReleaseDates']

        for game in data:
            if releaseDates.count_documents ({"title" : game.title, "release_date": game.releaseDate, "platform": platform}, limit = 1) == 0:
                releaseDates.insert_one ({"title": game.title, "release_date"  : game.releaseDate, "platform" : platform, "released" : False})
    except KeyError:
        print ("Key err no key called MONGO_URL set.")
    except TypeError:
        print ("type err")
    except:
        print ("Error has occured")

