import sqlite3

class DB_Handler:
    def __init__(self):
        self.db = sqlite3.connect("DATA/lol_stats.db")
        self.cursor = self.db.cursor()
        self.clear_db()

    def clear_db(self):
        self.cursor.execute("DELETE FROM global;")
        self.cursor.execute("DELETE FROM items;")
        self.cursor.execute("DELETE FROM spells;")
        self.db.commit()

    def export_to(self,data):
        export_data = [data[0].strip()]
        export_data.append(int(data[1]))
        export_data.append(data[2])
        kda = data[3].split("/")
        export_data.append(int(kda[0]))
        export_data.append(int(kda[1]))
        export_data.append(int(kda[2]))
        export_data.append(int(data[4]))
        if "k" in data[5]:
            gold = int(float(data[5].strip()[:-1])*1000)
        else:
            gold = int(data[5].strip())
        
        export_data.append(gold)
        export_data.append(data[6])
        export_data.append(data[7])
        export_data.append(int(data[8]))
        
        self.cursor.execute(f"INSERT INTO global (champion, level, gamemode, kills, deaths, assists, creep, gold, duration, date, result) VALUES (?,?,?,?,?,?,?,?,?,?,?);", export_data)
        self.db.commit()

        self.cursor.execute("SELECT match_id FROM global ORDER BY match_id DESC LIMIT 1;")
        last_id = self.cursor.fetchall()
        last_id = last_id[0][0]

        self.cursor.execute(f"INSERT INTO spells (match_id, spell_name) VALUES (?,?);", (last_id, data[9]))
        self.cursor.execute(f"INSERT INTO spells (match_id, spell_name) VALUES (?,?);", (last_id, data[10]))      
        self.db.commit()

        for item in data[11]:
            self.cursor.execute(f"INSERT INTO items (match_id, item_name) VALUES (?,?);", (last_id, item))
        
        self.db.commit()

    
    def close_connection(self):
        self.db.close()