# 6.0001 Problem Set 3
#
# The 6.0001 Word Game
# Created by: Kevin Luu <luuk> and Jenna Wiens <jwiens>
#
# Name          : <your name>
# Collaborators : <your collaborators>
# Time spent    : <total time>

import math
import random

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

WORDLIST_FILENAME = "words.txt"

def load_words():
    wordlist = []
    with open(WORDLIST_FILENAME, 'r') as inFile:
        for line in inFile:
            wordlist.append(line.strip().lower())
    return wordlist

def get_frequency_dict(sequence):
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq
	

# (end of helper code)
# -----------------------------------

#
# Problem #1: Scoring a word
#
def get_word_score(word, n):
    word = str.lower(word)
    summation, multiplyer = 0, 7 * len(word) - 3 * (n-len(word))
    for c in word:
        summation += SCRABBLE_LETTER_VALUES[c]
    if multiplyer > 1:
        return summation * multiplyer
    return summation
    

    

#
# Make sure you understand how this function works and what it does!
#
def display_hand(hand):
    for letter in hand.keys():
        for j in range(hand[letter]):
             print(letter, end=' ')      # print all on the same line

#
# Make sure you understand how this function works and what it does!
# You will need to modify this for Problem #4.
#
def deal_hand(n):

    n -= 1
    hand={}
    hand["*"] = 1
    num_vowels = int(math.ceil(n / 3))

    for i in range(num_vowels):
        x = random.choice(VOWELS)
        hand[x] = hand.get(x, 0) + 1
    
    for i in range(num_vowels, n):    
        x = random.choice(CONSONANTS)
        hand[x] = hand.get(x, 0) + 1
    
    return hand

#
# Problem #2: Update a hand by removing letters
#
def update_hand(hand, word):
    repHand = dict.copy(hand)
    for c in word:
        if (dict.get(repHand, c) == None or dict.get(repHand, c) == None) and c in VOWELS and dict.get(repHand, "*") != None and dict.get(repHand, "*") > 0:
            if dict.get(repHand, "*") == 1:
                dict.pop(repHand, "*")
            else:
                repHand['*'] = repHand['*'] -1
        elif dict.get(repHand, c) <= 1:
            dict.pop(repHand, c)
        elif dict.get(repHand, c) == None:
            continue
        else:
            repHand[c] = repHand[c] - 1
    return repHand
#
# Problem #3: Test word validity
#
def is_valid_word(word, hand, word_list):
    word_list = set(word_list)
    repliHand = dict.copy(hand)
    word = str.lower(word)
    vowels = "aeiou"
    
    for i in range(len(word)):
        c = word[i]
        if dict.get(repliHand, c) == None or dict.get(repliHand, c) < 1:
            print(1)
            if dict.get(repliHand, '*') > 0 and c in vowels:
                print(2)
                repliHand['*'] -= 1
                continue
            else:
                print(3)
                return False
        repliHand[c] -= 1
    if word in word_list:
        return True
    return False

# Problem #5: Playing a hand
#
def calculate_handlen(hand):
    summation = 0
    for c in hand:
        summation += hand[c]
    return summation


def play_hand(hand, word_list):

    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    
    * The user may input a word.

    * When any word is entered (valid or invalid), it uses up letters
      from the hand.

    * An invalid word is rejected, and a message is displayed asking
      the user to choose another word.

    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.

    * The sum of the word scores is displayed when the hand finishes.

    * The hand finishes when there are no more unused letters.
      The user can also finish playing the hand by inputing two 
      exclamation points (the string '!!') instead of a word.

      hand: dictionary (string -> int)
      word_list: list of lowercase strings
      returns: the total score for the hand
      
    """   
    score = 0
    while calculate_handlen(hand) > 0:   
        display_hand(hand) 
        word = input("put input ")
        if word == "!!":
            return score
        isValid = is_valid_word(word, hand, word_list)
        if isValid == True:
            val = get_word_score(word, calculate_handlen(hand))
            score += val
            print(f"Earned {val}")
        else:
            print("invalid word")
        hand = update_hand(hand, word)
    print("no more letters")
    return score


#
# Problem #6: Playing a game
# 


#
# procedure you will use to substitute a letter in a hand
#

def substitute_hand(hand, letter):
    """ 
    Allow the user to replace all copies of one letter in the hand (chosen by user)
    with a new letter chosen from the VOWELS and CONSONANTS at random. The new letter
    should be different from user's choice, and should not be any of the letters
    already in the hand.

    If user provide a letter not in the hand, the hand should be the same.

    Has no side effects: does not mutate hand.

    For example:
        substitute_hand({'h':1, 'e':1, 'l':2, 'o':1}, 'l')
    might return:
        {'h':1, 'e':1, 'o':1, 'x':2} -> if the new letter is 'x'
    The new letter should not be 'h', 'e', 'l', or 'o' since those letters were
    already in the hand.
    
    hand: dictionary (string -> int)
    letter: string
    returns: dictionary (string -> int)
    """
    replacedHand = dict.copy(hand)
    if len(hand) > 25:
        return hand
    abcd = "abcdefghijklmnopqrstuvwxyz"
    newChar = ''
    excludedChars = set([''])
    for c in replacedHand:
        excludedChars.add(c)
    while newChar in excludedChars:
        newChar = abcd[random.randint(0, 25)]
    replacedHand[newChar] = dict.get(hand, letter)
    dict.pop(replacedHand, letter)
    return replacedHand

def play_game(word_list):
    handNums = int(input("How many hands to play? "))
    totalScore = 0
    while handNums > 0:
        hand = deal_hand(HAND_SIZE)
        display_hand(hand)
        yOn = str.lower(input("substitute letter? "))
        if yOn == 'yes' or yOn == 'y':
            replaced = str.lower(input("input letter to substitute "))
            hand = substitute_hand(hand, replaced)
        num = play_hand(hand, word_list)
        print(num)
        totalScore += num
        handNums -= 1
    return totalScore
    
    
#
# Build data structures used for entire session and play game
# Do not remove the "if __name__ == '__main__':" line - this code is executed
# when the program is run directly, instead of through an import statement
#
if __name__ == '__main__':
    word_list = load_words()
    print(f"totalPoints: {play_game(word_list)}")
