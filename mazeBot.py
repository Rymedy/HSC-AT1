import sys
myDict = {
	# 28: [29],
	# 29: [28, 32, 34, 48],
	# 30: [32],
	# 31: [36],
	# 32: [29, 30, 36, 46],
	# 33: [43],
	# 34: [29, 35, 42, 43],
	# 35: [34],
	# 36: [31, 32, 41, 43],
	# 37: [41, 42, 43, 50],
	# 41: [36, 37, 46, 50],
	# 42: [37, 48, 34, 50],
	# 43: [33, 34, 36, 37],
	# 46: [32, 41, 48, 50],
	# 48: [29, 42, 46, 50],
	# 50: [37, 41, 42, 46, 48]
}
# Defines 'alreadyBeenIn' dictionary (empty)
alreadyBeenIn = {}
tempArray = []
# Defines a new function 'mazeBot' with myDict input variable and currentRoom key input.
def mazeBot(dictionary, currentRoom):
	# The following uses linear search to find the biggest num in the array.
	# Finds the largest num in the Room.
	largestNum = 0
	alreadyBeenIn[currentRoom] = True
	for num in dictionary[currentRoom]:
		# Checks if the Room has been alreadyBeenIn and if the num is larger than the largest current numer.
		if num > largestNum and alreadyBeenIn[num] == False:
			# Makes largestNum equal to num as it checks through the array for the largest numer.
			largestNum = num
		if num == currentRoom:
			print("Invalid inputted value.")
			sys.exit()
	# Checks if the largestNum variable is equal to 0 and if so returns the current Room.
	if largestNum == 0:
		return currentRoom
	# Returns the output of the mazeBot function when myDict and largestNum variables are input from 'myDict' and 'firstRoom'.
	return mazeBot(myDict, largestNum)

print("NOTE: ALL STARTING Room DATA MUST COROLATE WITH CONNECTING Room DATA!")
# Define startingRoom as equal to nothing.
startingRoom = None

while startingRoom != 0:
	# Clears everything inside the 'tempArray' array.
	tempArray.clear()
	if startingRoom == None:
		# Prompts for user input and ensures the input is an integer.
		try:
			startingRoom = int(input("Enter the first room: "))
		except ValueError:
			print("That is not a value!")
			continue
		firstRoom = startingRoom
	else:
		# Prompts for user input and ensures the input is an integer.
		try:
			startingRoom = int(input("Enter a room: "))
		except ValueError:
			print("That is not a value!")
			continue
	if startingRoom == 0:
		break
	print("[Enter '0' to finish entering data]")
	connectingRoom = None
	while connectingRoom != 0:
		# Prompts for user input and ensures the input is an integer.
		try:
			connectingRoom = int(input("Enter an adjacent room: "))
		except ValueError:
			print("That is not a value!")
			continue
		print("[Enter '0' to end connecting rooms]")
		if connectingRoom != 0:
			tempArray.append(int(connectingRoom))
		print(tempArray)
	myDict[int(startingRoom)] = tempArray.copy()
	# print('firstRoom: ' + str(firstRoom))
# print(myDict)
# States all key's inside the myDict dictionary as NOT alreadyBeenIn in the 'alreadyBeenIn' dictionary.
for key in myDict:
	alreadyBeenIn[key] = False
# Calls and stores the output of the mazebot function when myDict dictionary 
# and firstRoom is the starting current Room.
finalRoom = mazeBot(myDict, int(firstRoom))
print("The MazeBot has finished at room:")
# Prints the final Room or output gathered from the function/algorithm.
print(finalRoom)