# some basic python code
print("Hello")

# declare vars
x = 12
y = 5.4


# a function
def multiply():
    return x * y


# call the function
result = multiply()
print(result)


#
# strings
#

multi_line = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(multi_line)

# slicing
# slice string from index 0 to 5 - first character is at index 0
print(multi_line[0:5])
# just on position 1
print(multi_line[1])


# from the start to 5 + make it lower case
print(multi_line[:5].lower())
# from 6 to end + make it upper case
print(multi_line[6:].upper())

# length of string
print(len(multi_line))

# check if a word is in a string
print("et" in multi_line)  # True
print("tex" in multi_line)  # False


#
# if
#
if "Lorem" not in multi_line:
    print("Not in the text")
else:
    print("In the text")
