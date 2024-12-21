import sys
import csv

args = sys.argv
print(args)
delimiter = ";"
quotechar = "'"

if "--delimiter" in args:
    delimiter = args[args.index("--delimiter") + 1]
    print(delimiter)

if "--quotechar" in args:
    quotechar = args[args.index("--quotechar") + 1]
    print(quotechar)

file = args[-1]

fileContext = open(file, "r", newline="")
# print(fileContext.read())

csvContext = csv.reader(fileContext, delimiter=delimiter, quotechar=quotechar)
for row in csvContext:
    print(row)
