import random
from termcolor import colored
from bs4 import BeautifulSoup as BS
import requests
import dateparser
from typing import List, Dict
import csv
from model import Data
import datetime
import os

headers = {
    "Accept": "*/*",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
}
proxies = [
    {"http": "http://51.38.191.151:80"},
    {"http": "http://165.154.235.178:80"}
]


def saveTocsv(data: Dict) -> int:
    with open("data.csv", "a") as file:
        writer = csv.writer(file)
        writer.writerow((data['link_of_photo'], data['date_posted'], data['price']))
    return 0


def getData() -> int:
    print("Parser has been started...")
    global somethingI
    count = 0
    # 94 pages
    for i in range(1, 94):
        BASE_URL = f"https://www.kijiji.ca/b-apartments-condos/city-of-toronto/page-{i}/c37l1700273"
        res = requests.get(BASE_URL, headers=headers, proxies=random.choice(proxies))
        soup = BS(res.content, 'html.parser')
        for photo, date_posted, price in zip(soup.select("div .image"),
                                             soup.select(".location > .date-posted"),
                                             soup.select(".info-container > .price")):
            # filters
            count += 1
            photo = photo.find("source")
            photo = photo.get("data-srcset").replace("200-webp",
                                                     "640-webp") if photo is not None else "https://afs.googleusercontent.com/kijiji-ca/csa-image1-large.png"
            date_posted = date_posted.text.strip()
            price = price.text.strip()
            # normalize dates
            if date_posted not in "/":
                dt = dateparser.parse(date_posted.replace("<", ""))
                date_posted = dt.strftime("%d/%m/%Y")

            if len(price) > 20:
                price = price[:9]

            data = {
                "link_of_photo": photo,
                "date_posted": date_posted,
                "price": price
            }
            somethingI = saveTocsv(data)
        print(f"[Parsing] Parsed - {i} pages.......{colored('OK', 'green')}")
    print(f"Gotten - {count} posts")
    return 0 if somethingI == 0 else 1


def save_database(data: str):
    link_of_photo = data["link_of_photo"]
    readyDate = [int(i) for i in data["date_posted"].split("/")][::-1]
    date_posted = datetime.date(readyDate[0], readyDate[1], readyDate[2])
    price = float(data["price"].replace(",", "")[1:]) if data["price"] != "Please Contact" else 0

    if len(str(price)) > 7:
        price = str(price)[:-3]

    Data(
        link_of_photo=link_of_photo,
        date_posted=date_posted,
        price=price
    ).save()


def save():
    with open("data.csv") as f:
        keys = ["link_of_photo", "date_posted", "price"]
        reader_baike = csv.DictReader(f, fieldnames=keys)
        data = list(reader_baike)

        for pack in data:
            save_database(pack)

    print(colored(f"Saved...{len(data)} posts", "green"))
    os.system("rm -rf data.csv")


# Here not much game to start 😂😂
def isRun(prompt):
    while True:
        try:
            return {"y": True, "n": False, }[input(prompt).lower()]
        except KeyError:
            print("Invalid input, please enter Y or N!")


if __name__ == '__main__':

    somethingO = getData() if isRun("Run will be parsing? Yes - Y/N - No: ") else 1
    if somethingO == 0:
        if isRun("Datas has downloaded.Save anywere? Yes - Y/N - No: "):
            save()
