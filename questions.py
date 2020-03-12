#!usr/bin/python3
# Austin McCowan and Chris Huffman
# 3/12/2020

class Questions(object):
    def __init__(self):
        self.vgames = { "What game has the most sales?": [("Minecraft", 1), ("Tetris", 0), ("Wii Sports", 0), ("Frogger", 0)],
                        "What Inspired Tetris?": [("Pentominoes", 1), ("Chess", 0), ("Legos", 0), ("Durak", 0)],
                        "Who was the first person to achieve a perfect score on pac-man?":[("Billy Mitchell", 1), ("Toru Iwatani", 0), ("Antonio Romero Monteiro", 0),("Adam Montoya", 0)],
                        "How many official Legend of Zelda titles are there?": [("19", 1), ("18", 0), ("27", 0), ("14", 0)],
                        "What year was Super Mario world released?": [("1990", 1), ("1991", 0), ("1999", 0), ("1988", 0)],
                        "What was the first video game created?": [("OXO", 1), ("Tennis for two", 0), ("Pong", 0), ("Computer Space", 0)],
                        "What Game won GOTY in 2017":[("Persona 5", 0),("Legend of Zelda: BOTW", 1),("Cuphead", 0),("Super Mario Odyssey", 0)],
                        "What is the best selling game console of all time?":[("Nintendo DS", 0),("Playstation 2", 1),("Gameboy", 0),("Wii", 0)],
                        "Who is Luigi related to?":[("Link", 0),("Mario", 1),("Princess Peach", 0),("Yoshi", 0)],
                        "Who voices Mario?":[("Charles Andre Martinet", 1),("Kazuma Totaka", 0),("Tom Kenny", 0),("Steven Burton", 0)] }
        
        self.history = { "What triggered the introduction of the US into WW2?":[("Pearl Harbor", 1),("Assassination of Franz Ferdinand", 0),("The Manhattan Project", 0),("The Sinking of the Titanic", 0)],
                         "How many years did it take to finish the Great Wall of China?":[("2500", 1),("600", 0),("33", 0),("1005", 0)],
                         "When was the Declaration of Independence signed?":[("1776", 1),("1777", 0),("1818", 0),("1786", 0)],
                         "When was the first anime created?":[("1917", 1),("1930", 0),("1950", 0),("1970", 0)],
                         "What country did the Mongols invade in 1237?":[("Russia", 1),("China", 0),("India", 0),("Poland", 0)],
                         "What year did the Titanic sink?":[("1912", 1),("1918", 0),("1910", 0),("1891", 0)],
                         "How much was the Louisiana Purchase?":[("$15 million", 1),("$2 million", 0),("$500k", 0),("$156 million", 0)],
                         "When was the steam engine built?":[("1712", 1),("1800", 0),("1760", 0),("1860", 0)],
                         "Who was the first King of England":[("Æthelstan", 1),("King George I", 0),("King Charles I", 0),("Ælfweard", 0)],
                         "Who created the hot dog in 1901?":[("Harry M. Stevens", 1),("Thomas Alva Edison", 0),("George Crum", 0),("Colonel Sanders", 0)], }
        
        self.music = {  "":[("",),("",),("",),("",)],
                         "":[("",),("",),("",),("",)],
                         "":[("",),("",),("",),("",)],
                         "":[("",),("",),("",),("",)],
                         "":[("",),("",),("",),("",)],
                         "":[("",),("",),("",),("",)],
                         "":[("",),("",),("",),("",)],
                         "":[("",),("",),("",),("",)],
                         "":[("",),("",),("",),("",)],
                         "":[("",),("",),("",),("",)], }
        
        self.geography = {}