import requests
from bs4 import BeautifulSoup

def main():
    url = "https://www.amazon.in/s/ref=mega_elec_s23_2_3_1_1?rh=i%3Acomputers%2Cn%3A3011505031&ie=UTF8&bbn=976392031"

    headers = {
    'authority': 'www.amazon.com',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'dnt': '1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'none',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-dest': 'document',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    }

    response = requests.get(f"{url}", headers=headers)

    with open("webpg.html","w", encoding="utf-8") as file: # saving html file to disk
        file.write(response.text)

    bs = BeautifulSoup(response.text, "html.parser")
    print(bs) # displaying html file use bs.prettify() for making the document more readable


main()