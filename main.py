import csv 
from sys import argv, exit


def main():
    #Check if number of command_line arguments is correct
    if len(argv) < 3:
        exit('Too few command-line arguments')
    if len(argv) > 3:
        exit('Too many command-line arguments')



if __name__ == '__main__':
    main()