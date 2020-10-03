# You will store your poem in a .txt file. Feel free to use any poem of your choice!

# Create a function called get_file_lines():

# It should have 1 parameter called filename, which is a string of the filename.
# It should return a list of strings containing the lines of the file.
# Create a function called lines_printed_backwards():
# It should have 1 parameter called lines_list, which is a list of strings containing lines of your poem.



def get_file_lines(filename):
    file_lines = open(filename, "r")
    for x in file_lines:
        print(x)

get_file_lines("poem.txt")

#It should print the lines of the poem in reverse. Include the original line number at the beginning of each line.

def lines_printed_backwards(lines_list):
    with open(lines_list, "r") as read_obj:
        lines = read_obj.readlines()
        lines = [line.strip() for line in lines]
        lines = reversed(lines)
        return lines

lines_backwards = lines_printed_backwards("poem.txt")

for line in lines_backwards:
    print(line)


# lines_printed_backwards("poem.txt")

# def lines_printed_random(lines_list):



# def lines_printed_custom(lines_list):



