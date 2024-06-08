import csv
from sys import argv, exit


def main():
    # Check if number of command_line arguments is correct
    if len(argv) < 3:
        exit("Too few command-line arguments")
    elif len(argv) > 3:
        exit("Too many command-line arguments")
    else:
        # Check if the first argument (input file) has a .csv extension
        if not argv[1].endswith(".csv"):
            exit("Not a CSV file")
        else:
            scourge(argv[1], argv[2])


def scourge(before, after):
    try:
        # Open the input CSV file for reading and output CSV file for writing
        with open(argv[1]) as before, open(argv[2], "w", newline="") as after:
            reader = csv.DictReader(before)
            header = ["first", "last", "house"]
            writer = csv.DictWriter(after, fieldnames=header)
            writer.writeheader()

            # Process each row in input file
            for row in header:
                # Split the 'name' field into last name and first name
                lname, fname = row["name"].strip().split(", ")
                house = row["house"]
                # Write the processed data to the output file
                writer.writerow({"first": fname, "last": lname, "house": house})

    except FileNotFoundError:
        # Handle file not found error
        exit(f"Could not read {before}")


if __name__ == "__main__":
    main()
