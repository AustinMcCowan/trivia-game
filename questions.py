#!usr/bin/python3
# Austin McCowan and Chris Huffman
# 3/12/2020

class Questions(object):
    def __init__(self):
        self.vgames = { "What game has the most sales?": [("Minecraft", 1), ("Tetris", 0), ("Wii Sports", 0), ("Frogger", 0)],
                        "What Inspired Tetris?": [("Pentominoes", 1), ("Chess", 0), ("Legos", 0), ("Durak", 0)],
                        "Who was the first person to achieve a perfect score on pac-man?":[("Billy Mitchell", 1), ("Toru Iwatani", 0), ("Antonio Romero Monteiro", 0),("Adam Montoya", 0)] 
                        }
        
        self.history = {}
        
        self.music = {}
        
        self.geography = {}