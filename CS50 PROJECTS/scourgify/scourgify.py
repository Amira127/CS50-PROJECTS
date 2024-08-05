import sys
import csv

def main():
    try:
        check_command_line()
        output = []
        with open(sys.argv[1], "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                DATA ={}
                DATA["last"], DATA["first"] = row["name"].strip().split(", ")
                DATA["house"] = row["house"]
                output.append({"first": DATA["first"],"last": DATA["last"], "house" : DATA["house"]})

    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")

    with open(sys.argv[2], "w") as file:
        writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
        writer.writeheader()
        for student in output:
            writer.writerow(student)

def check_command_line():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    if sys.argv[1].endswith(".csv") == False or sys.argv[2].endswith(".csv") == False:
        sys.exit("Not a CSV file ")

if __name__ == "__main__":
    main()