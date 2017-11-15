import random

secretWords = 'wrestle thinkable airport trashy low determined seal alert bone nappy tough change agonizing dinner unbiased rule tawdry dam busy subtract crowd warn history bird record enchanting snakes dock hideous clam soothe step memorise foregoing disapprove lying sister known sugar kiss plot twist earsplitting clumsy warlike responsible squeal girls naive request'

words = secretWords.split()

pictures = ['''

   -----
   |   |
       |
       |
       |
       |
 +++++++''', '''

   -----
   |   |
   0   |
       |
       |
       |
 +++++++''', '''

   -----
   |   |
   0   |
   |   |
       |
       |
 +++++++''', '''

   -----
   |   |
   0   |
  /|   |
       |
       |
 +++++++''', '''

   -----
   |   |
   0   |
  /|\  |
       |
       |
 +++++++''', '''

   -----
   |   |
   0   |
  /|\  |
  /    |
       |
 +++++++''', '''

   -----
   |   |
   0   |
  /|\  |
  / \  |
       |
 +++++++''']

def RandomWord(wordList):
 wordIndex = random.randint(0, len(wordList) - 1)
 return wordList[wordIndex]

def displayGame(pictures, missedLetters, correctLetters, secretWord):
 print(pictures[len(missedLetters)])
 print()

 print('Secret word:', end=' ')
 for letter in missedLetters:
	 print(letter, end=' ')
 print()

 blanks = '*' * len(secretWord)

 for i in range(len(secretWord)):
	 if secretWord[i] in correctLetters:
		 blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

 for letter in blanks:
	 print(letter, end=' ')
 print()

def userWord(alreadyGuessed):
 while True:
	 print('Enter a letter.')
	 userWord = input()
	 userWord = guess.lower()
	 if userWord not in 'abcdefghijklmnopqrstuvwxyz':
		 print('It is not a letter.')
	 elif len(userWord) != 1: 
		 print('You can enter only one letter. Try again')
	 elif userWord in alreadyGuessed:
		 print('You have already guessed that letter. Choose again.')
	 else:
		 return userWord

def newGame():
 print('Do you want to try one more time? Please enter yes or no')
 return input().lower().startswith('y')


print('Hangman Game')
missedLetters = ''
correctLetters = ''
secretWord = RandomWord(words)
gameIsDone = False

while True:
 displayGame(pictures, missedLetters, correctLetters, secretWord)

 guess = userWord(missedLetters + correctLetters)

 if guess in secretWord:
	 correctLetters = correctLetters + guess

	 foundAllLetters = True
	 for i in range(len(secretWord)):
		 if secretWord[i] not in correctLetters:
			 foundAllLetters = False
			 break
	 if foundAllLetters:
		 print('Winner! Secret word was "' + secretWord + '"')
		 gameIsDone = True
 else:
	 missedLetters = missedLetters + guess

	 if len(missedLetters) == len(pictures) - 1:
		 displayGame(pictures, missedLetters, correctLetters, secretWord)
		 print('Looser!')
		 gameIsDone = True

 if gameIsDone:
	 if newGame():
		 missedLetters = ''
		 correctLetters = ''
		 gameIsDone = False
		 secretWord = RandomWord(words)
	 else:
		 break# lits
