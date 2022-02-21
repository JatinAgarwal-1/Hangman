# Hey I am contributing, i Am Ameya!!
# i added this
import os
import requests

hang = ["""
H A N G M A N

   +---+
   |   |
       |
       |
       |
       |
=========""", """
H A N G M A N  

  +---+
  |   |
  O   |
      |
      |
      |
=========""", """
H A N G M A N 

  +---+
  |   |
  O   |
  |   |
      |
      |
=========""", """
Now Executioner Can See You ):

  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""", """
Play Care Fully  
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========""", """
About to get hanged 

  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========""", """
OO OOh! Game Over 
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
========="""]


def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


def greet(name):
    print(f"Welcome {name} to Hangman Game".center(100))


def getRandomWord():
    URL = 'https://random-word-api.herokuapp.com/word?number=1'

    r = requests.get(url=URL)

    word = r.json()[0]

    # print(word)

    return word


def displayBoard(hang, missedLetters, correctLetters, secretWord):
    print(hang[len(missedLetters)])
    print()

    print('Missed Letters:', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print("\n")

    blanks = '_' * len(secretWord)

    for i in range(len(secretWord)):  # replace blanks with correctly guessed letters
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

    for letter in blanks:  # show the secret word with spaces in between each letter
        print(letter, end=' ')
    print("\n")


def getGuess(alreadyGuessed):
    while True:
        guess = input('Guess a letter: ')
        guess = guess.lower()
        if len(guess) != 1:
            print('Please enter a single letter.')
        elif guess in alreadyGuessed:
            print('You have already guessed that letter. Choose again.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter a LETTER.')
        else:
            return guess


def playAgain():
    return input("\nDo you want to play again? ").lower().startswith('y')


def main():

    name = input("Please Enter Your Name :  ")

    clearConsole()

    greet(name)

    missedLetters = ''
    correctLetters = ''
    secretWord = getRandomWord()
    gameIsDone = False

    while True:
        displayBoard(hang, missedLetters, correctLetters, secretWord)

        guess = getGuess(missedLetters + correctLetters)

        if guess in secretWord:
            correctLetters = correctLetters + guess

            foundAllLetters = True
            for i in range(len(secretWord)):
                if secretWord[i] not in correctLetters:
                    foundAllLetters = False
                    break
            if foundAllLetters:
                print('\nYes! The secret word is "' +
                      secretWord + '"! You have won!')
                gameIsDone = True
        else:
            missedLetters = missedLetters + guess

            if len(missedLetters) == len(hang) - 1:
                clearConsole()
                displayBoard(hang, missedLetters, correctLetters, secretWord)
                print('You have been Hanged!\nAfter ' + str(len(missedLetters)) + ' missed guesses and ' +
                      str(len(correctLetters)) + ' correct guesses, the word was "' + secretWord + '"')
                gameIsDone = True

        if gameIsDone:
            if playAgain():
                missedLetters = ''
                correctLetters = ''
                gameIsDone = False
                secretWord = getRandomWord()
            else:
                break

        clearConsole()


if __name__ == '__main__':
    main()
