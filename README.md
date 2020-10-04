Name: Poetry Slam

This is my CS1.0 Poetry Slam assignment. The assignment emcompasses 
maniuplating File IO and dictionaries. It reads from the text file 
poem.txt.

It has four functions. 

1. Function: get_file_lines() prints the list of strings
contained within the txt file. Spaces are removed for clarity.

2. Function: lines_printed_backwards() prints the list of strings
from the txt file but from back to front. This is accomplished
by running the lines variable with "lines = reversed(lines)".
The extra spaces are removed from between the strings and the 
original line number appears beside each line of text. 

3. Function: lines_printed_random() prints the list of strings 
from the text file using the import random module. The 
variable lines is applied to "random.shuffle(lines)". Each time 
the function is run the lines of text will be randomized. 
The extra spaces are removed from between the strings and the 
original line number appears beside each line of text. 

4. Function: lines_printed_random() prints the poem in my own
unique way. 