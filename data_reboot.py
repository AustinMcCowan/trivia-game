#!/usr/bin/python3
# Austin McCowan
# 1/28/2020

''' Reboots the data incase it becomes broken and thus unusable '''

import pickle

erase_content = {}

def fix_it():
    datafile = open("game_scores.pickle", "wb")
    pickle.dump(erase_content, datafile)
    datafile.close()
    