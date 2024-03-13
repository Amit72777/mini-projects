import random
rock = '''
                __________               
         ___.--"          "\'.        
  ------f"               // \\\        
        |                    |||      
        |                    |||     
    ----L_-----.             .|'   
                "\   -<_____///    
                  \___)     -"     
        '''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
user = int (input("Enter the number , for 0 is rock , 1 for paper and 2 for scissors "))
computer = random.randint(0,2)

# print a pattern 

if user >=0 and user <=2 :
    if user == 0 : user = rock
    elif user == 2 : user = scissors
    else :  user = paper
    
    print ( "\n  You enter \n ",user)

    if computer >=0 and computer <=2 :
        print(f"\n Computer choice { computer}\n ")
        if computer == 0 : computer = rock
        elif computer == 2 : computer = scissors
        else :  computer = paper
        print ("\n Computer Enter \n ",computer)

# condtion for who win 
if user == rock and computer == scissors:
    print("well done !! , You are win ")
elif user == scissors and computer == rock :
    print("Computer  is win ")
elif user == scissors and computer == paper:
    print("well done !! , You are win ")
elif user == paper and computer == scissors:
    print(" you Lose !!, Computer  are win ")
elif user == rock  and computer == paper:
    print("You Lose  !! , Computer are Win ")
elif user == paper and computer == rock:
    print("YOu Win !!, You   are win ")
elif user == paper and computer == paper :
    print(" Draw !!  ")
elif user == rock and computer == rock :  
    print(" Draw !!  ")
elif user == scissors and computer == scissors: 
    print(" Draw !!  ")

else :
    print("Please you enter a valit number ")

