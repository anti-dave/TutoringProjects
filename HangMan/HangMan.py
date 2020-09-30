import random

class HangMan:
	def __init__(self, words):
		self.words = words
		self.guessesLeft = 5
		self.gameWord = ""
		self.guessCharacters = []

	def validateGuess(self, guessChoice):
		if len(guessChoice) > 1 or not guessChoice.isalpha():
			print("Not a single character guess! Guess again!")
			return 1

		if guessChoice in self.guessCharacters:
			print("You already guessed that!")
			return 1
		return 0

	def guess(self):
		print("Guess a single letter")
		guessChoice = input()
		return guessChoice

	def guessLoop(self):
		guessChoice = self.guess()
		while self.validateGuess(guessChoice):
			guessChoice = self.guess()
			
		if guessChoice in self.words:
			print('You got one!')
		else:
			print("Sorry, that's not right. Try again.")
			self.guessesLeft = self.guessesLeft - 1

		self.guessCharacters.append(guessChoice)

	def gameLoop(self):
		self.renderBanner()
		self.gameWord = self.words[random.randrange(len(self.words))]

		while self.guessesLeft >= 0:
			self.renderGallows()
			self.renderGuessingSpaces()
			self.guessLoop()

		return

	def renderGuessingSpaces(self):
		printStr = ' '
		for letter in self.gameWord:
			if letter in self.guessCharacters:
				printStr = printStr + letter + ' '
			else:
				printStr = printStr + '_ '

		print(printStr)

	def renderBanner(self):
			print("*************************")
			print("*********HANGMAN*********")
			print("*************************")
			print("")
			print("   ****************      ")
			print("   *              *      ")
			print("   *              *      ")
			print("   *              *      ")
			print("   *             *  *    ")
			print("   *             *  *    ")
			print("   *               *     ")
			print("   *               *     ")
			print("   *           ********* ")
			print("   *               *     ")
			print("   *               *     ")
			print("   *               *     ")
			print("   *              * *    ")
			print("   *             *   *   ")
			print("   *            *     *  ")
			print("   *                     ")
			print("   *                     ")
			print(" **********************  ")
			print(" **********************  ")
			print("\n")
			print("The Game begins")

	def renderGallows(self):
		if self.guessesLeft == 5:
			print("   ****************      ")
			print("   *              *      ")
			print("   *              *      ")
			print("   *              *      ")
			print("   *                     ")
			print("   *                     ")
			print("   *                     ")
			print("   *                     ")
			print("   *                     ")
			print("   *                     ")
			print("   *                     ")
			print("   *                     ")
			print("   *                     ")
			print("   *                     ")
			print("   *                     ")
			print("   *                     ")
			print("   *                     ")
			print(" **********************  ")
			print(" **********************  ")

		if self.guessesLeft == 4:
			print("   ****************      ")
			print("   *              *      ")
			print("   *              *      ")
			print("   *              *      ")
			print("   *             *  *    ")
			print("   *             *  *    ")
			print("   *                     ")
			print("   *                     ")
			print("   *                     ")
			print("   *                     ")
			print("   *                     ")
			print("   *                     ")
			print("   *                     ")
			print("   *                     ")
			print("   *                     ")
			print("   *                     ")
			print("   *                     ")
			print(" **********************  ")
			print(" **********************  ")

		if self.guessesLeft == 3:
			print("   ****************      ")
			print("   *              *      ")
			print("   *              *      ")
			print("   *              *      ")
			print("   *             *  *    ")
			print("   *             *  *    ")
			print("   *               *     ")
			print("   *               *     ")
			print("   *           *****     ")
			print("   *                     ")
			print("   *                     ")
			print("   *                     ")
			print("   *                     ")
			print("   *                     ")
			print("   *                     ")
			print("   *                     ")
			print("   *                     ")
			print(" **********************  ")
			print(" **********************  ")

		if self.guessesLeft == 2:
			print("   ****************      ")
			print("   *              *      ")
			print("   *              *      ")
			print("   *              *      ")
			print("   *             *  *    ")
			print("   *             *  *    ")
			print("   *               *     ")
			print("   *               *     ")
			print("   *           ********* ")
			print("   *                     ")
			print("   *                     ")
			print("   *                     ")
			print("   *                     ")
			print("   *                     ")
			print("   *                     ")
			print("   *                     ")
			print("   *                     ")
			print(" **********************  ")
			print(" **********************  ")

		if self.guessesLeft == 1:
			print("   ****************      ")
			print("   *              *      ")
			print("   *              *      ")
			print("   *              *      ")
			print("   *             *  *    ")
			print("   *             *  *    ")
			print("   *               *     ")
			print("   *               *     ")
			print("   *           ********* ")
			print("   *               *     ")
			print("   *               *     ")
			print("   *               *     ")
			print("   *              *      ")
			print("   *             *       ")
			print("   *            *        ")
			print("   *                     ")
			print("   *                     ")
			print(" **********************  ")
			print(" **********************  ")

		if self.guessesLeft == 0:
			print("*************************")
			print("********GAME OVER********")
			print("*************************")
			print("\n")
			print("   ****************      ")
			print("   *              *      ")
			print("   *              *      ")
			print("   *              *      ")
			print("   *             *  *    ")
			print("   *             *  *    ")
			print("   *               *     ")
			print("   *               *     ")
			print("   *           ********* ")
			print("   *               *     ")
			print("   *               *     ")
			print("   *               *     ")
			print("   *              * *    ")
			print("   *             *   *   ")
			print("   *            *     *  ")
			print("   *                     ")
			print("   *                     ")
			print(" **********************  ")
			print(" **********************  ")
			print("\n")
			print("Game Word was " + self.gameWord)