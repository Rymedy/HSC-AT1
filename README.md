# HSC-AT1
was made for hsc school assignment

SDD AT1 - Documentation
How to Run:
Python Program
To run the program you must ensure you have python 3.5.0 or up installed on your computer. 

Once installed run the python program by opening terminal (command prompt on Windows) and directing to the location where the program is located. This can be done by running the command ‘cd [directory (eg. Desktop)]’, once done successfully you may now open the file by simply typing the full file name into the bash (e.g index.py), if on macOS you must use the python3 prefix (e.g python3 index.py). If you are opening python in the terminal for the first time you may be prompted asking what you want to open the file with. If this does open with Python. The program will then be executed and opened. 

OR

Once installed run the python program by simply right clicking on the file and opening with python. The program will then be executed and opened. 

JavaScript (GUI) Program
Open index.html by double clicking the program in the directory.

2. MazeBot (20 marks)
Format of User Input
You will be prompted by the program to enter the value of the first room the maze bot will start at. Once entered the program will then prompt you to enter the adjacent rooms, to finish entering the adjacent rooms simply enter ‘0’. It will then prompt you to enter a room similarly to the first room but note the maze bot will not start from this room. Then it will prompt you to enter the adjacent rooms to that room. This process will repeat until all of the rooms have been entered, once all rooms have been entered simply enter ‘0’ to finish and your final room will be displayed.

Algorithm (Pseudocode)
```
FUNCTION mazeBot(dictionary, currentRoom)
	// ‘alreadyBeenIn’ is a global variable with all the rooms with value ‘False’
	// at the beginning.
	// ‘dictionary’ is taken in as an argument from the dictionary ‘myDict’ that
	// is defined at the beginning of the program.
	// ‘currentRoom’ is taken in as an argument from the user input stored in
	// ‘firstRoom’.
	// The following uses linear search to find the biggest number in the
           // array.
	largestNum = 0
	// Makes the ‘currentRoom’ variable equal to boolean value ‘True’ inside
	// the ‘alreadyBeenIn’ dictionary.
	alreadyBeenIn[currentRoom] = True
	FOR num in dictionary[currentRoom]:
		// Finds the largest num in the Room.
		// Checks if the Room has been alreadyBeenIn and if the num is  
// larger than the largest current num.
		IF num > largestNum AND alreadyBeenIn[num] == False THEN
			// Makes largestNum equal to num as it checks through the 
// array for the largest number.
			largestNum = num
	// Checks if the largestNum variable is equal to 0 and if so returns the 
// current Room.
	IF largestNum == 0 THEN
		RETURN currentRoom

	// Returns the output of the mazeBot function when myDict and 
// largestNum variables are input from 'myDict' and 'firstRoom'.
	RETURN mazeBot(myDict, largestNum)
```
Test Data
NOTE: The user is prompted for user input including the first room and other rooms and all the adjacent rooms, this user input is stored in a dictionary as formatted below.
Test Case #1 (Original Case)
Input
NOTE: The first room entered is 50.
Room      Adjacent Rooms
Key                Array
{50: [37, 41, 42, 46, 48],
28: [29],
29: [28, 32, 34, 48],
30: [32],
31: [36],
32: [29, 30, 36, 46],
33: [43],
34: [29, 35, 42, 43],
35: [34],
36: [31, 32, 41, 43],
37: [41, 42, 43, 50],
41: [36, 37, 46, 50],
42: [37, 48, 34, 50],
43: [33, 34, 36, 37],
46: [32, 41, 48, 50],
48: [29, 42, 46, 50]}

Test Result #1 (Output)
30

Test Case #2 (Mock Case)
Input
NOTE: The first room entered is 5.
Room  Adjacent Rooms
Key  Array
{5: [2],
2: [5, 1, 6],
1: [2],
6: [2, 3, 7],
3: [6],
7: [6, 4, 10],
4: [7],
10: [7, 9, 11],
9: [10],
11: [10, 8, 15],
8: [11],
15: [11, 14, 13],
14: [15],
13: [15, 16, 18],
16: [13],
18: [13, 17],
17: [18]}

Test Result #2 (Output)
14

Test Case #3 (Mock Case)
Input
NOTE: The first room entered is 36.
Room  Adjacent Rooms
Key       Array
{36: [33, 35, 37, 34],
37: [36, 32, 34],
34: [36, 37],
35: [33, 36],
33: [32, 36, 35],
32: [33, 37]}

Test Result #3 (Output)
34

Test Case #4 (Single Room)
Input
NOTE: The first room entered is 1.
Room  Adjacent Rooms
Key  Array
{1: []}

Test Result #4 (Output)
1

Test Case #5 (Identical Rooms)
Input
NOTE: The first room entered is 1.
Room  Adjacent Rooms
Key  Array
{1: [1]}

Test Result #4 (Output)
Invalid inputted value. 

4. Annoying Nephew (20 marks)
Format of User Input
You will be prompted to add letters to the circle repeatedly. To finish entering letters to the circle simply enter ‘0’ (The amount of letters entered must be an even amount otherwise letter ‘D’ will not function properly as there will be no letter on the opposite side of the circle). You will then be prompted to enter the amount of moves. Once entered the result will be displayed (where the counter has landed).
Algorithm (Pseudocode)
```
// ‘moves’ is a variable that stores the value input from the user at the beginning.
// User input is appended to the ‘array’ for string values and is error checked to 
// ensure input is either A, B, C, D or E.
array = []
currentIndex = 0
// States the conditions in a for loop.
FOR move in range(moves):
	// A - Moves it clockwise 1 position.
	IF array[currentIndex] == 'A' THEN
		currentIndex += 1
	// B - Moves it clockwise 4 positions.
	ELSE IF array[currentIndex] == 'B' THEN
		currentIndex += 4
// C - Moves it clockwise 2 positions.
	ELSE IF array[currentIndex] == 'C' THEN
		currentIndex += 2
	// D - Moves it directly opposite its current position.
	ELSE IF array[currentIndex] == 'D' THEN
		currentIndex += array.length / 2)
	// E - Moves it anticlockwise 2 positions.
	ELSE IF array[currentIndex] == 'E' THEN
		currentIndex -= 2

// Ensures the index value does not go below index 0 or above index 11  // and brings the index back to it's appropriate index value from 0-11.
	IF currentIndex >= array.length THEN
		currentIndex -= len(array)
	ELSE IF currentIndex < 0 THEN
		currentIndex += array.length
```
Test Data
Test Case #1 (Original Case)
Input
Letters
[‘D’, ‘A’, ‘C’, ‘D’, ‘A’, ‘C’, ‘E’, ‘B’, ‘D’, ‘A’, ‘E’, ‘A’]
Amount of Moves
61
Test Result #1 (Output)
The counter has landed on the E lying in position number 7!

Test Case #2 (Mock Case)
Input
Letters
[‘A’, ‘B’, ‘C’, ‘D’, ‘E’, ‘A’]
Amount of Moves
1000

Test Result #2 (Output)
The counter has landed on the B lying in position number 2!

Test Case #3 (Mock Case)
Input
Letters
[‘A’, ‘E’, ‘C’, ‘D’, ‘B’, ‘B’, ‘E’, ‘A’]
Amount of Moves
68

Test Result #3 (Output)
The counter has landed on the A lying in position number 8!

Reference
https://stackoverflow.com/questions/22057610/uncaught-typeerror-cannot-read-property-value-of-null
https://stackoverflow.com/questions/351409/how-to-append-something-to-an-array
https://stackoverflow.com/questions/49881570/python-dictionaries-appending-arrays-to-a-dictionary-for-a-specific-key
https://www.w3schools.com/python/python_dictionaries_access.asp
https://www.w3schools.com/howto/howto_js_rangeslider.asp
https://www.w3schools.com/html/html5_canvas.asp
https://www.w3schools.com/python/ref_func_range.asp
https://www.w3schools.com/cssref/css_inherit.asp
https://stackoverflow.com/questions/24237557/using-css-how-do-i-move-a-div-to-the-left-of-the-centre-position
https://stackoverflow.com/questions/19886843/how-to-remove-outline-border-from-input-button
https://stackoverflow.com/questions/7129285/what-is-the-purpose-of-the-return-statement
https://stackoverflow.com/questions/54273844/link-slider-to-change-a-variable-real-time
https://stackoverflow.com/questions/36455350/im-struggling-on-functions-for-example-def-a-what-goes-in-the-brackets#:~:text=Arguments%2C%20parameters%2C%20or%20input%20variables,for%20use%20within%20that%20function.
https://stackoverflow.com/questions/73663/how-to-terminate-a-script
https://stackoverflow.com/questions/5424716/how-to-check-if-string-input-is-a-number
https://stackoverflow.com/questions/35817565/how-to-filter-array-when-object-key-value-is-in-array
https://stackoverflow.com/questions/40163454/how-do-i-change-the-font-family-of-a-button-element
