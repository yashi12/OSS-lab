import csv
import sys

f = open('hello.csv', 'rt')
try:
    reader = csv.reader(f,delimiter=';')
    for row in reader:
        if row[0][0] != '#':    #assuming no blank lines
            print (row)
finally:
    f.close()