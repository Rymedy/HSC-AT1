// Defines a series of variables to be used throughout the program.
let array = [];
let currentIndex = 0;
let number = null;
var canvas = document.getElementById('myCanvas');
var ctx = canvas.getContext('2d');
var centerX = canvas.width / 2;
var centerY = canvas.height / 2;
var radius = 250;

// Defines an 'appendLetter' function
function appendLetter() {
	var lowercaseLetter = document.getElementById('letter').value;
	var letter = lowercaseLetter.toUpperCase();
	document.getElementById('letter').value='';
	array.push(letter);
	console.log(array);
	// Clears the canvas
	ctx.clearRect(0, 0, canvas.width, canvas.height)
	// Creates a for loop and repeats for the size of the array
	for (i = 0; i < array.length; i++) {
		// Defines angle variable and makes it equal to the number of times the loop has repeated * 360 / the size of the array.
		let angle = i * (2 * Math.PI) / array.length;
		// Defines x and y coordinates using the radius, angle, cos and sin.
		let x = centerX + (radius + 30) * Math.cos(angle) - 10;
		let y = centerY + (radius + 30) * Math.sin(angle) + 10;
		// Makes the text object and displays it at the x and y coordinates.
		ctx.fillText(array[i], x, y);
		console.log(x, y);
		// Draws the circle on the canvas
		drawCircle()
		// console.log(i);
	}
}

// Defines a 'finalResult' function.
function finalResult() {
	// Defines variable moves and make it equal to the value of the input in the HTML with the id 'moves'.
	var moves = document.getElementById('moves').value;
	// Creates a for loop that repeats for the amount of moves.
	for (i = 0; i < moves; i++) {
		// A - Moves it clockwise 1 position.
		if (array[currentIndex] == 'A') {
			currentIndex += 1;
		}
		// B - Moves it clockwise 4 positions.
		else if (array[currentIndex] == 'B') {
			currentIndex += 4;
		}
		// C - Moves it clockwise 2 positions.
		else if (array[currentIndex] == 'C') {
			currentIndex += 2;
		}
		// D - Moves it directly opposite its current position.
		else if (array[currentIndex] == 'D') {
			currentIndex += array.length / 2;
		}
		// E - Moves it anticlockwise 2 positions.
		else if (array[currentIndex] == 'E') {
			currentIndex -= 2;
		}

		// Ensures the index value does not go below index 0 or above index 11 and brings the index back to 
		// it's appropriate index value from 0-11.
		if (currentIndex >= array.length) {
			currentIndex -= array.length;
		}
		else if (currentIndex < 0) {
			currentIndex += array.length;
		}
	// Once i has repeated for the amount of moves print the final letter and position of the letter to the user.
	if (i == moves - 1) {
	console.log(array[currentIndex]);
	ctx.fillText("The counter has landed on letter " + array[currentIndex] + " in position " + (currentIndex + 1) + "!", 50, 110);
	ctx.fillText("<=", 1050, 410);
	}
	}
}
// Defines a function that draws a circle onto the canvas.
function drawCircle() {
	ctx.beginPath();
	ctx.arc(centerX, centerY, radius, 0, 2 * Math.PI, false);
	ctx.fillStyle = 'green';
	ctx.fill();
	ctx.lineWidth = 5;
	ctx.strokeStyle = '//003300';
	ctx.stroke();
	ctx.font = "30px Arial";
	ctx.fillStyle = 'black';
}
// Calls the drawCircle() function
drawCircle()


