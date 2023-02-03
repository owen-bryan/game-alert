
from GameAlert.Scrapper import scrape
from DB import  storeInDB, getGamesFromDB, clearOld

from Alerts import sendAlertOne, sendAlerts

from datetime import datetime

def alerts (platform):
    games = getGamesFromDB (datetime.today(), platform)
    sendAlerts (games, platform)

def dailyAlerts ():
    alerts ('ps5')
    alerts ('switch')
    alerts ('xbox-series-x')

def dailyScrape ():
    ps5 = scrape ('ps5')
    switch = scrape ('switch')
    xbox_series_x = scrape ('xbox-series-x')
    storeInDB (ps5, 'ps5')
    storeInDB (switch, 'switch')
    storeInDB (xbox_series_x, 'xbox-series-x')

def dailyClear ():
    clearOld (datetime.today())

def main ():
    dailyScrape ()
    dailyAlerts ()
    dailyClear ()


if __name__ == "__main__":
    main()