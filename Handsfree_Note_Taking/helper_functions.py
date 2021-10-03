from __future__ import absolute_import
from __future__ import division, print_function, unicode_literals
import sys
import datetime
from os import path
import os
from io import StringIO
import warnings
import pandas as pd
# Custom module
from speech_to_text import record_until_interrupt
warnings.filterwarnings("ignore")

def start_recording(rec_type, file_name):
    if(rec_type == 1):
        file_name += str(datetime.datetime.now()) + ".txt"
        file_name = file_name.replace(' ' , '_')
        file_name = file_name.replace(':' , '-')
        print("Starting recording in file - ",file_name)
        print("Press CTRL + C to interrupt the recording anytime!")
        text = record_until_interrupt()
        with open(file_name, "w") as file:
            file.write(text)
            file.write("\n")
        print("Current Recording Finished, returing back to main Menu now")

    if(rec_type == 2):
        print("Continuing Recording notes in file - ",file_name)
        print("Press CTRL + C to interrupt the recording anytime!")
        text = record_until_interrupt()
        with open(file_name, "a") as file:
            file.write(text)
            file.write("\n")
        print("Current Recording Finished, returing back to main Menu now")

def take_notes():
    print("\nRecord Note Menu - ")
    print("1. Record a new note \n2. Continue in an existing note")
    try:
        choice = int(input("Enter your choice - "))
    except:
        print("Invalid input, returning to Main Menu")
        return
    if(choice == 1):
        print("Enter name for New Note : ",end="")
        new_file_name = input()
        start_recording(choice,new_file_name)

    elif(choice == 2):
        print("Enter Exact file name in which you want to continue taking notes : ")
        old_file_name = input()
        if(path.exists(old_file_name) == False):
            print("Given file does not exist!!")
            return
        start_recording(choice,old_file_name)
    else:
        print("Invalid input, returning to Main Menu")
        return