# Functions with Inputs
def greet(name):
    print(f"Hello {name}")
    print(f"What are you upto, {name}?")

greet("Ruby")

# Functions with multiple inputs
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"How is it in {location}?")

greet_with("Ruby", "Bengaluru")

# Keyword arguments
greet_with(location="Bangkok",name="Gennie")

# Love Calculator
def calculate_love_score(name1,name2):
    true=0
    love=0
    for c in name1.lower():
        if c == 't' or c=='r' or c=='u' or c=='e':
            true+=1 
        if c == 'l' or c=='o' or c=='v' or c=='e':
            love+=1 
    for c in name2.lower():
        if c == 't' or c=='r' or c=='u' or c=='e':
            true+=1 
        if c == 'l' or c=='o' or c=='v' or c=='e':
            love+=1
        
    print(str(true)+str(love))
calculate_love_score("Angela Yu","Jack Bauer")

# Day 8  Project - Caesar Cipher
alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

go_again=True
print("""           
 ,adPPYba, ,adPPYYba,  ,adPPYba,  ,adPPYba,  ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88  I8[    ""  ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""   `"Y8ba,   ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa  aa    ]8I  88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"'  `"YbbdP"'  `"8bbdP"Y8 88   

           88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
""")
while go_again==True:
    dir = input("Type 'encode' to encrypt and 'decode' to decrypt.\n").lower()
    text = input("Type the text: \n")
    shift = int(input("Enter shift number: \n"))


    def encrypt(original_text,shift_num):
        encoded=''
        for c in original_text:
            shifted_pos=alphabet.index(c) + shift_num
            shifted_pos%=len(alphabet) # To keep the shift range between 0 and 25
            encoded += alphabet[shifted_pos]
        print(f"Here is the encoded result: {encoded}")

    def decrypt(original_text,shift_num):
        decoded=''
        for c in original_text:
            shifted_pos=alphabet.index(c)-shift_num
            shifted_pos%=len(alphabet) # To keep the shift range between 0 and 25
            decoded+= alphabet[shifted_pos]
        print(f"Here is the decoded text: {decoded}")


    if dir=="encode":
        encrypt(original_text=text,shift_num=shift)

    elif dir=="decode":
        decrypt(original_text=text,shift_num=shift)

    repeat=input("Type 'yes' if you want to go again. Otherwise type 'no'.\n" )

    if repeat=="no":
        go_again=False

# To combine both encryption and decryption in one function

    def caesar(original_text, shift_amount, encode_or_decode):
        decoded = ''
        if encode_or_decode == "decode":
            shift_amount *= -1
        for c in original_text:
            if c not in alphabet:
                decoded+=c
            else:
                shifted_pos = alphabet.index(c) + shift_amount
                shifted_pos %= len(alphabet)  # To keep the shift range between 0 and 25
                decoded += alphabet[shifted_pos]
        print(f"Here is the {encode_or_decode}d text: {decoded}")

    caesar(text,shift,dir)
    repeat=input("Type 'yes' if you want to go again. Otherwise type 'no'.\n" )

    if repeat=="no":
        go_again=False