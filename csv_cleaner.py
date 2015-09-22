import csv, sys

# Check if csv file is formatted right
def check_file(file_name):
    csv_list = []
    with open(file_name, 'rb') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            csv_list.append(row)

    first_cell = csv_list[0][0]
    needles = ['Request ID', 'CASE NO.']
    
    print first_cell
    if first_cell in needles:
        return True
    return False
    

file_name = sys.argv[1]

print check_file(file_name);