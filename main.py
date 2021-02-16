from bs4 import BeautifulSoup
import requests


def get_url(url):
    # dont know
    reqs = requests.get(url)
    soup = BeautifulSoup(reqs.text, 'html.parser')
    # storing all the urls
    urls = []
    # finds all the divs with a certain id
    data = soup.find_all('div', attrs={'id': 'bodyContent'})

    # 'a' refers to hyperlinks
    for link in data:
        urls = link.find_all('a')


    # making it in to click-able url
    for url in urls:
        url = "https://en.wikipedia.org/" + str(url.get('href'))
        print(url)


def main():
    get_url("https://en.wikipedia.org/wiki/Korea")


if __name__ == "__main__":
    main()
