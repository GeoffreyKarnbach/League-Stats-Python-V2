import sqlite3
import collections

def item_list(champion):
    db = sqlite3.connect("DATA/lol_stats.db")
    cursor = db.cursor()

    cursor.execute(f'SELECT match_id FROM global WHERE champion = \"{champion}\"')

    games = [item[0] for item in cursor.fetchall()]
    
    item_count = {}

    for game in games:
        cursor.execute(f'SELECT item_name FROM items WHERE  match_id = \"{game}\"')
        items = [item[0] for item in cursor.fetchall()]
        for item in items:
            if item in item_count:
                item_count[item]+=1
            else:
                item_count[item] = 1

    item_count = dict(reversed(sorted(item_count.items(), key = lambda x: x[1])))
    return item_count

def gamemode_repartition(champion):
    db = sqlite3.connect("DATA/lol_stats.db")
    cursor = db.cursor()

    cursor.execute(f'SELECT gamemode FROM global WHERE champion = \"{champion}\"')

    game_count = {}
    for gamemode in [item[0] for item in cursor.fetchall()]:
        if gamemode in game_count:
            game_count[gamemode]+=1
        else:
            game_count[gamemode] = 1
    
    game_count = dict(reversed(sorted(game_count.items(), key = lambda x: x[1])))
    return game_count

def total_games(champion):
    db = sqlite3.connect("DATA/lol_stats.db")
    cursor = db.cursor()

    cursor.execute(f'SELECT * FROM global WHERE champion = \"{champion}\"')
    return len(cursor.fetchall())

def winrate(champion):
    db = sqlite3.connect("DATA/lol_stats.db")
    cursor = db.cursor()

    cursor.execute(f'SELECT result FROM global WHERE champion = \"{champion}\"')
    outcome = [elem[0] for elem in cursor.fetchall()]

    return (outcome.count(1),outcome.count(0))

def summoner_spells(champion):
    db = sqlite3.connect("DATA/lol_stats.db")
    cursor = db.cursor()

    cursor.execute(f'SELECT match_id FROM global WHERE champion = \"{champion}\"')

    games = [item[0] for item in cursor.fetchall()]
    
    spell_count = {}

    for game in games:
        cursor.execute(f'SELECT spell_name FROM spells WHERE  match_id = \"{game}\"')
        items = [item[0] for item in cursor.fetchall()]
        for item in items:
            if item in spell_count:
                spell_count[item]+=1
            else:
                spell_count[item] = 1

    spell_count = dict(reversed(sorted(spell_count.items(), key = lambda x: x[1])))
    return spell_count

def average_gold(champion):
    db = sqlite3.connect("DATA/lol_stats.db")
    cursor = db.cursor()

    cursor.execute(f'SELECT gold FROM global WHERE champion = \"{champion}\"')
    gold_list = [elem[0] for elem in cursor.fetchall()]
    return round(sum(gold_list)/len(gold_list))

def average_cs(champion):
    db = sqlite3.connect("DATA/lol_stats.db")
    cursor = db.cursor()

    cursor.execute(f'SELECT creep FROM global WHERE champion = \"{champion}\"')
    cs_list = [elem[0] for elem in cursor.fetchall()]
    return round(sum(cs_list)/len(cs_list),1)

def average_kda(champion):
    db = sqlite3.connect("DATA/lol_stats.db")
    cursor = db.cursor()

    result = ""

    #Kills
    cursor.execute(f'SELECT kills FROM global WHERE champion = \"{champion}\"')
    kill_list = [elem[0] for elem in cursor.fetchall()]
    result = result + str(round(sum(kill_list)/len(kill_list),1)) + " / "

    #Deaths
    cursor.execute(f'SELECT deaths FROM global WHERE champion = \"{champion}\"')
    death_list = [elem[0] for elem in cursor.fetchall()]
    result = result + str(round(sum(death_list)/len(death_list),1)) + " / "

    #Assists
    cursor.execute(f'SELECT assists FROM global WHERE champion = \"{champion}\"')
    assist_list = [elem[0] for elem in cursor.fetchall()]
    result = result + str(round(sum(assist_list)/len(assist_list),1))

    return result

def average_duration(champion):
    db = sqlite3.connect("DATA/lol_stats.db")
    cursor = db.cursor()

    cursor.execute(f'SELECT duration FROM global WHERE champion = \"{champion}\"')
    duration_list = [elem[0] for elem in cursor.fetchall()]
    total = 0
    for loop in duration_list:
        provisory = loop.split(":")
        total = total + int(provisory[0])*60 + int(provisory[1])
    
    total_time = total/len(duration_list)
    minutes = round(total_time//60)
    seconds = round(total_time%60)

    return f"{minutes}:{seconds}"

    


if __name__ == "__main__":
    average_duration("Master Yi")