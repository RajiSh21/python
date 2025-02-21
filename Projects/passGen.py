import random
import string

def passGen(min_length, number=True, special_char=True):
    letters = string.ascii_letters
    digits = string.digits
    special_char = string.punctuation

    char =  letters
    if number:
        char += digits
    if special_char:
        char += special_char

    password= ""
    meets_criteria = False
    has_number = False
    has_special_char = False

    while not meets_criteria or len(password) <min_length:
        new_char = random.choice(char)
        password += new_char

        if new_char in digits:  
            has_number = True
        elif new_char in special_char:
            has_special_char = True

        meets_criteria = True
        if number :
            meets_criteria = has_number
        if special_char:
            meets_criteria = meets_criteria and has_special_char 

    return password
min_length = int(input("Enter the minumum length: "))
has_number = input("Do you want to include numbers? (y/n): ").lower()=="y"
has_special_char = input("Do you want to include special characters? (y/n): ").lower()=="y"
pwd=passGen(min_length, has_number, has_special_char)   
print("The generated password is:",pwd)