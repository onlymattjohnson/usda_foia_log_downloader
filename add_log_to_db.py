#!env/bin/python
import csv, sys
from app import db, models

def get_file_contents(file_name):
    result = []
    reader = csv.DictReader(open(file_name),fieldnames=['CASE NO.','LAST NAME', 'FIRST NAME', 'AFFILIATION', 'DATE RECEIVED', 'DATE DUE OUT', 'TRACK', 'SUBJECT', 'CLOSURE DATE'])

    for row in reader:
        result.append(row)

    return result
    
def dict_to_db(data):
    # test
    my_dict = data[1]

    case_no = my_dict['CASE NO.']
    date_received = my_dict['DATE RECEIVED']
    date_due = my_dict['DATE DUE OUT']
    date_closed = my_dict['CLOSURE DATE']
    track = my_dict['TRACK']
    subject = my_dict['SUBJECT']

    print case_no, date_received, date_due, date_closed, track, subject

try:
    file_name = sys.argv[1]
except:
    print "You must give an argument for the name of the file"
    sys.exit(1)

mydict = get_file_contents(file_name)

dict_to_db(mydict)