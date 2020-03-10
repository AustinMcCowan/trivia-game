#!usr/bin/python3
# Austin McCowan and Chris Huffman
# 3/10/2020

''' Trivia game. Will have 5 categories for quizzes: History, geography, videogames, music, and random. 
Will have a highscore thing'''

# Imports
import pickle
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from tkinter import messagebox
import data_reboot as dr

# Constants
TITLE_FONT = ("Times New Roman", 24)

# Classes
class Data(object):
    def __init__(self):
        
        # Try and open the pickle file and grab contents
        try: 
            datafile = open("game_scores.pickle", "rb")
            self.scores = pickle.load(datafile)
            
        # If unable to grab content, run the function inside of data_reboot.py. Then try loading content again.    
        except:            
            dr.fix_it()
            print("Data failed to load; Erasing scores")
            datafile = open("game_scores.pickle", "rb")
            self.scores = pickle.load(datafile)
        
        # Close datafile    
        datafile.close()
        
    # updates the information in game_lib.pickle with the current information in the program (games)
    def save(self):
        try:
            datafile = open("game_scores.pickle", "wb")
            pickle.dump(self.games, datafile)
            datafile.close()
            
        except:
            
            # If file fails to load, raise error
            raise Exception("Data failed to save")


class MainMenu(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        
        self.lbl_title = tk.Label(self, text="Trivia Quiz", font=TITLE_FONT)
        self.lbl_title.grid(row=0, column=0, columnspan=3, sticky='news')
        
        self.btn_play = tk.Button(self, text="Play", command=self.go_triviasetup)
        self.btn_play.grid(row=1, column=1, sticky='news')
        
        self.btn_highscore = tk.Button(self, text="Highscore", command=self.go_leaderboard)
        self.btn_highscore.grid(row=2, column=1, sticky='news')
        
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        
        
    def go_leaderboard(self):
        leader_frame.tkraise()
        
    def go_triviasetup(self):
        popup = tk.Tk()
        popup.title("")
        
        frm_setup = TriviaSetup(popup)
        frm_setup.grid(row=0, column=0, sticky='news')
        popup.grid_columnconfigure(0, weight=1)        
        

class Leaderboard(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        
        self.lbl_title = tk.Label(self, text="Highscores", font=TITLE_FONT)
        self.lbl_title.grid(row=0, column=0, columnspan=3, sticky='news')
                                  
        self.scr_scoreboard = ScrolledText(self, height=20, width=30)
        self.scr_scoreboard.grid(row=1, column=0, columnspan=3, sticky='ns')        
        
        self.btn_back = tk.Button(self, text="BACK", command=self.go_mainmenu)
        self.btn_back.grid(row=2, column=1, sticky='news')
        
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        
        
    def go_mainmenu(self):
        main_frame.tkraise()


class TriviaSetup(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, master=parent)
        self.parent = parent
        
        self.lbl_category = tk.Label(self, text="Trivia Category:")
        self.lbl_category.grid(row=0, column=0, sticky='news')
        
        self.lbl_player = tk.Label(self, text="Player:")
        self.lbl_player.grid(row=1, column=0, sticky='news')
        
        self.categories = ["History", "Geography", "Videogames", "Music", "Random"]
        self.tkvar_categories = tk.StringVar(self)
        self.tkvar_categories.set(self.categories[4])
        self.dbx_category = tk.OptionMenu(self, self.tkvar_categories, *self.categories)
        self.dbx_category.grid(row=0, column=1, sticky='news')
        
        self.ent_player = tk.Entry(self)
        self.ent_player.grid(row=1, column=1, sticky='news')
        
        self.btn_confirm = tk.Button(self, text="Confirm", command=self.go_trivia)
        self.btn_confirm.grid(row=2, column=0, columnspan=2)
        
    def go_trivia(self):
        self.parent.destroy()
        
# Functions


# Main
if __name__ == "__main__":
    content = Data()
    root = tk.Tk()
    root.title("")
    root.resizable(False,False)
    root.geometry("400x450")
    
    main_frame = MainMenu()
    main_frame.grid(row=0, column=0, sticky='news')
    
    leader_frame = Leaderboard()
    leader_frame.grid(row=0, column=0, sticky='news')
    
    
    
    main_frame.tkraise()
    root.grid_columnconfigure(0, weight=1)
    root.mainloop()
