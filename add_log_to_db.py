#!env/bin/python
import csv, sys

def get_file_contents(file_name):
    result = []
    reader = csv.DictReader(open(file_name))

    for row in reader:
        result.append(row)

    return result
    

try:
    file_name = sys.argv[1]
except:
    print "You must give an argument for the name of the file"
    sys.exit(1)

print get_file_contents(file_name)