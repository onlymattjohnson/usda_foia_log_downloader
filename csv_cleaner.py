import csv, sys

# Check if csv file is formatted right
def check_file(csv_list, needles):
    first_cell = csv_list[0][0]
    
    if first_cell in needles:
        return True

    return False
    
def find_good_row(csv_list):
    counter = 0
    for row in csv_list:
        if row[0] in needles:
            return counter
        counter = counter + 1
    return -1

def load_csv(file_name):
    csv_list = []
    with open(file_name, 'rb') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            csv_list.append(row)

    return csv_list

file_name = sys.argv[1]
needles = ['Request ID', 'CASE NO.']
csv_list = load_csv(file_name)

if not check_file(csv_list, needles):
    # First row is bad, find the starting row
    good_row = find_good_row(csv_list)
    print 'Found good row, attempting re-write'
    f = csv.writer(open(file_name, 'wb'))
    for line in csv_list[good_row:]:
        f.writerow(line)
        