import random

words_list = ["ant", "baboon", "badger", "bat", "bear", "beaver", "camel",
    "cat", "clam", "cobra", "cougar", "coyote", "crow", "deer",
    "dog", "donkey", "duck", "eagle", "ferret", "fox", "frog", "goat",
    "goose", "hawk", "lion", "lizard", "llama", "mole", "monkey", "moose",
    "mouse", "mule", "newt", "otter", "owl", "panda", "parrot", "pigeon", 
    "python", "rabbit", "ram", "rat", "raven","rhino", "salmon", "seal",
    "shark", "sheep", "skunk", "sloth", "snake", "spider", "stork", "swan",
    "tiger", "toad", "trout", "turkey", "turtle", "weasel", "whale", "wolf",
    "wombat", "zebra"]
misses_word_list = []
gallows_stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''

max_try = 6
try_numb = 0
# Task 1 - Choose the random word 
chosen_word = random.choice(words_list)

# Task 2 - Convert the word string to an array of characters
chosen_word_chars = list(chosen_word)

# Task 2.1 - Make an array of placeholders  
word_len = len(chosen_word)
placeholder_list = []
for i in range(0 , word_len) :
    placeholder_list += "_"

# Task exc - print logo
print(logo)

# Task 3 - Make the loop print all things again and again, let user the max  of 6 tries
while try_numb < max_try :
    # Task 4 - Print the gallows
    print(gallows_stages[max_try - try_numb])     

    # Task 5 - Print the placeholders by the word size
    print("".join(placeholder_list) + "\n")   

    # Task 6 - Print the misses      
    print(misses_word_list)
    print("\n")

    # Task 7 - Get the letter from the user
    guess_letter = input("Guess a letter: ").lower()     

    # Task 8 - Check the letter 
    guess_is_right = False 

    for i in range(0 , len(chosen_word_chars)) :
      # Task 8.1 - If it's correct, change the placeholder array
      if guess_letter == chosen_word_chars[i] :
          placeholder_list[i] = guess_letter
          guess_is_right = True

    # Task 8.2 - If it's wrong, change the misses letters array
    if guess_is_right == False :
      misses_word_list += guess_letter
      try_numb += 1
    #Task 9 - Check Win 
    is_win = True
    for char in placeholder_list : 
       if char == "_" :
          is_win = False
    if is_win :
       print("Word:\t" + chosen_word)
       print("Nice job, Well done!")
       exit(0)
    #Task 9.1 - Loose!
    if try_numb == 6 and is_win == False :
      print(gallows_stages[0])
      print("Rip!")
      print("\nThe word was:\t" + chosen_word + "\n")
      exit(0)
