import sys
import tabulate

if (len(sys.argv) <2):
    sys.exit("Too few command-line arguments")
if (len(sys.argv) > 2):
    sys.exit("Too many command-line arguments")
if sys.argv[1].split(".")[-1]!="csv":
    sys.exit("Not a CSV file")

table=[]
headers=[]
try:
    with open(sys.argv[1],"r") as file:
        for line in file:
            headers=line.rstrip().split(",")
            break
        for line in file:
            table.append(line.rstrip().split(","))
    print(tabulate.tabulate(table, headers, tablefmt="grid"))

except FileNotFoundError:
    sys.exit("File does not exit")
