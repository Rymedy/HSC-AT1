import sys
print("NOTE: Amount of letters must be even otherwise letter 'D' will not function correctly.")
print("[Enter '0' at any time to finish adding letters]")
array = []
currentIndex = 0
letter = None

# Whilst the letter is not equal to 0, allows for user input and turns the user input into uppercase.
while letter != '0':
	lowercaseLetter = str(input("Add a letter: "))
	letter = lowercaseLetter.upper()
	# When letter is equal to 0 the loop is exited.
	if letter == '0':
		break

	# Error checks to ensure user input is equal to A, B, C, D or E and if not terminates the program.
	elif letter != 'A' \
	and letter != 'B' \
	and letter != 'C' \
	and letter != 'D' \
	and letter != 'E':
		sys.exit()

	# Appends the user input stored in letter to the array.
	elif letter != '0':
		array.append(str(letter))
		print(array)
	# Prints the string stored in the currentIndex of the array.
print("Your starting letter is " + array[currentIndex])
moves = int(input("How many moves? "))

# States the conditions in a for loop.
for move in range(moves):
	# A - Moves it clockwise 1 position.
	if array[currentIndex] == 'A':
		currentIndex += 1
	# B - Moves it clockwise 4 positions.
	elif array[currentIndex] == 'B':
		currentIndex += 4
	# C - Moves it clockwise 2 positions.
	elif array[currentIndex] == 'C':
		currentIndex += 2
	# D - Moves it directly opposite its current position.
	elif array[currentIndex] == 'D':
		currentIndex += int(len(array) / 2)
	# E - Moves it anticlockwise 2 positions.
	elif array[currentIndex] == 'E':
		currentIndex -= 2

	# Ensures the index value does not go below index 0 or above index 11 and brings the index back to 
	# it's appropriate index value from 0-11.
	if currentIndex >= len(array):
		currentIndex -= len(array)
	elif currentIndex < 0:
		currentIndex += len(array)

	# Prints the string stored in the currentIndex of the array.
print("The counter has landed on the " + array[currentIndex] + " lying in position number " + str(currentIndex + 1) + "!")