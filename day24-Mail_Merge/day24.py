file = open(r"day24-Mail_Merge\my_text.txt")
content = file.read()
print(content)
file.close() # To free up the resources occupied by the file

# Method that devs use to open files
with open(r"day24-Mail_Merge\my_text.txt",mode="w") as file:
    # content = file.read()
    print(content) # Auto closes the file once operations are done
    file.write("This is an example") # Gives error because the file opens in read mode only by default

# New file gets created if file doesn't exist in write mode
with open(r"day24-Mail_Merge\new_file.txt", mode="w") as file:
    file.write("New file creation")

# Write mode erases current content; Use append mode to add content without erasing the present content
with open(r"day24-Mail_Merge\my_text.txt", mode="a") as file:
    file.write("This is append function this does not erase current content")

with open(r"day24-Mail_Merge\my_text.txt") as file:
    print(file.read())

# Some methods in python for mail merge
# File.readlines() - returns each line of text as a list object
# String replace() - replaces 1 specified phrase to another phrase
# strip() - removes white space 


