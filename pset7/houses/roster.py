import sys
import csv
import sqlite3
from cs50 import SQL

if(len(sys.argv) != 2):
    print("Command-Line Arguement")
    exit()

house = sys.argv[1]

db = SQL("sqlite:///students.db")

house_list = db.execute("SELECT first, middle, last, birth FROM students WHERE house = (?) ORDER BY last, first", house)

for row in house_list:
    if(row["middle"] == None):
        print(row["first"]," ", row["last"], ", " "born", " ", row["birth"], sep="")
    else:
        print(row['first']," ", row["middle"], " ", row["last"], ", ", "born", " ", row["birth"], sep="")