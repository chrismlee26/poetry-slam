def get_file_lines(filename):
    file_lines = open(filename, "r")
    for x in file_lines:
        print(x, end="")
        file_lines.close

get_file_lines("poem.txt")

\
print('**break**')
\


def lines_printed_backwards(lines_list):

    lines_list = open("/Users/chris/dev/courses/cs1.0/poetry-slam/poem.txt", "r").readlines()
    lines_list = lines_list[::-1]

    num_line = len(lines_list)

    for line in range(len(lines_list)):
        reversed_line = str(num_line - line) + " " + lines_list[line]
        print(reversed_line)

lines_printed_backwards("poem.txt")


\
print('**break**')
\

import random

def lines_printed_random(lines_list):
    with open(lines_list, "r") as read_obj:

        lines = read_obj.readlines()
        lines = [line.strip() for line in lines]

        random.shuffle(lines)
        return lines

lines_random = lines_printed_random("poem.txt")

for line in lines_random:
    print(line)


# # \
# print('**break**')
# \



# import random

# def lines_printed_random(lines_list):
#     with open(lines_list, "r") as read_obj:

#         lines = read_obj.readlines()
        
#         for line in lines:
#             lines = line.strip() 
#             random.shuffle(lines)
            
#             line_number = str(line) + " " + lines[line]
#             print(line_number)
            
#             return lines
#         # lines.close

# lines_random = lines_printed_random("poem.txt")

# for line in lines_random:
#     print(line)


# # \
# print('**break**')
# \

# Fourth Question (Custom)
# def lines_printed_custom(lines_list):

# def lines_printed_custom(lines_list):
#     with open(lines_list, "r") as read_obj:

#             lines = read_obj.readlines()
#             lines = [line.strip() for line in lines]



