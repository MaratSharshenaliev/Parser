import csv
from typing import Dict


def savedatabase(data: str):
    pass


def save():
    with open("data.csv") as f:
        keys = ["link_of_photo", "date_posted", "price"]
        reader_baike = csv.DictReader(f, fieldnames=keys)
        data = list(reader_baike)

        for pack in data:
            savedatabase(pack)


if __name__ == "__main__":
    save()
