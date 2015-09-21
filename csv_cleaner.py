import csv, sys

# Check if csv file is formatted right
def check_file(file_name):
    csv_list = []
    with open(file_name, 'rb') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            csv_list.append(row)

    print csv_list[0][0]
    

file_name = sys.argv[1]
check_file(file_name);