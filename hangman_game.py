import random 
# print a Heading 
print('''
      
 _                                              
| |                                             
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __                      __ _  __ _ _ __ ___   ___  ___ 
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \\                    / _` |/ _` | '_ ` _ \ / _ \/ __|
| | | | (_| | | | | (_| | | | | | | (_| | | | |                  | (_| | (_| | | | | | |  __/\__ \\
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|                   \__, |\__,_|_| |_| |_|\___||___/
                    __/ |                                          __/ |          
                   |___/                                          |___/  
''')


word_list = ['abruptly','absurd','abyss','affix','askew', 'avenue', 'awkward', 'axiom', 'azure', 'bagpipes', 'bandwagon', 'banjo', 'bayou', 'beekeeper', 'bikini', 
'blitz', 'blizzard', 'boggle', 'bookworm', 'boxcar', 'boxful', 'buckaroo', 'buffalo','buffoon','buxom', 'buzzard','buzzing', 'buzzwords','caliph', 'cobweb', 'cockiness', 
'croquet','crypt', 'curacao','cycle', 'daiquiri','dirndl', 'disavow', 'dizzying', 'duplex', 'dwarves', 'embezzle','equip', 'espionage','euouae', 'exodus', 'faking', 
'fishhook','fixable', 'fjord', 'flapjack', 'flopping','fluffiness', 'flyby', 'foxglove', 'frazzled','frizzled','fuchsia', 'funny', 'gabby', 'galaxy','galvanize', 'gazebo','giaour', 
'gizmo', 'glowworm', 'glyph', 'gnarly', 'gnostic','gossip', 'grogginess', 'haiku', 'haphazard', 'hyphen', 'iatrogenic','icebox', 'injury', 'ivory', 'ivy', 'jackpot','jaundice', 
'jawbreaker','jaywalk', 'jazziest', 'jazzy', 'jelly', 'jigsaw', 'jinx', 'jiujitsu', 'jockey','jogging', 'joking','jovial', 'joyful','juicy', 'jukebox','jumbo', 'kayak', 'kazoo', 
'keyhole','khaki','kilobyte','kiosk', 'kitsch', 'kiwifruit', 'klutz', 'knapsack', 'larynx','lengths', 'lucky', 'luxury', 'lymph', 'marquis', 'matrix','megahertz', 'microwave',
'mnemonic', 'mystify', 'naphtha', 'nightclub','nowadays', 'numbskull','nymph', 'onyx', 'ovary', 'oxidize','oxygen', 'pajama', 'peekaboo', 'phlegm', 'pixel', 'pizazz', 'pneumonia',
'polka', 'pshaw', 'psyche','puppy', 'puzzling','quartz','queue', 'quips', 'quixotic', 'quiz', 'quizzes', 'quorum','razzmatazz','rhubarb','rhythm', 'rickshaw','schnapps', 
'scratch', 'shiv', 'snazzy', 'sphinx', 'spritz', 'squawk', 'staff', 'strength', 'strengths','stretch', 'stronghold', 'stymied', 'subway', 'swivel', 'syndrome','thriftless', 'thumbscrew',
'topaz', 'transcript','transgress', 'transplant','triphthong', 'twelfth', 'twelfths', 'unknown', 'unworthy', 'unzip', 'uptown', 'vaporize','vixen', 'vodka', 'voodoo', 
'vortex','voyeurism', 'walkway','waltz', 'wave', 'wavy', 'waxy', 'wellspring','wheezy','whiskey', 'whizzing', 'whomever','wimpy', 'witchcraft','wizard', 
'woozy', 'wristwatch','wyvern', 'xylophone', 'yachtsman','yippee', 'yoked', 'youthful', 'yummy','zephyr', 'zigzag', 'zigzagging','zilch', 'zipper', 'zodiac', 'zombie', 
]

gess_letter =random.choice(word_list)

blank_list = [ '_' for i in range(len(gess_letter))]   # add Blank list 
#add ascii art of hangman 
Hangman_stage =  [
'''     ___________.._______
| .__________))______|
| | / /      ||
| |/ /       ||
| | /        ||.-''.
| |/         |/  _  \\
| |          ||  `/,|
| |          (\\`_.'
| |         .-`--'.
| |        /Y . . Y\\
| |       // |   | \\\\
| |      //  | . |  \\\\
| |     ')   |   |   (`
| |          ||'||
| |          || ||
| |          || ||
| |          || ||
| |         / | | \\
""""""""""|_`-' `-' |"""|
|"|"""""""\ \       '"|"|
| |        \ \        | |
: :         \ \       : :  
. .          `'       . .
'''
,

''' ___________.._______
| .__________))______|
| | / /      ||
| |/ /       ||
| | /        ||.-''.
| |/         |/  _  \\
| |          ||  `/,|
| |          (\\`_.'
| |         .-`--'.
| |        /Y . . Y\\
| |       // |   | \\\\
| |      //  | . |  \\\\
| |     ')   |   |   (`
| |          ||'
| |          || 
| |          || 
| |          || 
| |         / | 
""""""""""|_`-'     |"""|
|"|"""""""\ \       '"|"|
| |        \ \        | |
: :         \ \       : :  
. .          `'       . .     '''
,

''' ___________.._______
| .__________))______|
| | / /      ||
| |/ /       ||
| | /        ||.-''.
| |/         |/  _  \\
| |          ||  `/,|
| |          (\\`_.'
| |         .-`--'.
| |        /Y . . Y\\
| |       // |   | \\\\
| |      //  | . |  \\\\
| |     ')   |   |   (`
| |          
| |           
| |           
| |                   
""""""""""|_        |"""|
|"|"""""""\ \       '"|"|
| |        \ \        | |
: :         \ \       : :  
. .          `'       . .     '''
,

''' ___________.._______
| .__________))______|
| | / /      ||
| |/ /       ||
| | /        ||.-''.
| |/         |/  _  \\
| |          ||  `/,|
| |          (\\`_.'
| |         .-`--'.
| |        /Y . . Y
| |       // |   | 
| |      //  | . | 
| |     ')   |   | 
| |          
| |           
| |           
| |                   
""""""""""|_        |"""|
|"|"""""""\ \       '"|"|
| |        \ \        | |
: :         \ \       : :  
. .          `'       . .     '''

,

''' ___________.._______
| .__________))______|
| | / /      ||
| |/ /       ||
| | /        ||.-''.
| |/         |/  _  \\
| |          ||  `/,|
| |          (\\`_.'
| |         .-`--'.
| |         Y . . Y
| |          |   | 
| |          | . | 
| |          |   | 
| |          
| |           
| |           
| |                   
""""""""""|_        |"""|
|"|"""""""\ \       '"|"|
| |        \ \        | |
: :         \ \       : :  
. .          `'       . .     '''

,

''' ___________.._______
| .__________))______|
| | / /      ||
| |/ /       ||
| | /        ||.-''.
| |/         |/  _  \\
| |          ||  `/,|
| |          (\\`_.'
| |         
| |         
| |         
| |          
| |          
| |          
| |           
| |           
| |                   
""""""""""|_        |"""|
|"|"""""""\ \       '"|"|
| |        \ \        | |
: :         \ \       : :  
. .          `'       . .     '''

]

life  = 5 
is_check = False
# while i != 0  and '_' in blank_list: 
    
while life  >=  0 and not is_check :
    choice_letter = input("\nEnter the Gess letter ")  # input choice a letter 
    is_change = False
    
    if choice_letter in blank_list :
        print("\nYou already enter this letter ")
    for postion  in range(len(gess_letter)):
        if gess_letter[postion] ==  choice_letter:
            blank_list[postion] =  choice_letter
            is_change = True

    if is_change == False :
        print(Hangman_stage[life ])  # if inpuit word false 1 life is destroy 
        life -=1 
    
    if "_" not in blank_list:
        is_check= True
    

    print(blank_list)


if life  == -1 :
    print(
          '''
                                  _                                      
                                 | |                                     
     _   _  ___   _   _          | | ___    __    ___
    | | | |/ _ \\ | | | |         | |/ _ \\ / __| / __|
    | |_| | (_) || |_| |         | | (_) |\__ \\ \\__ \\  
     \__, |\___/  \__,/          |_|\___/ |___/ |___/          
      __/ |      
     |___/      '''
          )
else :
    print(''' 
                                            _                 
                                           (_)           
     _   _  ___   _   _            __      ___ _ __  
    | | | |/ _ \\ | | | |           \ \ /\ / / | '_ \\
    | |_| | (_) || |_| |            \ V  V /| | | | |
     \__, |\___/  \__,/              \_/\_/ |_|_| |_|
      __/ |  
     |___/ 
          ''')
    print(" \n The Letter is ", ''.join(blank_list))