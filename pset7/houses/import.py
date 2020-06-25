import sys
import csv
from cs50 import SQL

if(len(sys.argv) != 2):
    print("Command-Line Arguement")
    exit()
    
db = SQL("sqlite:///students.db")
# db.execute("CREATE TABLE students (first TEXT, middle TEXT, last TEXT, house TEXT, birth NUMERiC)")

with open(sys.argv[1], "r") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        name = (row["name"].split())
        name.append(row["house"])
        name.append(row["birth"])
        if(len(name) == 4):
            db.execute("INSERT INTO students (first, last, house, birth) VALUES (?, ?, ?, ?)", name[0], name[1], name[2], name[3])
        elif(len(name) == 5):
            db.execute("INSERT INTO students (first, middle, last, house, birth) VALUES (?, ?, ?, ?, ?)", name[0], name[1], name[2], name[3], name[4])
            