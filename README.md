Name: Poetry Slam

This is my CS1.0 Poetry Slam assignment. The assignment emcompasses 
maniuplating File IO and dictionaries. It reads from the text file 
poem.txt.

It has four functions. 

1. Function: get_file_lines() prints the list of strings
contained within the txt file. Spaces are removed for clarity.

2. Function: lines_printed_backwards() prints the list of strings
from the txt file but from back to front. This is accomplished
by running the lines variable with lines_list = lines_list[::-1]
This also allows num_line = len(lines_list) to be run through
a for loop where num line is converted to a string and decremented
and then concatinated into the print function allowing the line
number to appear beside the poem text.

3. Function: lines_printed_random() prints the list of strings 
from the text file using the import random module. The 
variable lines is applied to "random.shuffle(lines)". Each time 
the function is run the lines of text will be randomized. 
The extra spaces are removed from between the strings.

4. Function: lines_printed_custom() prints the poem in my own
unique way. I have chosen to use some extremely elegant code to
reduce the true essence of the poem, "Remember", by Joy Harjo, 
into its most cussinct form through my masterpiece custom Haiku. 
This uses print functions along with the readline() command, to 
create the standard 5-7-5 syllable haiku out of only the first 
line of the poem. The 3rd line required an ingenious close 
function or order for the poem to be able to run again from the
start. 