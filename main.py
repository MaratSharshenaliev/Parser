from bs4 import BeautifulSoup as BS
import requests
import dateparser
from typing import List, Dict
import csv


headers = {
    "Accept": "*/*",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"

}


def saveTocsv(data: Dict):
    with open("data.csv", "a") as file:
        writer = csv.writer(file)
        writer.writerow((data['link_of_photo'], data['date_posted'], data['price']))


def getData():
    for i in range(1, 94):
        BASE_URL = f"https://www.kijiji.ca/b-apartments-condos/city-of-toronto/page-{i}/c37l1700273"
        res = requests.get(BASE_URL, headers)
        soup = BS(res.content, 'html.parser')

        for photo, date_posted, price in zip(soup.select(".image > picture > source"),
                                             soup.select(".location > .date-posted"),
                                             soup.select(".info-container > .price")):
            # filters
            photo = photo.get("data-srcset").replace("200-webp", "640-webp")
            date_posted = date_posted.text.strip()
            price = price.text.strip()

            # normalize dates
            if date_posted not in "/":
                dt = dateparser.parse(date_posted.replace("<", ""))
                date_posted = dt.strftime("%d/%m/%Y")
                print(date_posted)

            data = {
                "link_of_photo": photo,
                "date_posted": date_posted,
                "price": price
            }
            saveTocsv(data)


if __name__ == '__main__':
    getData()
