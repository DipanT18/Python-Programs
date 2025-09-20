import sys

if (len(sys.argv) < 3):
    sys.exit("Too few command-line arguments")
if (len(sys.argv) > 3):
    sys.exit("Too many command-line arguments")
if sys.argv[1].split(".")[-1] != "csv" and sys.argv[2].split(".")[-1] != "csv":
    sys.exit("Not a CSV file")
toAppend=[]
try:
    with open(sys.argv[1], "r") as file:
        next(file)
        for line in file:
            row=line.rstrip().replace('"','').split(',')
            toAppend.append(f"{row[1]},{row[0]},{row[-1]}\n".strip(" "))
    with open(sys.argv[2], "w") as file:
        file.write(f"first,last,house\n")
        for lines in toAppend:
            file.write(lines)


except FileNotFoundError:
    sys.exit("File does not exit")
