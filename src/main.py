import os
from functions import filemake, filepath

#TODO: ADD CLI METHOD TO READ IN DESIRED USER FILEPATH

#UPON EXECUTION
try:
    os.mkdir("%s/copypaste" % filepath)
except FileExistsError:
    None
filemake()

var = 1 
while var > 0:
    repeat = input("Would you like to create any additional files? (y/n): ")
    if repeat == "y":
        filemake()
    else:
        var -= 1