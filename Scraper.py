import requests
from bs4 import BeautifulSoup

# download music by link
def download(url, name):

    data = requests.get(url+"_128.mp3").content 
    # save .mp3 file 
    fileDirectory = f"D:/python/Scraper/Tracks/{name}.mp3"
    #or 
    # fileDirectory = f"{name}.mp3"
    with open(fileDirectory,"wb") as audio_file:
        audio_file.write(data)


def scrape(url):

    # get html data from web page

    htmldata = requests.get(url).text
    soup = BeautifulSoup(htmldata, "lxml")
    elements = soup.find_all("div", class_ ="track-itemss")

    # get music mame and url for download
    for element in elements:

        # sound name
        el = str (element.get("data-title"))    
        print(el)

        # artist name
        art = element.get("data-artist")
        print(art)

        # sound link
        audio = element.get("data-track")

        # call function
        download(audio, el)
        print(audio, "\n")


if __name__ == "__main__":
    url= "https://playi.net/artists/miyagi-andy-panda"
    scrape(url)