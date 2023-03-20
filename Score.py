import os
from Utils import *
POINTS_OF_WINNIG=0
def add_score(difficulty):
    global POINTS_OF_WINNIG
    POINTS_OF_WINNIG = (int(difficulty) * 3) + 5
    file1 = open("Scores.txt", "w")
    file1.write(str(POINTS_OF_WINNIG))
    file1.close()


# def calculate_points(difficulty):
#     return (difficulty * 3) + 5
