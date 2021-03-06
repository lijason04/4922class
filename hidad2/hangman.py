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
    with open(WORDLIST_FILENAME, 'r') as inFile:
      return inFile.readline().split()

def choose_word(wordlist):
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()

def is_word_guessed(secret_word, letters_guessed):
  letters_guessed = set(letters_guessed)
  for c in secret_word:
    if c not in letters_guessed:
        return False
  return True

def get_guessed_word(secret_word, letters_guessed):
    toReturn = ''
    letters_guessed = set(letters_guessed)
    for c in secret_word:
      toReturn += c if c in letters_guessed else '_ '
    return toReturn



def get_available_letters(letters_guessed):
    letters_guessed = set(letters_guessed)
    letters = 'abcdefghijklmnopqrstuvwxyz'
    let2 = ''
    for c in letters:
      if c not in letters_guessed:
        let2 += c
    return let2

def actualHangman(secret_word, hasHint):
  lettersGuessed, vowels, guessCount, warnCount = [], set(['a', 'e', 'i', 'o', 'u']), 6, 3

  while (guessCount > 0):
    usable, old = get_available_letters(lettersGuessed), get_guessed_word(secret_word, lettersGuessed)
    print(f"The word has {len(secret_word)} letters \nAvailable letters: {usable}")
    keyInput = input("Please input a letter ")

    if(len(keyInput) > 1) or (keyInput not in usable):
      if (keyInput == '*' and hasHint == True):
        print(show_possible_matches(old))
      elif (warnCount > 0):
        warnCount -= 1
        print(f"invalid or repeated input {warnCount}. warns remain: {old}")
      else: 
        guessCount -= 1
      continue

    lettersGuessed.append(keyInput)
    new = get_guessed_word(secret_word, lettersGuessed)

    if (new == old):
      guessCount -= 2 if keyInput in vowels else 1
      print(f"{keyInput} is not in the word {old}. {str(guessCount)} guesses remaning")
      continue
    if is_word_guessed(secret_word, lettersGuessed) == True:
      print(f"The word is: {new} \nScore is {guessCount}")
      return
    print(f"{keyInput} is in the word: {new}")
  print(f"The word was: {secret_word}")

def hangman(secret_word):
  actualHangman(secret_word, False)
    




def match_with_gaps(my_word, other_word):
    my_word = my_word.replace(' ', '')
    if len(other_word) != len(my_word):
      return False
    for mc, oc in zip(my_word, other_word):
      if mc != '_' and mc != oc:
        return False
    return True 


def show_possible_matches(my_word):
  returnList = []
  for c in wordlist:
    if match_with_gaps(my_word, c) == True:
      returnList.append(c)
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
    
    secret_word = choose_word(wordlist)
    hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)

