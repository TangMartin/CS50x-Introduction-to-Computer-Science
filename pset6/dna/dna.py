import sys
import csv

dif_sequence = {}

if(len(sys.argv) != 3):
    print("Command-Line Arguement")
    exit(1)

with open(sys.argv[1]) as csvfile:
    data = csv.reader(csvfile)
    row = list(data)
    sequence_names = row[0]
    sequence_names.pop(0)

for item in sequence_names:
    dif_sequence[item] = 1
    
with open(sys.argv[2]) as text:
    dna = text.read()
    dna.rstrip()
    
for key in dif_sequence:
    length = len(key)
    temp = 0
    max_temp = 0
    
    for i in range(len(dna)):
        
        while temp > 0:
            temp -= 1
            continue
        
        if(dna[i: i + length] == key):
            while(dna[i - length: i] == dna[i: i + length]):
                temp += 1
                i += length
            
        if(temp > max_temp):
            max_temp = temp
        
    dif_sequence[key] += max_temp
    
    
    

