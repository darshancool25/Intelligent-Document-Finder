from summary_util import summarisation_engine
from helper_functions import take_notes

'''
A menu driven program for Hands Free Note Taking
'''
while(True):
    print(":::::::::::WELCOME TO Smart Hands Free Note Taking App:::::::::::\n")
    print("MENU - ", "\n1. Record Note(s)" , "\n2. Summarisation Engine", "\n3. Exit")
    print("Enter your Choice - ",end="")
    try:
        choice = int(input())
    except:
        print("Invalid Input!")
        continue
    if(choice == 1):
        take_notes()
    elif (choice == 2):
        summarisation_engine()
    if(choice == 3):
        break
    if(choice!=1 and choice!=2 and choice!=3):
        print("Invalid Input!! ",end="")
    print("Do you Wish to Continue ? (Y/N) - ", end="")
    temp = input()
    if(temp=="y" or temp=="Y"):
        continue
    else:
        break