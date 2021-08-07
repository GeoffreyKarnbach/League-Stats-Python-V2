import sqlite3

def get_match_from(id, nb = 11):
    db = sqlite3.connect("DATA/lol_stats.db")
    cursor = db.cursor()

    cursor.execute(f'SELECT * FROM global')
    matches = cursor.fetchall()
    return matches[id:id+nb]

def total_matches_nb():
    db = sqlite3.connect("DATA/lol_stats.db")
    cursor = db.cursor()
    cursor.execute(f'SELECT * FROM global')
    return len(cursor.fetchall())

def total_matches_nb_for(champion):
    db = sqlite3.connect("DATA/lol_stats.db")
    cursor = db.cursor()
    cursor.execute(f'SELECT * FROM global WHERE champion = "{champion}"')
    return len(cursor.fetchall())

def get_match_from_for(id, champion, nb = 11):
    db = sqlite3.connect("DATA/lol_stats.db")
    cursor = db.cursor()

    cursor.execute(f'SELECT * FROM global WHERE champion = "{champion}"')
    matches = cursor.fetchall()
    return matches[id:id+nb]

def get_match_number(id):
    db = sqlite3.connect("DATA/lol_stats.db")
    cursor = db.cursor()

    cursor.execute(f'SELECT * FROM global WHERE match_id = "{id}"')
    return cursor.fetchall()[0]

def get_items_from(id):
    db = sqlite3.connect("DATA/lol_stats.db")
    cursor = db.cursor()

    cursor.execute(f'SELECT item_name FROM items WHERE match_id = "{id}"')
    return cursor.fetchall()

def get_spells_from(id):
    db = sqlite3.connect("DATA/lol_stats.db")
    cursor = db.cursor()

    cursor.execute(f'SELECT spell_name FROM spells WHERE match_id = "{id}"')
    return cursor.fetchall()

if __name__ == "__main__":
    get_match_from(697)