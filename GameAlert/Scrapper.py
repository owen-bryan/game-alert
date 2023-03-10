from bs4 import BeautifulSoup
import requests
import Game
from datetime import datetime

def scrape (platform):
    base_url = 'https://www.metacritic.com/browse/games/release-date/coming-soon/{0}/date?page={1}'

    session = requests.Session()
    session.headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.131 Safari/537.36'

    page = session.get(base_url.format(platform,0))
    soup = BeautifulSoup(page.content, 'html.parser')

    last_page_span = soup.find ('a', class_="page_num")

    last_page = 0

    if last_page_span:
        last_page = int (last_page_span.text)
    else:
        last_page = 1

    results = []

    for i in range(last_page):
        page = session.get(base_url.format(platform,i))
        soup = BeautifulSoup(page.content, 'html.parser')
        gameList = soup.find_all ('tr', class_='')

        if gameList :
            for gameData in gameList:
                title = gameData.find ('h3').text

                releaseDate = datetime.strptime(gameData.find ('div', class_='clamp-details').find ('span', class_='').text,  '%B %d, %Y')

                game = Game.Game (title, releaseDate)
                
                results.append (game)

    return results

