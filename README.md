# Tic Tac Toe AI (Internship Task 2)

A console based Tic Tac Toe game where you play against the computer.
The computer uses the Minimax algorithm, so it plays perfectly — it will
never lose, best you can do is force a draw.

## Features

- Play against an unbeatable AI (Minimax based)
- Simple text based board, no extra setup needed
- Correctly detects win, loss and draw
- Input validation — handles wrong numbers or already filled spots without
  crashing

## How to run

Make sure Python 3 is installed, then run:

python tic_tac_toe_ai.py


## How to play

- You play as `X`, computer plays as `O`
- Board positions are numbered 1 to 9 like this:

```
 1 | 2 | 3
 4 | 5 | 6
 7 | 8 | 9
```

- Enter a number from 1-9 when asked, to place your move there
- Game ends when someone gets 3 in a row (row, column or diagonal), or
  when the board fills up with no winner (draw)

## How the AI works (Minimax)

For every possible move, the AI imagines the human playing their best
response, then imagines its own best response to that, and keeps going
like this until the game ends. Doing this for every move lets it know
the outcome of each choice in advance, so it always picks the move that
leads to the best result for itself.

- AI winning = score of 1
- Human winning = score of -1
- Draw = score of 0

AI always picks the move with the highest score, human (in this
simulation) is assumed to always pick the move with the lowest score.
That's basically what minimax means - one side maximizing, other side
minimizing.


