from bs4 import BeautifulSoup
import requests


def scrape (platform):
    base_url = 'https://www.metacritic.com/browse/games/release-date/coming-soon/{0}/date?page={1}'

    s = requests.Session()
    s.headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.131 Safari/537.36'

    page = s.get(base_url.format(platform,0))
    soup = BeautifulSoup(page.content, 'html.parser')

    last_page = soup.find ('a', class_="page_num").text

    # print (last_page.text)

    last_page = int (last_page)

    for i in range(last_page):
        page = s.get(base_url.format(platform,i))
        soup = BeautifulSoup(page.content, 'html.parser')
        gameList = soup.find_all ('tr', class_='')


        # print (gameLists)

        # gameList = gameList.find_all ('tr', class_ = '')
        # print ("page: {}".format(i))
        for game in gameList:
            print (game.find ('h3').text)

            releaseDate = game.find ('div', class_='clamp-details').find ('span', class_='').text

            print (releaseDate)

        # print (gameList.find_all ('tr', class_ = ''))

def main ():
    scrape ("ps5")

if __name__ == "__main__":
    main ()