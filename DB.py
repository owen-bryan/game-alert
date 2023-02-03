import csv
import pymongo

import os
from dotenv import load_dotenv, find_dotenv

from datetime import datetime
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
        print ("type err.")
    except:
        print ("Unknown err has occured.")

def deleteReleasedGames (platform = ""):
    try:
        load_dotenv (find_dotenv())
        mongo_url = os.getenv('MONGO_URL')

        print ('USING DATABASE AT {0}'.format (mongo_url))

        client = pymongo.MongoClient (mongo_url)
        GameAlert = client ['GameAlert']
        releaseDates = GameAlert ['ReleaseDates']

        # releaseDates.delete_many ()
    except KeyError:
        print ("Key err no key called MONGO_URL set.")
    except Exception as e:
        print ("Unknown err has occured.", str (e))


def getGamesFromDB (date):
    try:
        load_dotenv (find_dotenv())
        mongo_url = os.getenv('MONGO_URL')

        print ('USING DATABASE AT {0}'.format (mongo_url))

        client = pymongo.MongoClient (mongo_url)
        GameAlert = client ['GameAlert']
        releaseDates = GameAlert ['ReleaseDates']


        # print (datetime.now())
        results = releaseDates.find({'release_date' : {'$lte' : date}})

        return results
    except Exception as e:
        print ("Unknown err has occured.", str(e))

def clearOld (date):
    try:
        load_dotenv (find_dotenv())
        mongo_url = os.getenv('MONGO_URL')

        print ('USING DATABASE AT {0}'.format (mongo_url))

        client = pymongo.MongoClient (mongo_url)
        GameAlert = client ['GameAlert']
        releaseDates = GameAlert ['ReleaseDates']


        # print (datetime.now())
        results = releaseDates.delete_many({'release_date' : {'$lte' : date}})

        if results.deleted_count > 0:
            return True

        return False
    except Exception as e:
        print ("Unknown err has occured.", str(e))