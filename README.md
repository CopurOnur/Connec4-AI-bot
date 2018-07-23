# Connect4_AI_Python

This is a Python 3 AI bot playing connect 4 game.

The strategy of the bot is inculded in ai_player.py file.

To run the code, first open all the files and run all of them. Finally,
run the run_cmd.py file and play the game.


Strategty Description

The algorithm has 2 steps
	Wining condition check
	Evaluation Function and decision tree


Wining condition check
	At each sate of the game board, check for if there is a wining condition

	If the algorithms finds a wining situation 
	(3 tokens in a row vertical, Horizontal, diagonal 1 or diagonal 2) 
	and if there is a possible move to complete the game

	Do not search for any other conditions on the decision tree. 


Evaluation Function and decision tree
	First assign points to each cell on the game board. 

	The numbers in the table indicate the number of four connected positions which include that space.

	the 3 in the upper left corner is for one each of horizontal, vertical
	and diagonal lines of four which can be made with it.

	the 4 beside it is for two horizontal (one including starting in the corner, 
	one starting on it, one vertical, and one diagonal)


		{{3, 4, 5, 7, 5, 4, 3}, // coefficients for board values
                {4, 6, 8, 10, 8, 6, 4},
                {5, 8, 11, 13, 11, 8, 5}, 
                {5, 8, 11, 13, 11, 8, 5},
                {4, 6, 8, 10, 8, 6, 4},
                {3, 4, 5, 7, 5, 4, 3}};

SCORING
	After Creating the Score Board, we can start scoring.
	Player 1 (Maximizing) starts with 138 points (total points on the score board divided by 2)
	Player 2 (Minimizing) starts with -138 points

EXAMPLE DECISION TREE SCORING

	Lets say Player 1 makes the first move with the 1 st column.
	Then Player 2 will get a penalty with the score of player 1’s move.
	So in this case the new score of player 2 would be -138 + 3 =-135

	After if Player 2 makes a move for the second column,
	then Player 1 will get a penalty of 4 
	and the new score of player 1 would be 138 – 4 =134 and so on...


By this way, we can form the decision tree and the AI will make moves to maximize the final score of the Player 1.





