from os import error
from bs4 import BeautifulSoup
import json
from FETCHER.export_to_db import*

def fecth_data_from_html(filename):
    with open('DATA/items.json') as file, open(filename,"rb") as f:
        json_data = json.load(file)
        html_doc = f.readlines()

    soup = BeautifulSoup(html_doc[0], 'html.parser')
    db = DB_Handler()
    counter = 0

    for element in soup.find_all('li'):
        try:
            ############# Match information #############
            gamemode = element.find("div", {"class": "mode map-mode"}).text
            level = element.find("span", {"class": "champion-nameplate-level"}).text
            champion = element.find("div", {"class": "champion-nameplate-name"}).text
            creep_score = element.find("div", {"class": "income-minions"}).text
            gold = element.find("div", {"class": "income-gold"}).text
            kda = element.find("div", {"class": "kda-plate"}).text
            duration = element.find("span", {"class": "date-duration-duration"}).text
            date = element.find("span", {"class": "date-duration-date"}).text
            game_result = element.find_all("div", {"class": "game-summary-defeat result-marker"})
            if len(game_result) == 1: result = 0
            else: result = 1

            ############# Summoner spells #############
            spells = element.find_all("div", {"class": "spell-icon binding"})
            spell_1 = spells[0].find_all("img")[0]["src"].split("/")[-1].split(".")[0]
            spell_2 = spells[1].find_all("img")[0]["src"].split("/")[-1].split(".")[0]

            ############ Item List ###################

            mydivs = element.find("div", {"class": "inventory gs-container gs-no-gutter"}).find_all("div", {"data-rg-id": True})
            item_list = []

            for item in mydivs:
                item_list.append(json_data["data"][str(item["data-rg-id"])]["name"])
            ############ Output ###################
            db.export_to([champion, level, gamemode, kda, creep_score, gold, duration, date, result, spell_1, spell_2, item_list])
        except:
            pass

    db.close_connection()
    print("Fetching and export sucessful.")

