import requests
from datetime import datetime
from getpass import getpass

s = requests.session()

data = {
    "username":"lazar41121",
    "password":getpass("Sifra molim te: "),
    "ustanova":"ITS"
}

portal = s.post("https://v2.link-onlineservice.com/its/services/login", data=data)

data = {
    "godina": datetime.now().year,
    "mesec": datetime.now().month,
    }

headers = {
    #"origin":"https://v2.link-onlineservice.com",
    #"referer":"https://v2.link-onlineservice.com/services/KalendarPredavanja",
    "x-requested-with":"XMLHttpRequest"
    }

raspored = s.post("https://v2.link-onlineservice.com/services/KalendarPredavanja/vratiPredavanjaZaMesec",data=data,headers=headers)

with open("raspored.txt","w",encoding="utf-8") as file:
    keys_to_get = ['title','vreme','vremeEnd','param','lokacija']
    for _ in raspored.json():
        for key in keys_to_get:
            file.write(f'{key}: {_[key]}\n')
        file.write('-----------------------\n')