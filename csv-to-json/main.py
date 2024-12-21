import sys
import csv
import json

args = sys.argv
# print(args)
delimiter = ";"
quotechar = "'"


def help():
    print("""$ python main.py --delimiter ',' --quotechar '"' test.csv""")
    sys.exit(0)


if len(args) < 2:
    help()


if "--help" in args:
    help()

if "--delimiter" in args:
    delimiter = args[args.index("--delimiter") + 1]
    # print(delimiter)

if "--quotechar" in args:
    quotechar = args[args.index("--quotechar") + 1]
    # print(quotechar)


file = args[-1]

fileContext = open(file, "r", newline="")
# print(fileContext.read())

json_data = []
properties = []
line = 1
csvContext = csv.reader(fileContext, delimiter=delimiter, quotechar=quotechar)
for row in csvContext:
    if line == 1:
        properties = row
    else:
        row_dict = {properties[i]: row[i] for i in range(len(properties))}
        json_data.append(row_dict)

    line += 1

print(json.dumps(json_data, indent=4))
