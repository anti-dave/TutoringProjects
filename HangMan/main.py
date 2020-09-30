from HangMan import HangMan

if __name__ == "__main__":

	words = open('words')
	dictionairy = []

	try:
	    for word in words:
	    	dictionairy.append(word)

	finally:
	    words.close()

	game = HangMan(dictionairy)
	game.gameLoop()