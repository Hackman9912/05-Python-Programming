"""
Task:
    Your task is to implement the Hangman game in Python.

Program Specifications:
    1) Output a brief description of the game of hangman and how to play
    2) Ask the user to enter the word or phrase that will be guessed (have a friend enter the phrase 
        for you if you want to be surprised)
    3) Output the appropriate number of dashes and spaces to represent the phrase (make sure it’s clear 
        how many letters are in each word and how many words there are)
    4) Continuously read guesses of a letter from the user and fill in the corresponding blanks if the 
        letter is in the word, otherwise report that the user has made an incorrect guess.
    5) Each turn you will display the phrase as dashes but with any already guessed letters filled in, 
        as well as which letters have been incorrectly guessed so far and how many guesses the user has remaining.
    6) Your program should allow the user to make a total of k=6 guesses.

Assignment Notes:
    If the letter has already been guessed, output a message to the player and ask for input again.
    If the guess entered is not an alphabetic letter, output a message and ask for input again.

    If the letter is present in the word to be guessed, fill in the blanks appropriately with this particular letter. 
    If the complete name has been guessed, the game is over  - player wins the game.  Output a message telling the 
    player they have won and quit the game.

    If the letter/digit is not present in the word to be guessed, give a message to the player indicating that the 
    guess is incorrect and remaining number of chances is one less. If remaining number of chances is 0 (zero), 
    the game is over  - player loses the game. Output a message that they have lost and what the correct word was.  Quit the game.

Bonus:
    You can do one or both of the following:

    1) Using a file:
    Instead of asking for user input for the word, make a word bank in a file named hangman_words.txt. 
    Read in the contents of the file and choose a word at random.

    2) Forever alone option:
    You enter the word (or it is randomly chosen from the word bank) and have the computer try to guess the letters.

    3) Add some more functionality: 
        - Persist user profiles with scores
        - Prompt for which user is playing
        - Ask if the user wants to play a set of games
        - Build a leader board
        
    Have fun, get creative, and demonstrate what you've come up with.
"""
import sys
import time
import random

hangman_dict = {1 : "word", 2 : "ceiling", 3 : "superb", 
                4 : "python", 5 : "computer", 6 : "light"
    }
correct_guess = []
incorrect_guess = []
y = ""
z = ""
turn = 1
complete = False
answer = []
board = []


def main():
    global hangman_dict, y, turn, complete, board, incorrect_guess, correct_guess
    titlescreen()
    how_to_play()
    selection = random.randint(1, len(hangman_dict))
    # print(selection)
    # print(hangman_dict[selection])
    word = hangman_dict[selection]
    make_board(selection, hangman_dict)
    while complete == False:
        if board == answer:
            complete = True
            print("You won!")
            print("The answer was ", word)
        elif len(incorrect_guess) > 5:
            print("You lost!")
            print("The answer was ", word)
            exit()
        else:
            print("Here is the board \n", "".join(board))
            guess = guessing()
            right_wrong(guess)
    print("Game Over")
def print_slow(txt):
    # for every letter in whatever text
    for letter in txt:
        # makes it print like typing
        sys.stdout.write(letter)
        # make it print right
        sys.stdout.flush()
        # give the user some time to read
        time.sleep(0.03)
def titlescreen():
    print_slow("  ######################################")
    print_slow("\n  #                                    #")
    print_slow("\n  #             Hang Man               #")
    print_slow("\n  #                                    #")
    print_slow("\n  ######################################")
def how_to_play():
    print_slow("\n \n             How to play                 ")
    print_slow(" \n The program will randomly select a word and \n you must guess the word letter by letter. You")
    print_slow("\n are allowed to have 6 mistakes before you lose!\n \n")
def make_board(selected, dictionary):
    global y, board, answer
    for x in dictionary[selected]:
        if x.isalpha() == True:
            answer.append(x)
    length = len(answer)
    for i in range(0, length):
        board.append('_ ')
    # print("Here is the answer", "".join(answer))
    print_slow("Get ready to go: \n")

def print_board(board):
    print("           Here is your board: \n           ", "".join(board), "\n")           
def guessing():
    selected = input(f"\n \nEnter your guess: ")
    if selected.isalpha() == True:
        print("keep going")
        return selected
    else:
        print("Enter a single letter a to z")
        guessing()
def right_wrong(guess):
    global hangman_dict, incorrect_guess, answer, board
    if guess in answer:
        index = answer.index(guess)
        board[index] = guess
    else:
        incorrect_guess.append(guess)

main()

