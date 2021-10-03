from os import path
from io import StringIO
import os
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from summa import summarizer
from summa import keywords
from gensim.summarization import keywords as key

def get_summary(path):
    with open(path, 'r') as f:
        text = f.read()
        #text is a string
        summary_ratio = 0.5
        summary_words = 300
        summary_final = summarizer.summarize(text, ratio=summary_ratio)  #for words , words = summary_words
        return summary_final

def summarisation_engine():
    print("Enter Exact file name for which you wish to generate Summary : ")
    file_name = input()
    if(path.exists(file_name) == False):
        print("Input File Does not Exist !! Returning to Main Menu")
        return
    new_file_name = file_name[:len(file_name)-4] + "_summary.txt"
    if(path.exists(new_file_name) == True):
        print("Given file already exists!!")
        print("Do you wish to overwrite the existing summary file ? (Y/N) - ", end="")
        temp = input()
        if(temp=="y" or temp=="Y"):
            pass
        else:
            return
    summarized_text = get_summary(file_name)
    with open(new_file_name, "a") as file:
        file.write(summarized_text)
        file.write("\n")
    print("Summary stored in ",new_file_name,)
    print("Returning now to Main Menu")