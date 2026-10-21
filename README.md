# Maze-Solver-with-Recursion
A recursive maze solving program that reads a puzzle from a text file and outputs the first valid path and all possible paths from Start to Goal. The project demonstrates backtracking, recursion, and structured output formatting for maze exploration.

This project implements a recursive maze solving algorithm capable of producing two types of solutions:

First Path Solver – Finds and prints the first valid path from Start to Goal using recursion and backtracking.

All Paths Solver – Extends the recursive approach to explore every possible valid path through the maze.

The maze is provided as a text file and loaded into a 2D character matrix. The solver marks successful paths with '+' and visited dead‑ends with 'X', then writes the results into output files (path1.txt and pathAll.txt) following the required formatting.

This project is designed for learning recursion, backtracking, file I/O, and matrix traversal.

## Purpose of the Project
To practice implementing recursive algorithms.

To understand backtracking and path exploration in grid‑based puzzles.

To generate structured output files showing the maze and the discovered paths.

To demonstrate clean Python project structure suitable for GitHub.

## How to Run the Python Code in VS Code
1. Open the Project Folder
Launch Visual Studio Code

Go to File → Open Folder

Select your maze solver project directory

2. Ensure Python Is Installed
In VS Code terminal:

`python --version`
If Python is not installed, install it from python.org.

3. Select Python Interpreter
Press Ctrl + Shift + P

Type: Python: Select Interpreter

Choose your Python installation

4. Run the Program
Open all_paths.py and run:

Code
`python all_paths.py`
or “the name of the code you want to execute”
or use the VS Code Run button in the top‑right corner.

5. Check Output Files
After running:

path1.txt will contain the first path

pathAll.txt will contain all paths
