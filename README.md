# Maze Solver with BFS

This project solves a maze using the `BFS` (`Breadth-First Search`) algorithm.

The program reads the maze from `input.txt`, searches for a path from the entrance `S` to the exit `E`, and writes the result to `output.txt`.

## Goal

The goal of the program is to:

- find the maze exit
- guarantee the shortest path in number of steps
- show a visual representation of the path found
- measure the execution time of the search

## Project Files

- `bfs.py`: main source code
- `input.txt`: input maze
- `output.txt`: generated result
- `README.md`: project documentation

## How It Works

The program:

1. reads the content of `input.txt`
2. counts the number of rows and columns in the maze
3. checks that both `S` and `E` exist
4. adds a border of `#` around the matrix to simplify boundary checks
5. runs BFS starting from `S`
6. when it finds `E`, reconstructs the shortest path
7. saves the result to `output.txt`

## Meaning of the Symbols

In the input file, the maze must use these characters:

- `#` = wall
- `.` = free space
- `S` = starting point
- `E` = exit

In the output file:

- `#` remains a wall
- blank space = free cell
- `S` = start
- `E` = exit
- `·` = correct path found by BFS

## `input.txt` Format

Each row of the maze must match one line of the file.

Each element must be separated by a space.

Example:

```text
# # # # #
# S . E #
# # # # #
```

Important rules:

- all rows must have the same number of columns
- there must be a space between symbols
- the maze must follow a consistent grid structure
- both `S` and `E` must be present

## How to Run the Program

Make sure Python is installed, then run:

```powershell
python bfs.py
```

At the end, the result will be written to `output.txt`.

## Example Output

If a path is found, `output.txt` will contain:

- the minimum number of steps
- the maze map with the highlighted path
- the execution time

Example:

```text
Uscita trovata con 140 passi
...
tempo impiegato = 0.0019
```

If the maze is invalid or has no solution, the program may write:

```text
Manca l'entrata
```

or:

```text
Manca l'uscita
```

or:

```text
Non c'e` nessuna uscita
```

## Why BFS

`Breadth-First Search` explores the maze level by level.

This means that the first time it reaches `E`, the path found is also the shortest one in terms of number of steps, assuming each move has a cost of 1.

## Code Structure

The file `bfs.py` contains these main functions:

- `contatore_r_c(f)`: counts the number of rows and columns in the maze
- `controllo(matrice)`: checks for the presence of `S` and `E`
- `allargo_matrice(matrice, linee, colonne)`: adds an outer wall border
- `trovo_entrata(matrice)`: finds the starting position of `S`
- `tempo()`: returns the current time

After these functions, the program:

- loads the maze into a matrix
- creates a support matrix to store distances
- uses a `deque` as the BFS queue
- reconstructs the final path starting from the exit

## Path Reconstruction Logic

The BFS stores in the support matrix the distance from the start for each visited cell.

When the exit is found:

- it takes the final cell
- it moves backward by looking for a neighboring cell with a distance smaller by 1
- in this way, it reconstructs the shortest path from the start to the exit

## Current Limitations

The program works correctly with the expected format, but there are some limitations:

- it does not explicitly check whether all rows have the same length
- it does not verify whether there is more than one `S` or more than one `E`
- it always reads from and writes to fixed file names: `input.txt` and `output.txt`
- it is designed for movement in 4 directions only: north, east, south, west

## Possible Improvements

Here are some ideas for improving it:

- add stricter input validation
- allow choosing input and output files from the command line
- print the result to the terminal as well
- support multiple mazes
- refactor the code into more modular functions or classes

## Conclusion

This project is a simple and practical example of how BFS can be applied to a maze.

It is a good example for understanding:

- matrix handling
- queues with `deque`
- shortest-path search
- path reconstruction
- file input and output management
