import random 

print(
    '''  ________                          ________                       
 /  _____/  ____   ______ ______   /  _____/_____    _____   ____  
/   \  ____/ __ \ /  ___//  ___/  /   \  ___\__  \  /     \_/ __ \ 
\    \_\  \  ___/ \___ \ \___ \   \    \_\  \/ __ \|  Y Y  \  ___/ 
 \______  /\___  >____  >____  >   \______  (____  /__|_|  /\___  >
        \/     \/     \/     \/           \/     \/      \/     \/ '''
)
print("Wellcome to the Gessing game ")
win = '''
                                                                                                                            
YYYYYYY       YYYYYYY                                     WWWWWWWW                           WWWWWWWW   iiii                   
Y:::::Y       Y:::::Y                                     W::::::W                           W::::::W  i::::i                  
Y:::::Y       Y:::::Y                                     W::::::W                           W::::::W   iiii                   
Y::::::Y     Y::::::Y                                     W::::::W                           W::::::W                        
YYY:::::Y   Y:::::YYYooooooooooo   uuuuuu    uuuuuu        W:::::W           WWWWW           W:::::W  iiiiiii nnnn  nnnnnnnn    
   Y:::::Y Y:::::Y oo:::::::::::oo u::::u    u::::u         W:::::W         W:::::W         W:::::W   i:::::i n:::nn::::::::nn  
    Y:::::Y:::::Y o:::::::::::::::ou::::u    u::::u          W:::::W       W:::::::W       W:::::W     i::::i n::::::::::::::nn 
     Y:::::::::Y  o:::::ooooo:::::ou::::u    u::::u           W:::::W     W:::::::::W     W:::::W      i::::i nn:::::::::::::::n
      Y:::::::Y   o::::o     o::::ou::::u    u::::u            W:::::W   W:::::W:::::W   W:::::W       i::::i   n:::::nnnn:::::n
       Y:::::Y    o::::o     o::::ou::::u    u::::u             W:::::W W:::::W W:::::W W:::::W        i::::i   n::::n    n::::n
       Y:::::Y    o::::o     o::::ou::::u    u::::u              W:::::W:::::W   W:::::W:::::W         i::::i   n::::n    n::::n
       Y:::::Y    o::::o     o::::ou:::::uuuu:::::u               W:::::::::W     W:::::::::W          i::::i   n::::n    n::::n
       Y:::::Y    o:::::ooooo:::::ou:::::::::::::::uu              W:::::::W       W:::::::W          i::::::i  n::::n    n::::n
    YYYY:::::YYYY o:::::::::::::::o u:::::::::::::::u               W:::::W         W:::::W           i::::::i  n::::n    n::::n
    Y:::::::::::Y  oo:::::::::::oo   uu::::::::uu:::u                W:::W           W:::W            i::::::i  n::::n    n::::n
    YYYYYYYYYYYYY    ooooooooooo       uuuuuuuu  uuuu                 WWW             WWW             iiiiiiii  nnnnnn    nnnnnn
                                                                                                                             
                                                                                                                             '''
Loss = '''                                                                                                                                    
YYYYYYY       YYYYYYY                                     LLLLLLLLLLL                                                                
Y:::::Y       Y:::::Y                                     L:::::::::L                                                                
Y:::::Y       Y:::::Y                                     L:::::::::L                                                                
Y::::::Y     Y::::::Y                                     LL:::::::LL                                                                
YYY:::::Y   Y:::::YYYooooooooooo   uuuuuu    uuuuuu         L:::::L                  ooooooooooo       ssssssssss       ssssssssss   
   Y:::::Y Y:::::Y oo:::::::::::oo u::::u    u::::u         L:::::L                oo:::::::::::oo   ss::::::::::s    ss::::::::::s  
    Y:::::Y:::::Y o:::::::::::::::ou::::u    u::::u         L:::::L               o:::::::::::::::oss:::::::::::::s ss:::::::::::::s 
     Y:::::::::Y  o:::::ooooo:::::ou::::u    u::::u         L:::::L               o:::::ooooo:::::os::::::ssss:::::ss::::::ssss:::::s
      Y:::::::Y   o::::o     o::::ou::::u    u::::u         L:::::L               o::::o     o::::o s:::::s  ssssss  s:::::s  ssssss 
       Y:::::Y    o::::o     o::::ou::::u    u::::u         L:::::L               o::::o     o::::o   s::::::s         s::::::s      
       Y:::::Y    o::::o     o::::ou::::u    u::::u         L:::::L               o::::o     o::::o      s::::::s         s::::::s   
       Y:::::Y    o::::o     o::::ou:::::uuuu:::::u         L:::::L         LLLLLLo::::o     o::::ossssss   s:::::s ssssss   s:::::s 
       Y:::::Y    o:::::ooooo:::::ou:::::::::::::::uu     LL:::::::LLLLLLLLL:::::Lo:::::ooooo:::::os:::::ssss::::::ss:::::ssss::::::s
    YYYY:::::YYYY o:::::::::::::::o u:::::::::::::::u     L::::::::::::::::::::::Lo:::::::::::::::os::::::::::::::s s::::::::::::::s 
    Y:::::::::::Y  oo:::::::::::oo   uu::::::::uu:::u     L::::::::::::::::::::::L oo:::::::::::oo  s:::::::::::ss   s:::::::::::ss  
    YYYYYYYYYYYYY    ooooooooooo       uuuuuuuu  uuuu     LLLLLLLLLLLLLLLLLLLLLLLL   ooooooooooo     sssssssssss      sssssssssss    
                                                                                                                                     
'''
game_over = '''
 _______  _______  _______  _______    _______           _______  _______ 
(  ____ \(  ___  )(       )(  ____ \  (  ___  )|\     /|(  ____ \(  ____ )
| (    \/| (   ) || () () || (    \/  | (   ) || )   ( || (    \/| (    )|
| |      | (___) || || || || (__      | |   | || |   | || (__    | (____)|
| | ____ |  ___  || |(_)| ||  __)     | |   | |( (   ) )|  __)   |     __)
| | \_  )| (   ) || |   | || (        | |   | | \ \_/ / | (      | (\ (   
| (___) || )   ( || )   ( || (____/\  | (___) |  \   /  | (____/\| ) \ \__
(_______)|/     \||/     \|(_______/  (_______)   \_/   (_______/|/   \__/
                                                                            '''
def calculate_gess(gess_number,answer ):
    """ take a input gess_number or user_choce and return the result"""
    if gess_number == answer :
        print(f"You got it ! The answer was {answer}")
        return  "You win"
    elif gess_number < answer:
        return "Too high"
    else :
        return "Too low"

def gess_game():
    ''' Gessing game main functionallity '''
    game_level = input("Type your game level : 'easy' and 'hard':\n").lower()
    attemp = 10

    if game_level == "hard":
        attemp = 5 
    
    # generator a random number 
    gess_number = random.randint(1,100)

    while attemp :
        print(f"You have {attemp} remaining to gess the number")
        user_choice = int(input("Enter a number between 1 to 100:\n"))
        result = calculate_gess(gess_number, user_choice)
        if result == 'You win':
            print(win)
            return 
        print(result)
        attemp -=1 
    print(game_over)
    print(Loss)
    


# take input tho game play or not 
if input("Do Want to play a Gess Number game'y' or 'n':\n") == 'y':
    gess_game()
    
    while True :
        """this block use to run a code again and again """
        if input("Do you want to play again : Type 'y' otherwise 'n' for exit :") == 'y':
            gess_game()
        else :
            break 

print("Thank You \nHave a good day")