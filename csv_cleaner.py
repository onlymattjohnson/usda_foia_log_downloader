import csv, sys

# Check if csv file is formatted right
def check_file(csv_list, needles):
    first_cell = csv_list[0][0]
        
    if ' '.join(first_cell.split()) in needles:
        return True

    return False
    
def find_good_row(csv_list, col_num):
    counter = 0
    for row in csv_list:
        if row[col_num] in needles:
            return counter
        counter = counter + 1
    return False

def load_csv(file_name):
    csv_list = []
    with open(file_name, 'rb') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            csv_list.append(row)

    return csv_list

file_name = sys.argv[1]
needles = ['Request ID', 'CASE NO.', 'CASENO', 'CASE NO']
csv_list = load_csv(file_name)

if not check_file(csv_list, needles):
    # First row is bad, find the starting row
    for i in range(0,len(csv_list[0])):
        good_row = find_good_row(csv_list, i)
        if good_row:
            break

    if good_row:
        print 'Found good row at col %s row %s, attempting re-write' % (str(i), str(good_row))
        f = csv.writer(open(file_name, 'wb'))
        for line in csv_list[good_row:]:
            f.writerow(line[i:])
    else:
        print '*** Could not find good row in file.\n\n'


        