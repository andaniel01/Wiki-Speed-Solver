from bs4 import BeautifulSoup
import requests


def get_url(url):
    reqs = requests.get(url)
    soup = BeautifulSoup(reqs.text, 'html.parser')
    # storing all the urls
    urls = []
    urls_string = []
    urls_clean = []
    # finds all the divs with a certain id
    data = soup.find_all('div', attrs={'id': 'bodyContent'})

    # 'a' refers to hyperlinks
    for link in data:
        urls = link.find_all('a')

    # changing to click-able links
    # also adds the string version to the urls_string
    for url in urls:
        url = "https://en.wikipedia.org" + str(url.get('href'))
        urls_string.append(url)

    # identifies the faulty urls
    for n in range(len(urls_string)):
        if ("/wiki/" not in urls_string[n]) or ("wiktionary.org" in urls_string[n]) or \
                (".jpg" in urls_string[n]) or (".png" in urls_string[n]) or ("BookSources" in urls_string[n]) or \
                (".svg" in urls_string[n]) or ("ISBN" in urls_string[n]) or ("(" in urls_string[n]) or \
                ("Category" in urls_string[n]) or ("wikidata.org" in urls_string[n]) or ("Verifiability" in urls_string[n]) or \
                ("Portal" in urls_string[n]) or ("Citation" in urls_string[n]) or ("wikisource" in urls_string[n]) or \
                ("File" in urls_string[n]):
            urls_string[n] = "temp"

    # gets rid of all faulty urls
    for n in range(len(urls_string)-1, 0, -1):
        if urls_string[n] == "temp":
            urls_string.remove("temp")

    # testing purposes
    for n in range(len(urls_string)):
        print(str(n) + " " + urls_string[n])


def main():
    get_url("https://en.wikipedia.org/wiki/Korea")


if __name__ == "__main__":
    main()
