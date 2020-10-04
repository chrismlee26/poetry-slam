def lines_printed_backwards(lines_list):
    
    with open(lines_list, "r") as read_obj:
        lines = read_obj.readlines()
        lines = [line.strip() for line in lines]
        lines = reversed(lines)
        
        return lines

lines_backwards = lines_printed_backwards("poem.txt")

for backward in lines_backwards:
    print(backward)

