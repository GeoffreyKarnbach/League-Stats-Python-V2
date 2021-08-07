import sqlite3

def sort_by_spell(spell):
    db = sqlite3.connect("DATA/lol_stats.db")
    cursor = db.cursor()

    cursor.execute(f'SELECT match_id FROM spells WHERE spell_name = "{spell}"')
    match_list = [item[0] for item in cursor.fetchall()]
    matches = []
    for match in match_list:
        cursor.execute(f'SELECT * FROM global WHERE match_id = "{match}"')
        matches.append(cursor.fetchall()[0])
    
    return matches

def sort_by_item(item):
    db = sqlite3.connect("DATA/lol_stats.db")
    cursor = db.cursor()

    cursor.execute(f'SELECT match_id FROM items WHERE item_name = "{item}"')
    match_list = [item[0] for item in cursor.fetchall()]
    matches = []
    for match in match_list:
        cursor.execute(f'SELECT * FROM global WHERE match_id = "{match}"')
        matches.append(cursor.fetchall()[0])
    
    return matches

def sort_by_outcome(outcome):
    db = sqlite3.connect("DATA/lol_stats.db")
    cursor = db.cursor()

    cursor.execute(f'SELECT * FROM global WHERE result = "{outcome}"')
    return cursor.fetchall()

def sort_by_gamemode(gamemode):
    db = sqlite3.connect("DATA/lol_stats.db")
    cursor = db.cursor()

    cursor.execute(f'SELECT * FROM global WHERE gamemode = "{gamemode}"')
    return cursor.fetchall()

if __name__ == "__main__":
    print(sort_by_spell("SummonerSmite"))