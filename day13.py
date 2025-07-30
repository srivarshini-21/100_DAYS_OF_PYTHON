def my_fun():
    for i in range(1,20):
        if i == 20:
            print("Yay")

my_fun() # No output because 'i' will never be 20 since the 20 in range() is exclusive

# Try and Except
try:
    age=int(input("Age: "))
except ValueError:
    print("Type in a numerical such as 15.")
    age=int(input("Age: "))
if age>18:
    print(f"You are {age} years old")

# Squash bugs using print()
pages=int(input("Number of pages: "))
words=int(input("Number of words: ")) # Error here - Use print statement to check - works only in some IDE's :)
total_words=pages * words