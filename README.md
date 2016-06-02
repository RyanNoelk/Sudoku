##This is a simple django sudoku web app. It contains:
- Python classes that generate, solve, and check any x by x (square) sudoku puzzle
- UsI using Bootstrap and jQuery

##Setting up the web app
- Before you can start the app, you willneed to create a `private_settings.py` file within `base/`. You will need you add a secet key as well as setting `DEBUG`.
- You may also wish to setup your own database. By default this uses SQLite3. The models are quite simple so it should run on most DBs compatble with django.
- To seed the database; run the migrations then run `python manage.py save_puzzles.py` to create random puzzles and add them to the DB.

##Generating puzzles
The generator will return an x by y list of lists of numbers, where 0 is an empty cell.
```
from common.generator import Generator

generate = Generator(9, 9)
for row in generate.generate():
    print row
```
Output of above:
```
[
    [0, 7, 8, 5, 6, 0, 1, 0, 0],
    [0, 2, 3, 0, 0, 0, 5, 7, 0],
    [0, 0, 0, 0, 0, 2, 6, 0, 0],
    [7, 0, 0, 0, 9, 1, 0, 5, 3],
    [0, 8, 0, 0, 4, 0, 0, 6, 0],
    [4, 3, 0, 6, 2, 0, 0, 0, 1],
    [0, 0, 6, 2, 0, 0, 0, 0, 0],
    [0, 4, 7, 0, 0, 0, 3, 8, 0],
    [0, 0, 1, 0, 3, 6, 7, 2, 0]
]
```


##Solving puzzles
The solver will return a list of all the possaible solutions to the puzzle. There are some examples of solving puzzles within `common/runner.py`.
```
from common.solver import Solver

raw_puzzle = [
    [0, 7, 8, 5, 6, 0, 1, 0, 0],
    [0, 2, 3, 0, 0, 0, 5, 7, 0],
    [0, 0, 0, 0, 0, 2, 6, 0, 0],
    [7, 0, 0, 0, 9, 1, 0, 5, 3],
    [0, 8, 0, 0, 4, 0, 0, 6, 0],
    [4, 3, 0, 6, 2, 0, 0, 0, 1],
    [0, 0, 6, 2, 0, 0, 0, 0, 0],
    [0, 4, 7, 0, 0, 0, 3, 8, 0],
    [0, 0, 1, 0, 3, 6, 7, 2, 0]
]
ss = Solver(raw_puzzle)
ss.solve_puzzle()
print(ss.solutions)
```

##Checking puzzles
The checker will return True or False. True if the Puzzle is correct and Flase otherwise. If `check_with_zeros=True`, The puzzle will also return true if the puzzle is still solvable even if there are 0s left in the puzzle. There are some examples of checking puzzles within `common/runner.py`.
```
from common.solver import Solver

raw_puzzle = [
    [0, 7, 8, 5, 6, 0, 1, 0, 0],
    [0, 2, 3, 0, 0, 0, 5, 7, 0],
    [0, 0, 0, 0, 0, 2, 6, 0, 0],
    [7, 0, 0, 0, 9, 1, 0, 5, 3],
    [0, 8, 0, 0, 4, 0, 0, 6, 0],
    [4, 3, 0, 6, 2, 0, 0, 0, 1],
    [0, 0, 6, 2, 0, 0, 0, 0, 0],
    [0, 4, 7, 0, 0, 0, 3, 8, 0],
    [0, 0, 1, 0, 3, 6, 7, 2, 0]
]
ss = Solver(raw_puzzle)
ss.solve_puzzle()
print(ss.solutions)
```



