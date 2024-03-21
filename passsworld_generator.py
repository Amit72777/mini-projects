# generatoer a random password 
import random 

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

special_characters = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '{', '}', '[', ']', '|', '\\', ';', ':', '"', "'", '<', '>', ',', '.', '?', '/']

# taking input 
my_letter = int(input("how many letters would you like in your passworld?\n"))

my_symols = int(input("how man symbols would you like ? \n "))
my_numbers = int(input("how many number would you like? \n"))


password_list = []

# random   choice take a alhabate 
for i in range(my_letter):
    password_list.append(random.choice(alphabet))

# add random symbols 
for i in range(my_symols):
    password_list.append (random.choice(special_characters))

# add random numbers 
for i in range(my_numbers):
    password_list.append(random.choice(numbers))
    
#  change place of list using shuffle function 
random.shuffle(password_list)

# change list to string 
password = ''.join(password_list)

print(f"the Generated password is {password}")