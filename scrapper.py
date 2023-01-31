from bs4 import BeautifulSoup
import requests
import Game


def scrape (platform):
    base_url = 'https://www.metacritic.com/browse/games/release-date/coming-soon/{0}/date?page={1}'

    s = requests.Session()
    s.headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.131 Safari/537.36'

    page = s.get(base_url.format(platform,0))
    soup = BeautifulSoup(page.content, 'html.parser')

    last_page_span = soup.find ('a', class_="page_num")

    # print (last_page.text)
    last_page = 0

    if last_page_span:
        last_page = int (last_page_span.text)
    else:
        last_page = 1

    results = []

    for i in range(last_page):
        page = s.get(base_url.format(platform,i))
        soup = BeautifulSoup(page.content, 'html.parser')
        gameList = soup.find_all ('tr', class_='')

        if gameList :
            # print (gameLists)

            # gameList = gameList.find_all ('tr', class_ = '')
            # print ("page: {}".format(i))
            for gameData in gameList:
                title = gameData.find ('h3').text

                releaseDate = gameData.find ('div', class_='clamp-details').find ('span', class_='').text

                game = Game.Game (title, releaseDate)

                results.append (game)

                # print ("{0} Releasing: {1}".format (title, releaseDate))

        # print (gameList.find_all ('tr', class_ = ''))
    
    return results

