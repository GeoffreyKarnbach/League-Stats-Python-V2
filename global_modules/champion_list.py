import sqlite3

def all_champions_name(frequence = False):
    db = sqlite3.connect("DATA/lol_stats.db")
    cursor = db.cursor()

    cursor.execute("SELECT champion FROM global") 
    result = cursor.fetchall()

    if not frequence:
        return list(set([item[0] for item in result]))

    amount = {}
    for champion in [item[0] for item in result]:
        if champion in amount:
            amount[champion]+=1
        else:
            amount[champion]=1

    return amount
