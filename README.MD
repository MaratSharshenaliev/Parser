# Parsing with Python
#####  _Created by Marat Sharshenaliev_


[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://github.com/MaratSharshenaliev/Parser.git)

## Requiments:

- beautifulsoup4 
- dateparser
- peewee
- psycopg2
- psycopg2-binary
- requests

## Installation




##### for Mac or Linux:
#
```sh
git clone "https://github.com/MaratSharshenaliev/Parser.git"
cd Parser && python3 -m venv venv 
source venv/bin/activate 
pip install -r requirments.txt
```

##### for Windows:
#
```sh
git clone "https://github.com/MaratSharshenaliev/Parser.git"
cd Parser && virtualenv venv
.\venv\Scripts\activate 
pip install -r requirments.txt
```
Check it, i guass i'd written not correct ^^^



You can start parsing without saving
BUT you want to keep the database data you need to change the host, port, database name and password inside models.py ...
#
```sh
db = PostgresqlDatabase(
    database="Name of data Base",
    password="Your pass",
    user="postgres",
    host="localhost",
    port=5432
)
```

##### Then you most write your ``User-Agent``  main.py 11 line :

#
```
headers = {
    "Accept": "*/*",
    "User-Agent": "Here ..."
}
```
## Then you car easy start parsing...

```sh
python3 main.py
```

Of course, I'm not a perfect coder, but I tried my best ❤️❤️❤️

