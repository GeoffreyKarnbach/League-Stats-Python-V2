from tkinter import*
from tkinter.messagebox import*

from global_modules.champion_list import*
from global_modules.match_getter import*
from global_modules.individual_champion import*
from global_modules.sort_matches import*
from global_modules.element_lists import*

'''
CLass for Main Page (Index) showing match list

'''
class Index:
    def __init__(self, root, frame):
        self.root = root
        self.frame = frame
        
        self.start = 0
        self.var = StringVar()
        self.build()


    def confirm_champ_select(self):
        if self.var.get() != "":
            Champion(self.root, self.frame, self.var.get(), self, self)
        
    def center_window(self):
        self.root.geometry("+400+0")
        
    def clear(self):
        for widget in self.frame.winfo_children():
            widget.destroy()

    def go_to_match(self, id):
        Match(self.root, self.frame, id, self, self)
    
    def go_to_select(self):
        Selecting(self.root, self.frame, self, self)

    def go_to_facts(self):
        BestStats(self.root, self.frame, self, self)

    def change_match_interval(self, nb):
        if nb < 0:
            if self.start == total_matches_nb()-1:
                reste = self.start % 11
                self.start -= reste
            else:
                self.start = max(self.start+nb, 0)
            self.build()
        else:
            if self.start+11 < total_matches_nb()-1:
                self.start = min(self.start+nb, total_matches_nb()-1)
                self.build()

    def build(self):

        # Clear frame
        self.clear()
        self.root.title("Index")

        # Champion selection menu
        champion_list = sorted(all_champions_name(False))
        
        Label(self.frame, text = "Champion List: ", font=("Verdana","10")).grid(column = 0, row = 0, padx = 10, pady = 10)
        OptionMenu(self.frame, self.var, *champion_list).grid(column = 1, row = 0, padx = 10, pady = 10)
        Button(self.frame, text= "Confirm", command = self.confirm_champ_select, font=("Verdana","10")).grid(column=2, row=0, padx = 10, pady = 10)
        Button(self.frame, text= "Sort Matches", command = self.go_to_select, font=("Verdana","10")).grid(column=3, row=0, padx = 10, pady = 10)

        # Match history
        self.load_from_match()
    
        # Navigation Buttons
        Button(self.frame, text = "<<", command = lambda x = -11 : self.change_match_interval(x), font=("Verdana","10")).grid(column = 0, row = 2, padx = 10, pady = 10)
        Button(self.frame, text = "Global Stats", command = self.go_to_facts, font=("Verdana","10")).grid(column = 1, row = 2, padx = 10, pady = 10)
        Button(self.frame, text = ">>", command = lambda x = 11 : self.change_match_interval(x), font=("Verdana","10")).grid(column = 2, row = 2, padx = 10, pady = 10)
    
    def load_from_match(self):
        self.match_container = Frame(self.frame)
        self.match_container.grid(column=0, row = 1, columnspan=5)
        matches = get_match_from(self.start, nb = 11)
        for id,match in enumerate(matches):
            colors = {"Howling Abyss ":"light goldenrod","Summoner's Rift Ranked (Draft Mode)":"brown","Summoner's Rift Normal (Draft Mode)": "orange", "Summoner's Rift ":"yellow"}
            if match[3] in colors:
                Button(self.match_container, text  = match[1]+"   |   "+str(match[4])+"/"+str(match[5])+"/"+str(match[6])+"   |   "+match[3]+"\n\n"+match[10], font=("Verdana","10"), bg = colors[match[3]], width = 70, height = 3, command = lambda x =  match[0]: self.go_to_match(x)).grid(column = 0, row = id, padx = 10, pady = 10)
            else:
                Button(self.match_container, text  = match[1]+"   |   "+str(match[4])+"/"+str(match[5])+"/"+str(match[6])+"   |   "+match[3]+"\n\n"+match[10], font=("Verdana","10"), bg = "grey", width = 70, height = 3, command = lambda x =  match[0]: self.go_to_match(x)).grid(column = 0, row = id, padx = 10, pady = 10)
            
            if match[11] == 1:
                Button(self.match_container, bg = "green", width = 7, height = 3).grid(column = 1, row = id, padx = 10, pady = 10)
            else:
                Button(self.match_container, bg = "red", width = 7, height = 3).grid(column = 1, row = id, padx = 10, pady = 10)
        self.center_window()


'''
Class to show Best Stats:
- Champion Winrate with 5+ games
- Most Built Item
- Best Champion average CS with 5+ games
- Most used Spells

'''
class BestStats:
    def __init__(self, root, frame, main_page, last_page):
        self.root = root
        self.frame = frame
        self.main_page = main_page
        self.last_page = last_page
        self.build()

    def center_window(self):
        self.root.geometry("+400+0")

    def go_to_last_page(self, event):
        self.last_page.build()

    def clear(self):
        for widget in self.frame.winfo_children():
            widget.destroy()      
    def go_to_main_page(self):
        self.main_page.build()

    def build(self):
        self.clear()
        self.root.title("Global stats and facts")
        self.root.bind("<Left>", self.go_to_last_page)

        Label(self.frame, text = "Global stats and facts", font=("Verdana","15","underline")).grid(column=0, row= 0, padx = 10, pady = 10)
        self.center_window()

'''
Class for Individual Champion window

'''
class Champion:
    def __init__(self, root, frame, champion, main_page, last_page):
        self.root = root
        self.frame = frame
        self.champion = champion
        self.main_page = main_page
        self.last_page = last_page
        self.build()

    def center_window(self):
        self.root.geometry("+400+0")

    def go_to_last_page(self, event):
        self.last_page.build()

    def clear(self):
        for widget in self.frame.winfo_children():
            widget.destroy()

    def go_to_main_page(self):
        self.main_page.build()

    def go_to_champion_matches(self):
        Matches(self.root, self.frame, self.champion, self.main_page, self)

    def build(self):

        self.clear()
        self.root.title("Stats for "+self.champion)
        self.root.bind("<Left>", self.go_to_last_page)

        # Most Built items
        self.item_frame = Frame(self.frame, highlightbackground="black", highlightthickness=1, height= 600, width = 600)
        self.item_frame.grid(column = 0, row = 0, padx = 10, pady = 10, sticky = NW)
        self.item_frame.grid_propagate(0)
        items = list(item_list(self.champion).items())
        Label(self.item_frame, text = "Most Common Items with "+self.champion, font=("Verdana","15","underline")).grid(column = 0, row = 0, padx = 10, pady = 10, sticky = NW)
        current_row = 0
        for item in range(min(10, len(items))):
            current_row = item + 1
            Label(self.item_frame, text = items[item][0]+"  -  "+str(items[item][1]), font=("Verdana","9")).grid(column = 0, row = current_row, padx = 10, pady = 10, sticky = NW)
            

        # Games Played per gamemode
        self.gamemode_frame = Frame(self.frame, highlightbackground="black", highlightthickness=1, height= 600, width = 600)
        self.gamemode_frame.grid(column = 1, row = 0, padx = 10, pady = 10, sticky = NW)
        self.gamemode_frame.grid_propagate(0)

        gamemodes = list(gamemode_repartition(self.champion).items())
        
        Label(self.gamemode_frame, text = "Games played with  "+self.champion, font=("Verdana","15","underline")).grid(column = 0, row = 0, padx = 10, pady = 10, sticky = NW)
        
        self.winrate_frame = Frame(self.gamemode_frame, highlightbackground="black", highlightthickness=1)
        self.winrate_frame.grid(column = 0, row = 1, padx = 10, pady = 10, sticky = NW)

        Label(self.winrate_frame, text = "Total game count with "+self.champion+" : "+str(total_games(self.champion)), font=("Verdana","11","underline")).grid(column = 0, row = 1, padx = 10, pady = 10, sticky = NW)
        
        win_lose = winrate(self.champion)
        Label(self.winrate_frame, text = "Wins: "+str(win_lose[0]), font=("Verdana","9")).grid(column = 0, row = 2, padx = 10, pady = 10, sticky = NW)
        Label(self.winrate_frame, text = "Loses: "+str(win_lose[1]), font=("Verdana","9")).grid(column = 0, row = 3, padx = 10, pady = 10, sticky = NW)
        Label(self.winrate_frame, text = "Wirate: "+str(round(win_lose[0]/(win_lose[1]+win_lose[0])*100,2))+"%", font=("Verdana","9")).grid(column = 0, row = 4, padx = 10, pady = 10, sticky = NW)
        
        self.mode_frame = Frame(self.gamemode_frame, highlightbackground="black", highlightthickness=1)
        self.mode_frame.grid(column = 0, row = 2, padx = 10, pady = 10, sticky = NW)

        current_row = 4
        for gamemode in range(len(gamemodes)):
            current_row += 1
            Label(self.mode_frame, text = gamemodes[gamemode][0]+"  -  "+str(gamemodes[gamemode][1]), font=("Verdana","9")).grid(column = 0, row = current_row, padx = 10, pady = 10, sticky = NW)

        #Summoner Spells
        self.spell_frame = Frame(self.frame, highlightbackground="black", highlightthickness=1, height = 250, width = 600)
        self.spell_frame.grid(column = 0, row = 1, padx = 10, pady = 10, sticky = NW)
        self.spell_frame.grid_propagate(0)

        spells = list(summoner_spells(self.champion).items())
        Label(self.spell_frame, text = "List of summoner spells with "+self.champion, font=("Verdana","15","underline")).grid(column = 0, row = 0, padx = 10, pady = 10, sticky = NW, columnspan = 3)
        current_row = 1
        for spell in range(len(spells)):
            Label(self.spell_frame, text = spells[spell][0]+" : "+str(spells[spell][1]), font=("Verdana","9")).grid(column = spell%3, row = current_row, padx = 10, pady = 10, sticky = NW)
            if spell % 3 == 2:
                current_row += 1
        
        # Other stats
        self.stats_frame = Frame(self.frame, highlightbackground="black", highlightthickness=1, height = 250, width = 600)
        self.stats_frame.grid(column = 1, row = 1, padx = 10, pady = 10, sticky = NW)
        self.stats_frame.grid_propagate(0)

        Label(self.stats_frame, text = "Global Stats for  "+self.champion, font=("Verdana","15","underline")).grid(column = 0, row = 0, padx = 10, pady = 10, sticky = NW)
        Label(self.stats_frame, text = "Average KDA: "+str(average_kda(self.champion)), font=("Verdana","9")).grid(column = 0, row = 1, padx = 10, pady = 10, sticky = NW)
        Label(self.stats_frame, text = "Average Gold: "+str(average_gold(self.champion)), font=("Verdana","9")).grid(column = 0, row = 2, padx = 10, pady = 10, sticky = NW)
        Label(self.stats_frame, text = "Average CS: "+str(average_cs(self.champion)), font=("Verdana","9")).grid(column = 0, row = 3, padx = 10, pady = 10, sticky = NW)
        Label(self.stats_frame, text = "Average Duration: "+str(average_duration(self.champion)), font=("Verdana","9")).grid(column = 0, row = 4, padx = 10, pady = 10, sticky = NW)

        # To match list
        Button(self.frame, text = "Match List with "+self.champion, width = 65, height = 2, command = self.go_to_champion_matches, font=("Verdana","11"), bg = "grey").grid(column = 0, row = 2)
        Button(self.frame, text = "Go Back to Main Page", width = 65, height = 2, command = self.go_to_main_page, font=("Verdana","11"), bg = "grey").grid(column = 1, row = 2)
        self.center_window()


'''
Class to display details about a specific match by its id

'''
class Match:
    def __init__(self, root, frame, id, main_page, last_page):
        self.root = root
        self.frame = frame
        self.id = id
        self.main_page = main_page
        self.last_page = last_page

        self.build()
    
    def go_to_main_page(self):
        self.main_page.build()
    
    def go_to_last_page(self, event):
        self.last_page.build()

    def center_window(self):
        self.root.geometry("+400+0")
        
    def clear(self):
        for widget in self.frame.winfo_children():
            widget.destroy()

    def go_to_champion(self, champion):
        Champion(self.root, self.frame, champion, self.main_page, self)
    
    def go_to_gamemode(self, gamemode):
        Selecting(self.root, self.frame, self.main_page, self.last_page, category=0, search_term=gamemode)
    
    def go_to_item(self, item):
        Selecting(self.root, self.frame, self.main_page, self.last_page, category=1, search_term=item)
    
    def go_to_spell(self, spell):
        Selecting(self.root, self.frame, self.main_page, self.last_page, category=2, search_term=spell)

    def build(self):
        self.clear()
        self.root.bind("<Left>", self.go_to_last_page)
        self.root.title("Match number : "+str(self.id))

        match_data = get_match_number(self.id)


        self.global_frame = Frame(self.frame, highlightbackground="black", highlightthickness=1, height= 500, width = 500)
        self.global_frame.grid(column = 0, row = 1)
        self.global_frame.grid_propagate(0)

        Label(self.frame, text = "Details on match number "+str(match_data[0]), font=("Verdana","15","underline")).grid(column = 1, row = 0, padx = 10, pady = 10)
        Button(self.global_frame, text = "Champion played: "+match_data[1], font=("Verdana","11"), command = lambda x = match_data[1]: self.go_to_champion(x)).grid(column = 0, row = 1, padx = 10, pady = 10, sticky = NW)
        Label(self.global_frame, text = "Final champion level: "+str(match_data[2]), font=("Verdana","11")).grid(column = 0, row = 2, padx = 10, pady = 10, sticky = NW)
        Button(self.global_frame, text = "Gamemode: "+str(match_data[3]), font=("Verdana","11"), command = lambda x = match_data[3]: self.go_to_gamemode(x)).grid(column = 0, row = 3, padx = 10, pady = 10, sticky = NW)
        kda = "KDA: "+str(match_data[4])+" / "+str(match_data[5])+" / "+str(match_data[6])
        Label(self.global_frame, text = kda, font=("Verdana","11")).grid(column = 0, row = 4, padx = 10, pady = 10, sticky = NW)
        Label(self.global_frame, text = "CS: "+str(match_data[7]), font=("Verdana","11")).grid(column = 0, row = 5, padx = 10, pady = 10, sticky = NW)
        Label(self.global_frame, text = "Gold: "+str(match_data[8]), font=("Verdana","11")).grid(column = 0, row = 6, padx = 10, pady = 10, sticky = NW)
        Label(self.global_frame, text = "Duration: "+str(match_data[9]), font=("Verdana","11")).grid(column = 0, row = 7, padx = 10, pady = 10, sticky = NW)
        Label(self.global_frame, text = "Date: "+str(match_data[10]), font=("Verdana","11")).grid(column = 0, row = 8, padx = 10, pady = 10, sticky = NW)
        outcome = {1: "Victory",0:"Defeat"}
        Label(self.global_frame, text = "Outcome: "+outcome[match_data[11]], font=("Verdana","11")).grid(column = 0, row = 9, padx = 10, pady = 10, sticky = NW)


        # Items
        self.item_frame = Frame(self.frame, highlightbackground="black", highlightthickness=1, height= 500, width = 350)
        self.item_frame.grid(column = 1, row = 1, padx = 10, pady = 10)
        self.item_frame.grid_propagate(0)

        Label(self.item_frame, text = "Item List:", font=("Verdana","11","underline")).grid(column = 0, row = 0, padx = 10, pady = 10, sticky=NW)
        items = [elem[0] for elem in get_items_from(self.id)]
        for id, item in enumerate(items):
            Button(self.item_frame, text = item, font=("Verdana","10"), command = lambda x =item: self.go_to_item(x)).grid(column = 0, row = 1+id, padx = 10, pady = 10, sticky=NW)

        # Spells
        self.spell_frame = Frame(self.frame, highlightbackground="black", highlightthickness=1, height= 500, width = 350)
        self.spell_frame.grid(column = 2, row = 1, padx = 10, pady = 10)
        self.spell_frame.grid_propagate(0)
        Label(self.spell_frame, text = "Summoner Spells:", font=("Verdana","11","underline")).grid(column = 0, row = 0, padx = 10, pady = 10, sticky=NW)

        spells = [elem[0] for elem in get_spells_from(self.id)]
        for id, spell in enumerate(spells):
            Button(self.spell_frame, text = spell, font=("Verdana","10"), command = lambda x = spell: self.go_to_spell(x)).grid(column = 0, row = 1+id, padx = 10, pady = 10, sticky=NW)

        Button(self.frame, text = "Go Back to Main Page", width = 38, height = 2, command = self.go_to_main_page, font=("Verdana","11"), bg = "grey").grid(column = 1, row = 2, padx = 10, pady = 10)
        self.center_window()


'''
Class to show a list of all matches for a specific champion
'''
class Matches:
    def __init__(self, root, frame, champion, main_page, last_page):
        self.root = root
        self.frame = frame
        self.champion = champion
        self.main_page = main_page
        self.last_page = last_page

        self.start = 0
        self.var = StringVar()

        self.build()
    
    def center_window(self):
        self.root.geometry("+400+0")
    
    
    def go_to_last_page(self, event):
        self.last_page.build()
        
    def clear(self):
        for widget in self.frame.winfo_children():
            widget.destroy()
        
    def go_to_main_page(self):
        self.main_page.build()
    
    def go_to_match(self, id):
        Match(self.root, self.frame, id, self.main_page, self)

    def change_match_interval(self, nb):
        if nb < 0:
            if self.start == total_matches_nb_for(self.champion)-1:
                reste = self.start % 11
                self.start -= reste
            else:
                self.start = max(self.start+nb, 0)
            self.build()
        else:
            if self.start+11 < total_matches_nb_for(self.champion)-1:
                self.start = min(self.start+nb, total_matches_nb_for(self.champion)-1)
                self.build()

    def build(self):

        self.clear()
        self.root.title("Match list with "+self.champion)
        self.root.bind("<Left>", self.go_to_last_page)

        Label(self.frame, text = self.champion, font=("Verdana","15","underline")).grid(column = 0, row = 0, padx = 10, pady = 10)

        self.load_from_match()
    
    def load_from_match(self):
        self.match_container = Frame(self.frame)
        self.match_container.grid(column=0, row = 1, columnspan=3)
        matches = get_match_from_for(self.start, nb = 11, champion=self.champion)
        id = 0
        for id,match in enumerate(matches):
            colors = {"Howling Abyss ":"light goldenrod","Summoner's Rift Ranked (Draft Mode)":"brown","Summoner's Rift Normal (Draft Mode)": "orange", "Summoner's Rift ":"yellow"}
            if match[3] in colors:
                Button(self.match_container, text  = match[1]+"   |   "+str(match[4])+"/"+str(match[5])+"/"+str(match[6])+"   |   "+match[3]+"\n\n"+match[10], font=("Verdana","10"), bg = colors[match[3]], width = 70, height = 3, command = lambda x =  match[0]: self.go_to_match(x)).grid(column = 0, row = id, padx = 10, pady = 10, columnspan=2)
            else:
                Button(self.match_container, text  = match[1]+"   |   "+str(match[4])+"/"+str(match[5])+"/"+str(match[6])+"   |   "+match[3]+"\n\n"+match[10], font=("Verdana","10"), bg = "grey", width = 70, height = 3, command = lambda x =  match[0]: self.go_to_match(x)).grid(column = 0, row = id, padx = 10, pady = 10, columnspan=2)
            
            if match[11] == 1:
                Button(self.match_container, bg = "green", width = 7, height = 3).grid(column = 2, row = id, padx = 10, pady = 10)
            else:
                Button(self.match_container, bg = "red", width = 7, height = 3).grid(column = 2, row = id, padx = 10, pady = 10)
            
        Button(self.match_container, text = "<<", command = lambda x = -11 : self.change_match_interval(x), font=("Verdana","10")).grid(column = 0, row = id+1)
        Button(self.match_container, text = "Go Back to Main Page", width = 55, height = 2, command = self.go_to_main_page, font=("Verdana","11"), bg = "grey").grid(column = 1, row = id+1)
        Button(self.match_container, text = ">>", command = lambda x = 11 : self.change_match_interval(x), font=("Verdana","10")).grid(column = 2, row = id+1)
        self.center_window()


'''
Class to select matches for a specific sorting setting

'''
class Selecting:
    def __init__(self, root, frame, main_page, last_page, category = None, search_term = None):
        self.root = root
        self.frame = frame
        self.main_page = main_page
        self.last_page = last_page

        if category is not None and search_term is not None:
            self.direct_search(category, search_term)
        else:
            self.outcome = IntVar()
            self.gamemode = StringVar()
            self.spell = StringVar()
            self.item = StringVar()
            self.build()

        

    def center_window(self):
        self.root.geometry("+400+0")
    
    def go_to_main_page(self):
        self.main_page.build()

    def direct_search(self, category, term):

        if category == 0:
            match_list = sort_by_gamemode(term)
            if len(match_list) != 0:
                Sorting(self.root, self.frame, self.main_page, self.last_page, match_list)
            else:
                showerror("Gamemode not found","Please check the exact name in list.")
        
        if category == 1:
            match_list = sort_by_item(term)
            if len(match_list) != 0:
                Sorting(self.root, self.frame, self.main_page, self.last_page, match_list)
            else:
                showerror("Item not found","Please check the exact name in list.")
        
        if category == 2:
            match_list = sort_by_spell(term)
            if len(match_list) != 0:
                Sorting(self.root, self.frame, self.main_page, self.last_page, match_list)
            else:
                showerror("Spell not found","Please check the exact name in list.")
        
    def clear(self):
        for widget in self.frame.winfo_children():
            widget.destroy()
        
    def go_to_last_page(self, event):
        self.last_page.build()

    def get_outcome(self):
        match_list = sort_by_outcome(self.outcome.get())
        Sorting(self.root, self.frame, self.main_page, self, match_list)
    
    def gamemode_list(self):
        self.gamemode_list_window = Toplevel(self.root)
        self.gamemode_list_window.title("Gamemode List")

        Label(self.gamemode_list_window, text = "Gamemode List", font=("Verdana","13","underline")).grid(column = 0, row = 0, padx = 10, pady = 10)

        all_gamemodes = get_all_gamemodes()
        temp_variables = []

        for id, gamemode in enumerate(all_gamemodes):
            temp_variables.append(StringVar())
            temp_variables[-1].set(gamemode)
            Entry(self.gamemode_list_window, textvariable=temp_variables[-1], width = 40).grid(column = 0, row = id+1, padx = 10, pady = 10)
        self.gamemode_list_window.mainloop()

    def spell_list(self):
        self.spell_list_window = Toplevel(self.root)
        self.spell_list_window.title("Spell List")
        
        Label(self.spell_list_window, text = "Spell List", font=("Verdana","13","underline")).grid(column = 0, row = 0, padx = 10, pady = 10)

        all_spells = get_all_spells()
        temp_variables = []

        for id, spell in enumerate(all_spells):
            temp_variables.append(StringVar())
            temp_variables[-1].set(spell)
            Entry(self.spell_list_window, textvariable=temp_variables[-1], width = 40).grid(column = 0, row = id+1, padx = 10, pady = 10)

        self.spell_list_window.mainloop()
    
    def item_list(self):
        self.item_list_window = Toplevel(self.root)
        self.item_list_window.title("Item List")
        
        Label(self.item_list_window, text = "Item List", font=("Verdana","13","underline")).grid(column = 0, row = 0, padx = 10, pady = 10)

        all_items = sorted(get_all_items())
        temp_variables = []

        for id, item in enumerate(all_items):
            temp_variables.append(StringVar())
            temp_variables[-1].set(item)
            Entry(self.item_list_window, textvariable=temp_variables[-1], width = 30).grid(column = id % 8, row = id//8, padx = 10, pady = 10)

        self.item_list_window.mainloop()

    def get_gamemode(self):
        chosen = self.gamemode.get()
        match_list = sort_by_gamemode(chosen)
        if len(match_list) != 0:
            Sorting(self.root, self.frame, self.main_page, self, match_list)
        else:
            showerror("Gamemode not found","Please check the exact name in list.")
    
    def get_spell(self):
        chosen = self.spell.get()
        match_list = sort_by_spell(chosen)
        if len(match_list) != 0:
            Sorting(self.root, self.frame, self.main_page, self, match_list)
        else:
            showerror("Spell not found","Please check the exact name in list.")

    def get_item(self):
        chosen = self.item.get()
        match_list = sort_by_item(chosen)
        if len(match_list) != 0:
            Sorting(self.root, self.frame, self.main_page, self, match_list)
        else:
            showerror("Item not found","Please check the exact name in list.")
    
    def build(self):
        self.root.bind("<Left>", self.go_to_last_page)
        self.root.title("Select Criterias")
        self.clear()

        Label(self.frame, text = "Select Criterias", font=("Verdana","15","underline")).grid(column = 0, row = 0, padx = 10, pady = 10, columnspan=2)

        # Spells
        self.spell_frame = Frame(self.frame, highlightbackground="black", highlightthickness=1, height= 200, width = 500)
        self.spell_frame.grid(column = 0, row = 1, padx = 10, pady = 10)
        self.spell_frame.grid_propagate(0)
        Label(self.spell_frame, text = "Spell Name:", font=("Verdana","11","underline")).grid(column = 0, row = 0, padx = 170, pady = 25, columnspan=3)
        Label(self.spell_frame, text = "Spell: ").grid(column = 0, row = 1, padx = 10, pady = 10)
        Entry(self.spell_frame, textvariable=self.spell).grid(column = 1, row = 1, padx = 10, pady = 10)
        Button(self.spell_frame, text = "Spell List", command = self.spell_list).grid(column = 2, row = 1, padx = 10, pady = 10)
        Button(self.spell_frame, text = "Confirm", command = self.get_spell, font=("Verdana","11"), width = 20, height = 1).grid(column = 0, row = 2, padx = 10, pady = 10, columnspan=3)

        # Items
        self.item_frame = Frame(self.frame, highlightbackground="black", highlightthickness=1, height= 200, width = 500)
        self.item_frame.grid(column = 1, row = 1, padx = 10, pady = 10)
        self.item_frame.grid_propagate(0)
        Label(self.item_frame, text = "Item Name:", font=("Verdana","11","underline")).grid(column = 0, row = 0, padx = 170, pady = 25, columnspan=3)
        Label(self.item_frame, text = "Item: ").grid(column = 0, row = 1, padx = 10, pady = 10)
        Entry(self.item_frame, textvariable=self.item).grid(column = 1, row = 1, padx = 10, pady = 10)
        Button(self.item_frame, text = "Item List", command = self.item_list).grid(column = 2, row = 1, padx = 10, pady = 10)
        Button(self.item_frame, text = "Confirm", command = self.get_item, font=("Verdana","11"), width = 20, height = 1).grid(column = 0, row = 2, padx = 10, pady = 10, columnspan=3)

        # Outcome
        self.outcome_frame = Frame(self.frame, highlightbackground="black", highlightthickness=1, height= 200, width = 500)
        self.outcome_frame.grid(column = 0, row = 2, padx = 10, pady = 10)
        self.outcome_frame.grid_propagate(0)
        Label(self.outcome_frame, text = "Match Outcome:", font=("Verdana","11","underline")).grid(column = 0, row = 0, padx = 170, pady = 25, columnspan=2)
        Radiobutton(self.outcome_frame, variable=self.outcome, text = "Victory", value=1).grid(column = 0, row = 1, padx = 10, pady = 10)
        Radiobutton(self.outcome_frame, variable=self.outcome, text = "Defeat", value=0).grid(column = 1, row = 1, padx = 10, pady = 10)
        Button(self.outcome_frame, text = "Confirm", font=("Verdana","11"), width = 20, height = 1, command=self.get_outcome).grid(column=0, row = 2, padx = 10, pady = 10, columnspan=2)
        
        # Gamemode
        self.gamemode_frame = Frame(self.frame, highlightbackground="black", highlightthickness=1, height= 200, width = 500)
        self.gamemode_frame.grid(column = 1, row = 2, padx = 10, pady = 10)
        self.gamemode_frame.grid_propagate(0)
        Label(self.gamemode_frame, text = "Gamemode Name:", font=("Verdana","11","underline")).grid(column = 0, row = 0, padx = 170, pady = 25, columnspan=3)
        Label(self.gamemode_frame, text = "Gamemode: ").grid(column = 0, row = 1, padx = 10, pady = 10)
        Entry(self.gamemode_frame, textvariable=self.gamemode).grid(column = 1, row = 1, padx = 10, pady = 10)
        Button(self.gamemode_frame, text = "Gamemode List", command = self.gamemode_list).grid(column = 2, row = 1, padx = 10, pady = 10)
        Button(self.gamemode_frame, text = "Confirm", command = self.get_gamemode, font=("Verdana","11"), width = 20, height = 1).grid(column = 0, row = 2, padx = 10, pady = 10, columnspan=3)

        Button(self.frame, text = "Go Back to Main Page", width = 55, height = 2, command = self.go_to_main_page, font=("Verdana","11"), bg = "grey").grid(column = 0, row = 3, columnspan=2)

        self.center_window()


'''
Class to display all matches for a specific sorting setting

'''
class Sorting:
    def __init__(self, root, frame, main_page, last_page, match_list):
        self.root = root
        self.frame = frame
        self.main_page = main_page
        self.last_page = last_page

        self.matches = match_list
        self.start = 0
        self.var = StringVar()

        self.build()


    def center_window(self):
        self.root.geometry("+400+0")
        
    def clear(self):
        for widget in self.frame.winfo_children():
            widget.destroy()

    def go_to_last_page(self, event):
        self.last_page.build()

    def go_to_main_page(self):
        self.main_page.build()
    
    def go_to_match(self, id):
        Match(self.root, self.frame, id, self.main_page, self)

    def change_match_interval(self, nb):
        if nb < 0:
            if self.start == len(self.matches)-1:
                reste = self.start % 11
                self.start -= reste
            else:
                self.start = max(self.start+nb, 0)
            self.build()
        else:
            if self.start+11 < len(self.matches)-1:
                self.start = min(self.start+nb, len(self.matches)-1)
                self.build()

    def build(self):

        self.clear()
        self.root.title("Match List Search Result")
        self.root.bind("<Left>", self.go_to_last_page)

        Label(self.frame, text = "Search Result", font=("Verdana","15","underline")).grid(column = 1, row = 0, padx = 10, pady = 10)

        self.load_from_match()
    
    def load_from_match(self):
        self.match_container = Frame(self.frame)
        self.match_container.grid(column=0, row = 1, columnspan=3)
        matches = self.matches[self.start:self.start+11]
        id = 0
        for id,match in enumerate(matches):
            colors = {"Howling Abyss ":"light goldenrod","Summoner's Rift Ranked (Draft Mode)":"brown","Summoner's Rift Normal (Draft Mode)": "orange", "Summoner's Rift ":"yellow"}
            if match[3] in colors:
                Button(self.match_container, text  = match[1]+"   |   "+str(match[4])+"/"+str(match[5])+"/"+str(match[6])+"   |   "+match[3]+"\n\n"+match[10], font=("Verdana","10"), bg = colors[match[3]], width = 70, height = 3, command = lambda x =  match[0]: self.go_to_match(x)).grid(column = 0, row = id, padx = 10, pady = 10, columnspan=2)
            else:
                Button(self.match_container, text  = match[1]+"   |   "+str(match[4])+"/"+str(match[5])+"/"+str(match[6])+"   |   "+match[3]+"\n\n"+match[10], font=("Verdana","10"), bg = "grey", width = 70, height = 3, command = lambda x =  match[0]: self.go_to_match(x)).grid(column = 0, row = id, padx = 10, pady = 10, columnspan=2)
            
            if match[11] == 1:
                Button(self.match_container, bg = "green", width = 7, height = 3).grid(column = 2, row = id, padx = 10, pady = 10)
            else:
                Button(self.match_container, bg = "red", width = 7, height = 3).grid(column = 2, row = id, padx = 10, pady = 10)
            
        Button(self.match_container, text = "<<", command = lambda x = -11 : self.change_match_interval(x), font=("Verdana","10")).grid(column = 0, row = id+1)
        Button(self.match_container, text = "Go Back to Main Page", width = 55, height = 2, command = self.go_to_main_page, font=("Verdana","11"), bg = "grey").grid(column = 1, row = id+1)
        Button(self.match_container, text = ">>", command = lambda x = 11 : self.change_match_interval(x), font=("Verdana","10")).grid(column = 2, row = id+1)
        self.center_window()