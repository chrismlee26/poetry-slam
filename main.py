# Simmpliest solution for #1. Variable into open. for loop to read. print with no spaces. program closes. 
def get_file_lines(filename):
    file_lines = open(filename, "r")
    for x in file_lines:
        print(x, end="")
        file_lines.close

get_file_lines("poem.txt")


#First Question (Regular order):
# def get_file_lines(filename):
#     with open(filename, "r") as read_obj:
#         lines = read_obj.readlines()
#         return lines

# filename = get_file_lines("poem.txt")

# for line in filename:
#     print(line, end="")

# \

#Second Question (Backwards):
#It should print the lines of the poem in reverse. Include the original line number at the beginning of each line.

# def lines_printed_backwards(lines_list):
#     with open(lines_list, "r") as read_obj:
#         lines = read_obj.readlines()
#         lines = [line.strip() for line in lines]
#         lines = reversed(lines)
#         return lines
#         lines.close

# lines_backwards = lines_printed_backwards("poem.txt")

# for line in lines_backwards:
#     print(line)

# \

#Third Question (Random):
# def lines_printed_random(lines_list):

# def lines_printed_random(lines_list):
#     with open(lines_list, "r") as read_obj:
#         lines = read_obj.readlines()
#         lines = [line.strip() for line in lines]
#         lines = reversed(lines)
#         return lines
#         lines.close

# lines_random = lines_printed_random("poem.txt")

# for line in lines_random:
#     print(line)

# import random
# random_lines = random.choice(open("poem.txt").readlines())
# print(random_lines)

# import random

# def lines_printed_backwards(lines_list):
#     with open(lines_list, "r") as read_obj:
#         lines = read_obj.readlines()
#         lines = [line.strip() for line in lines]
#         lines = random.shuffle(lines)
#         return lines
#         lines.close

# lines_backwards = lines_printed_backwards("poem.txt")

# for line in lines_backwards:
#     print(line)



# def lines_printed_custom(lines_list):



