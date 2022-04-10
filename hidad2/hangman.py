# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import numbers
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist
def choose_word(wordlist):
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
  secret_word = str.lower(secret_word)
  counter = 0
  for i in range(len(secret_word)):
    if secret_word[i] in letters_guessed:
      counter+=1
  if counter == len(secret_word):
    return True
  return False



def get_guessed_word(secret_word, letters_guessed):
    toReturn = ''
    secret_word = str.lower(secret_word)
    for i in range(len(secret_word)):
        if secret_word[i] in letters_guessed:
            toReturn += secret_word[i] 
        else:
          toReturn += '_ '

    return toReturn



def get_available_letters(letters_guessed):
    letters = "abcdefghiklmnopqrstuvwxyz"
    let2 = ''
    for i in range(len(letters)):
      if str.lower(letters[i]) not in letters_guessed:
        let2 += letters[i]
    return let2

def actualHangman(secret_word, hasHint):
  lettersGuessed = []
  vowels = "aeiou"
  guessCount = 6
  warnCount = 3
  while (guessCount > 0):
    usable = get_available_letters(lettersGuessed)
    old = get_guessed_word(secret_word, lettersGuessed)
    print("The word has " + str(len(secret_word)) + " letters")
    print("Available letters: " + usable)
    keyInput = input("Please input a letter ")
    if(len(keyInput) > 1) or (keyInput not in usable):
      if (keyInput == '*' and hasHint == True):
        print(show_possible_matches(old))
        continue
      if (warnCount > 0):
        warnCount -= 1
        print("invalid or repeated input, " + str(warnCount) + "warns remain. " + old)
        continue
      else: 
        guessCount -= 1
        continue

    lettersGuessed.append(keyInput)
    new = get_guessed_word(secret_word, lettersGuessed)
    if (new == old):
      if keyInput in vowels:
        guessCount -= 2
        print("vowel" + keyInput + " is not in the word" + old + ". " + str(guessCount) + " guesses remaning")
      
        continue
      else:
        guessCount -= 1
        print(keyInput + " is not in the word" + old + ". " + str(guessCount) + " guesses remaning")
        continue
    if is_word_guessed(secret_word, lettersGuessed) == True:
      print("The word is: " + new)
      print("Score is " + str(guessCount))
      return
    print(keyInput + " is in the word: " + new)
  print("The word was: " + secret_word)

def hangman(secret_word):
  actualHangman(secret_word, False)
    




def match_with_gaps(my_word, other_word):
    my_word = my_word.replace(' ', '')
    if len(other_word) != len(my_word):
      return False
    for i in range(len(my_word)):
      if my_word[i] != '_' and my_word[i] != other_word[i]:
        return False
    return True 


def show_possible_matches(my_word):
  returnList = []
  for i in range(len(wordlist)):
    if match_with_gaps(my_word, wordlist[i]) == True:
      returnList.append(wordlist[i])
  return returnList



def hangman_with_hints(secret_word):
   actualHangman(secret_word, True)



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
   # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
 ##   secret_word = choose_word(wordlist)
 ##   hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)

