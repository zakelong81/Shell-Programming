#!/usr/bin/python3.5
import pandas as pd
import csv
fieldsfilms = ['Year','Length','Title','Director']
df = pd.read_csv('Films.csv',skipinitialspace=True, usecols=fieldsfilms, encoding = "ISO-8859-1")


fieldsmovies = ['Title','Year','Length', 'budget', 'rating', 'Action','Animation','Comedy','Drama','Documentary','Romance', 'Short']
dm = pd.read_csv('Movies.csv',skipinitialspace=True, usecols=fieldsmovies, encoding = "ISO-8859-1")


dfm = pd.merge(df, dm, on=('Year','Title','Length'), how="inner")

dfm = dfm[pd.notnull(dfm['budget'])]
header = ['Title','Director','Year','Length', 'budget', 'rating', 'Action','Animation','Comedy','Drama','Documentary','Romance', 'Short']
dfm.to_csv('fm.csv', columns = header)


movie_dic = dfm.set_index('Title').T.to_dict()

while True:
    usr_input = input('> ')
    if (usr_input == "q"):
        break;
    elif (usr_input == "all"):
        for i in movie_dic:
            print (i)
    elif usr_input in movie_dic:
        for i, j in movie_dic[usr_input].items():
            print(i, j)
    elif usr_input not in movie_dic:
        print("Movie is not in the Database type all to see 'all' Movie name")
