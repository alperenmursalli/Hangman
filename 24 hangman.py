import random
import time
HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
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
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

words = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
         'coyote crow deer dog donkey duck eagle ferret fox frog goat '
         'goose hawk lion lizard llama mole monkey moose mouse mule newt '
         'otter owl panda parrot pigeon python rabbit ram rat raven '
         'rhino salmon seal shark sheep skunk sloth snake spider '
         'stork swan tiger toad trout turkey turtle weasel whale wolf '
         'wombat zebra aardvark').split()

wrong_guesses=[]

word=random.choice(words)

"""blanks=len(word)
print(word,blanks)"""
blanks=""
for a in range(1,len(word)+1):  #blanks="_"*len(word)
    blanks +="_"

list_letters=[]
for letter in word:
    list_letters.append(letter) #harfleri bir listede topluyoruz


x=0
while "_" in blanks:
    question=input(f"There is a hidden animal name! Type a letter to start: {blanks}\n").lower()
    if question in wrong_guesses or question in blanks:
        print("You made this guess!")
    elif question in list_letters:
        for i in range(0,len(word)):
           if question == word[i]: #what a guess'i iki kere yazdırmaz. "question" kelimede var mı diye bakar.
                blanks = blanks[:i] + question + blanks[i+1:] #[:i] i den önceki kısmı alır 
                print("What a Guess!")
        
    else:
        wrong_guesses.append(question)
        if x<=6:       
            print("Wrong guess.")
            time.sleep(0.5)
            print(HANGMANPICS[x]) 
            x += 1 
        else:
            print("YOU LOST")
time.sleep(0.5)
print(f"CONGRULATIONS! YOU WON!!! The word is {f}")