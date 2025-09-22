import sys

if (len(sys.argv) <2):
    sys.exit("Too few command-line arguments")
if (len(sys.argv) > 2):
    sys.exit("Too many command-line arguments")
if sys.argv[1].split(".")[-1]!="py":
    sys.exit("Not a python file")
lineNumber=0
try:
    with open(sys.argv[1],"r") as file:
        for line in file:
            if (not line.rstrip().strip().startswith("#") and line.strip()):
                lineNumber+=1
        print(lineNumber)
except FileNotFoundError:
    sys.exit("File does not exit")
