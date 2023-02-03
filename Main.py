
from Scrapper import scrape
from DB import  storeInDB, getGamesFromDB, clearOld

from Alerts import sendAlertOne, sendAlerts

from datetime import datetime

    
def dailyAlerts ():
    games = getGamesFromDB (datetime.today())

    sendAlerts (games)

def dailyScrape ():
    storeInDB ((scrape ('ps5'), 'ps5'))
    storeInDB ((scrape ('switch'), 'switch'))
    storeInDB ((scrape ('xbox-series-x'), 'xbox-series-x'))

def dailyClear ():
    clearOld (datetime.today())

def main ():
    dailyScrape ()
    dailyAlerts ()
    dailyClear ()


if __name__ == "__main__":
    main()