# Simpliest solution for #1. Variable into open. For loop to read. Print with no spaces. Program closes. 

def get_file_lines(filename):
    file_lines = open(filename, "r")
    for x in file_lines:
        print(x, end="")
        file_lines.close

get_file_lines("poem.txt")

\
print('**break**')
\

# Second Question (Backwards):
# It should print the lines of the poem in reverse. Include the original line number at the beginning of each line.

def lines_printed_backwards(lines_list):
    with open(lines_list, "r") as read_obj:
        lines = read_obj.readlines()
        lines = [line.strip() for line in lines]
        lines = reversed(lines)
        return lines
        lines.close

lines_backwards = lines_printed_backwards("poem.txt")

for line in lines_backwards:
    print(line)

\
print('**break**')
\

# Third Question (Random):
# def lines_printed_random(lines_list):

import random

def lines_printed_random(lines_list):
    with open(lines_list, "r") as read_obj:

        lines = read_obj.readlines()
        lines = [line.strip() for line in lines]

        random.shuffle(lines)
        return lines
        lines.close

lines_random = lines_printed_random("poem.txt")

for line in lines_random:
    print(line)


\
print('**break**')
\

# Fourth Question (Custom)
# def lines_printed_custom(lines_list):

# def lines_printed_custom(lines_list):
#     with open(lines_list, "r") as read_obj:

#             lines = read_obj.readlines()
#             lines = [line.strip() for line in lines]



