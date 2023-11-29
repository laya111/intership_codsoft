import random

lc = "abcdefghijklmnopqrstuvwxyz"
up = "ABCDEFGHHIJKLMNOPQRSTUVWXYZ"
no = "0123456789"
symbols = "@#$%^&*?\/!"
use_for = lc + up + no + symbols

try:
    while True:
        ps_len = int(input("Enter password length: "))
        
        if ps_len < 8:
            print("Length should be more than 8 characters.")
        else:
            pass1 = "".join(random.sample(use_for, ps_len))
            print("Your generated password:", pass1)
            
           
            exit_choice = input("Do you want to exit? (y/n): ").lower()
            if exit_choice == 'y':
                break  
except ValueError:
    print("Please enter an integer value.")
except:
    print("exception occured..")
