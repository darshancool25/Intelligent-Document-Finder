from __future__ import absolute_import
from __future__ import division, print_function, unicode_literals

from sumy.parsers.html import HtmlParser
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer as Summarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words
from PyPDF2 import PdfFileReader
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO
import os
import nltk                                                  #library uesd to get unique keywords
import re                                                    #library uesd to get unique keywords
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from summa import summarizer
from summa import keywords 
from gensim.summarization import keywords as key
import warnings
import pandas as pd
import pymysql
import mysql.connector
from mysql.connector import Error

warnings.filterwarnings("ignore")

'''def stem(word):                                     #function to get unique keywords
	regexp=r'^(.*?)(ing|ly|ed|ious|ies|ive|s|ment)?$'
	stem,suffix=re.findall(regexp,word)[0]
	return stem
'''
def get_file_name(first_name,keyword,connection):
        cursor = connection.cursor()
        cursor.execute('SELECT txt_name FROM USERS U INNER JOIN TEXT_FILES T ON U.user_id = T.user_id WHERE First_Name = %s AND  ( txt_keyword_1 = %s  ) ;',(first_name,keyword))
        record = cursor.fetchall()
        return str(record[0][0])

def get_info(path):
    with open(path, 'r') as f:
        text = f.read()        
        LANGUAGE = "english"
        SENTENCES_COUNT = 10
        #url = "https://en.wikipedia.org/wiki/Automatic_summarization"
        #parser = HtmlParser.from_url(url, Tokenizer(LANGUAGE))
        # or for plain strings
        parser = PlaintextParser.from_string(text, Tokenizer(LANGUAGE)) #PlaintextParser.from_file for files
        stemmer = Stemmer(LANGUAGE)

        summarizer = Summarizer(stemmer)
        summarizer.stop_words = get_stop_words(LANGUAGE)
        
        print("SUMMARY","\n")
        for sentence in summarizer(parser.document, SENTENCES_COUNT):
            print(sentence)

        #print(keywords.keywords(text))                  #original keywords
        '''keywordlist1=keywords.keywords(text,split=True)  #list of keywords
        keywordstring=" ".join(keywordlist1)             #string of keywords
        tokens= nltk.word_tokenize(keywordstring)

        print("\n","KEYWORDS")
        print("\n",{stem(t) for t in tokens},"\n")       # gives set of unique kywords 
        '''   
connection = mysql.connector.connect(host='idfproject-1.cncp58rbjwbv.ap-south-1.rds.amazonaws.com',database='idfproject',user='idf',password='idf12345')
if connection.is_connected():
        print("Connected to MySQL Server version ", connection.get_server_info(),"\n")
        first_name=input()
        keyword=input()
        path='C:\\Users\\AMAN SHAKYA\\Desktop\\Infenion Startup India Project\\codes\\' + get_file_name(first_name,keyword,connection) + '.txt'
        get_info(path)    

