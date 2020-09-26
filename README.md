# Tic-Tac-Toe-with-Monte-Carlo-Tree-Search
A Tic-Tac-Toe playing program where a human can play against the computer, and the computer makes all its moves using random playouts as described below.

The program does not use any information about Tic-Tac-Toe beyond the essential rules of how to play it, how to determine legal moves, and how to recognize if the game is a win, loss, or draw.

The program works as follows:
- When it’s the computers turn to make a move on a board, it will make a list of all legal moves. Then for each of the moves it does some number of random playouts. A random playout is when the computer simulates playing the game until it is over. 
- During a random playout, the computer makes random moves for each player until a win, loss, or draw is reached. When a playout is done, the result (win, loss, or draw) is recorded, and then some more random playouts are done. 
- After random playouts are done for all legal moves, it choses the move that resulted in the greatest number of wins (or least number of losses, or most number of wins + draws, etc.).

The program generates enough random playouts so that it never loses against a smart player.
