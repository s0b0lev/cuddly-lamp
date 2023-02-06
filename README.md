# Side-Stacker game

This is essentially connect-four, but the pieces stack on either side of the board instead of bottom-up.
Two players see a board, which is a grid of 7 rows and 7 columns. They take turn adding pieces to a row, on one of the sides. The pieces stack on top of each other, and the game ends when there are no spaces left available, or when a player has four consecutive pieces on a diagonal, column, or row.

For example, the board might look like this:
```
0 [ _ _ _ _ _ _ _ ]
1 [ o x _ _ _ _ o ]
2 [ x _ _ _ _ _ x ]
3 [ x _ _ _ _ _ o ]
4 [ o _ _ _ _ _ _ ]
5 [ _ _ _ _ _ _ _ ]
6 [ _ _ _ _ _ _ _ ]
```

in this case, it is x’s turn. If x plays (2, R), the board will look like this:
```
0 [ _ _ _ _ _ _ _ ]
1 [ o x _ _ _ _ o ]
2 [ x _ _ _ _ x x ]
3 [ x _ _ _ _ _ o ]
4 [ o _ _ _ _ _ _ ]
5 [ _ _ _ _ _ _ _ ]
6 [ _ _ _ _ _ _ _ ]
```
