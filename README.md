# Solution of Crosses-Crosses game
### About
The solution of crosses-crosses game through Sprague–Grundy theorem. The program represents all possible states of the game in the form of a graph and, by means of the Sprague–Grundy theorem, translates the game into an equivalent state of the nim game.
### Crosses-Crosses game
Crosses-Crosses game rules: You can't put two crosses side by side, a player who can't make a move loses
### game-AI.py
This script provides possible move variants for the entered state of the game
### game-traverser.py
This script displays the outcome of the game on a certain field. The first line displays numbers, if the number is positive, the field is winning for the player making the first move, if the number is 0, then the field is winning for the player who moves second. Also, these numbers show the number of stones in a pile (representing the batch as nim). Next, various possible move options are displayed on fields of different sizes
