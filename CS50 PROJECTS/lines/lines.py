import sys

# Check condition
if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

if sys.argv[1].endswith(".py") == False:
    sys.exit("Not a Python file")

# Count lines of code
try:
    lines = []
    count = 0
    with open(sys.argv[1]) as file:
        for line in file:
            row = line.lstrip()
            if row.startswith("#") == False and len(row) != 0:
                count += 1
    print(count)


# The file does not exist
except FileNotFoundError:
    sys.exit("File does not exist")
