import csv 
from sys import argv, exit


def main():
    #Check if number of command_line arguments is correct
    if len(argv) < 3:
        exit('Too few command-line arguments')
    elif len(argv) > 3:
        exit('Too many command-line arguments')
    else:
        #Check if the first argument (input file) has a .csv extension
        if not argv[1].endswith('.csv'):
            exit('Not a CSV file')
        else:
            ...


def scourge(before, after):
    try:
        #Open the input CSV file for reading and output CSV file for writing
        with open(argv[1]) as before, open(argv[2], 'w', newline='') as after:
            reader = csv.DictReader(before)
            header = ['first', 'last', 'house']
            writer = csv.DictWriter(after, fieldname=header)
            writer.writeHeader()
            
    except:
        ...



if __name__ == '__main__':
    main()