# DAY 9
# Grading problem
student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}
 
# Create an empty dictionary to collect the new values.
student_grades = {}
 
# Loop through each key in the student_scores dictionary
for student in student_scores:
 
    #Get the value (student score) by using the key each time.
    score = student_scores[student]
 
    #Check what grade the score would get, then add it to student_grades
    if score >= 91:
        student_grades[student] = 'Outstanding'
    elif score >= 81:
        student_grades[student] = 'Exceeds Expectations'
    elif score >= 71:
        student_grades[student] = 'Acceptable'
    else:
        student_grades[student] = 'Fail'

# Nested Lists and Dictionaries
country = {
    "Karnataka" : ["Bangalore","Hubli","Mandya","Mysore"],
    "Tamil Nadu" : {
    "Madurai": ["Meenakshi","Shiva","Parvati"],
    "Kanchi":"Kamakshi",
    },
    "Kerala":"Cochin"
}

print(country["Karnataka"][2]) # Mandya will be printed
print(country["Tamil Nadu"]["Kanchi"]) # Kamakshi will be printed
print(country["Tamil Nadu"]["Madurai"][2]) # Parvati will be printed

# Day 9 Project - The Silent Auction
print(r'''
  _______ _             _____ _ _            _                        _   _             
 |__   __| |           / ____(_) |          | |       /\             | | (_)            
    | |  | |__   ___  | (___  _| | ___ _ __ | |_     /  \  _   _  ___| |_ _  ___  _ __  
    | |  | '_ \ / _ \  \___ \| | |/ _ \ '_ \| __|   / /\ \| | | |/ __| __| |/ _ \| '_ \ 
    | |  | | | |  __/  ____) | | |  __/ | | | |_   / ____ \ |_| | (__| |_| | (_) | | | |
    |_|  |_| |_|\___| |_____/|_|_|\___|_| |_|\__| /_/    \_\__,_|\___|\__|_|\___/|_| |_|                                                                                        
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
''')

repeat=True
bidders={}
while repeat:
    print("\nWelcome to the Secret Auction Program!\n")
    name=input("What is your name?\n")
    bid=int(input("What is your bid?\n$"))
    bidders[name]=bid
    other=input("Are there any other bidders? Type 'yes' or 'no'. \n")
    if other=="yes":
        print("\n" * 100)
    else:
        repeat=False
        print("\n" * 100)

# Approach 1
max_value=max(bidders.values())
for name,bid in bidders.items():
    if bid==max_value:
        max_bidder=name

# Approach 2
for bidder in bidders:
    max_bidder=''
    max_value=0
    bid_amount=bidders[bidder]
    if bid_amount>max_value:
        max_value=bid_amount
        max_bidder=bidder
print(f"The winner is {max_bidder} with a bid of ${max_value}")



