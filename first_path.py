import copy

# To read the maze from a text file
def read_maze(filename):
    with open(filename, "r") as f:
        # Strips whitespace/newlines and excludes empty lines
        return [list(line.strip()) for line in f if line.strip()]

def find_start(maze):
    for y in range(len(maze)):
        for x in range(len(maze[0])):
            if maze[y][x] == 'S':
                return x, y
    raise ValueError("Start 'S' not found in maze")

# The recursive function
def find_first_path(maze, x, y, visited):
    rows = len(maze)
    cols = len(maze[0])

    # 1. Base Case: Outside maze boundaries
    if x < 0 or x >= cols or y < 0 or y >= rows:
        return False

    # 2. Base Case: Goal reached
    if maze[y][x] == 'G':
        return True

    # 3. Base Case: Hit a wall or an already visited cell
    if maze[y][x] == '#' or visited[y][x]:
        return False

    # Mark the current cell as visited in our tracking matrix
    visited[y][x] = True

    # Mark the current cell as part of the tentative path
    # Replaces 'S' and '.' with '+'
    if maze[y][x] in ('.', 'S'):
        maze[y][x] = '+'

    if (find_first_path(maze, x + 1, y, visited) or  # East
        find_first_path(maze, x, y + 1, visited) or  # South
        find_first_path(maze, x - 1, y, visited) or  # West
        find_first_path(maze, x, y - 1, visited)):   # North
        return True

    if maze[y][x] == '+':
        maze[y][x] = 'X'

    return False

# Write solved maze to file
def write_maze(filename, maze):
    with open(filename, "w") as f:
        for row in maze:
            f.write("".join(row) + "\n")

def solve_first_path(input_file):
    maze = read_maze(input_file)
    start_x, start_y = find_start(maze)

    visited = [[False] * len(maze[0]) for _ in range(len(maze))]
    maze_copy = copy.deepcopy(maze)
    # Execute recursive search
    find_first_path(maze_copy, start_x, start_y, visited)

    # Write output to path1.txt
    write_maze("path1.txt", maze_copy)
    print("First path complete -> path1.txt created.")


# Run
if __name__ == "__main__":
    solve_first_path("inputPuzzle1.txt")