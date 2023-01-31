
from Scrapper import scrape
from StoreData import writeToFile, storeInDB

from Alerts import sendAlert

def main ():
    # scrape ("ps5")
    # scrape ("switch")
    # scrape ("xbox-series-x")
    # writeToFile (scrape("ps5"), "ps5")
   games = scrape ("ps5")
   sendAlert (games [0])
   

if __name__ == "__main__":
    main ()