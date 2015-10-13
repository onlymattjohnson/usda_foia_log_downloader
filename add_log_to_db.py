#!env/bin/python
import csv, sys

def get_file_contents(file_name):
    result = []
    with open(file_name, 'rb') as csvfile:
        filereader = csv.reader(csvfile)
        for row in filereader:
            result.append(row)

    return result
    

try:
    file_name = sys.argv[1]
except:
    print "You must give an argument for the name of the file"
    sys.exit(1)

print get_file_contents(file_name)