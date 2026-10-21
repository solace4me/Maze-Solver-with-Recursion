import copy

def read_maze(filename):
    with open(filename, "r") as f:
        return [list(line.strip()) for line in f if line.strip()]

def find_start(maze):
    for y in range(len(maze)):
        for x in range(len(maze[0])):
            if maze[y][x] == 'S':
                return x, y
    raise ValueError("Start 'S' not found in maze")

def find_all_paths(maze, x, y, visited, path, all_paths):
    rows = len(maze)
    cols = len(maze[0])

    # 1. Outside maze bounds
    if x < 0 or x >= cols or y < 0 or y >= rows:
        return

    # 2. Blocked or visited
    if maze[y][x] == '#' or visited[y][x]:
        return

    # 3. Goal found -> store path. The 'G' is kept as destination
    if maze[y][x] == 'G':
        all_paths.append(list(path))
        return

    visited[y][x] = True
    path.append((x, y))

    find_all_paths(maze, x, y - 1, visited, path, all_paths)  # North
    find_all_paths(maze, x + 1, y, visited, path, all_paths)  # East
    find_all_paths(maze, x, y + 1, visited, path, all_paths)  # South
    find_all_paths(maze, x - 1, y, visited, path, all_paths)  # West

    visited[y][x] = False
    path.pop()

def write_all_paths(filename, maze, all_paths):
    separator = "-" * 40 + "\n"
    with open(filename, "w") as f:
        for path in all_paths:
            f.write(separator)
            temp = copy.deepcopy(maze)

            # Mark path cells with '+' (replaces 'S' and '.', preserves 'G')
            for (x, y) in path:
                if temp[y][x] in ('.', 'S'):
                    temp[y][x] = '+'

            for row in temp:
                f.write("".join(row) + "\n")

            f.write(separator)

def solve_all_paths(input_file):
    maze = read_maze(input_file)
    start_x, start_y = find_start(maze)

    visited = [[False] * len(maze[0]) for _ in range(len(maze))]
    all_paths = []

    find_all_paths(maze, start_x, start_y, visited, [], all_paths)
    write_all_paths("pathAll.txt", maze, all_paths)
    print("All possible paths complete -> pathAll.txt created.")

if __name__ == "__main__":
    solve_all_paths("inputPuzzle2.txt")