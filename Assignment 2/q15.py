import csv
import sys

f = open('hello.csv', 'rt')
try:
    reader = csv.reader(f)
    for row in reader:
        print (row)
finally:
    f.close()