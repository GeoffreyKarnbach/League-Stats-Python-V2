import sqlite3

def get_all_gamemodes():
    db = sqlite3.connect("DATA/lol_stats.db")
    cursor = db.cursor()

    cursor.execute('SELECT gamemode FROM global')
    gamemodes = set([item[0] for item in cursor.fetchall()])
    return gamemodes

def get_all_items():
    db = sqlite3.connect("DATA/lol_stats.db")
    cursor = db.cursor()

    cursor.execute('SELECT item_name FROM items')
    gamemodes = set([item[0] for item in cursor.fetchall()])
    return gamemodes

def get_all_spells():
    db = sqlite3.connect("DATA/lol_stats.db")
    cursor = db.cursor()

    cursor.execute('SELECT spell_name FROM spells')
    gamemodes = set([item[0] for item in cursor.fetchall()])
    return gamemodes

if __name__ == "__main__":
    print(get_all_spells())