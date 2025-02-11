import curses
from curses import wrapper
import time

# Maze representation using a 2D list
maze = [
    ["#", "#", "#", "#", "O", "#", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", " ", "#", "#", " ", "#", "#", " ", "#"],
    ["#", " ", "#", " ", " ", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "X", "#"]
]

# Function to print the maze with the path highlighted
def print_maze(maze, stdscr, path=[]):
    BLUE = curses.color_pair(1)  # Normal maze color
    RED = curses.color_pair(2)   # Path color
    
    for i, row in enumerate(maze):
        for j, value in enumerate(row):
            if (i, j) in path:
                stdscr.addstr(i, j * 2, "X", RED)  # Highlight path in red
            else:
                stdscr.addstr(i, j * 2, value, BLUE)  # Print maze normally

# Function to find the start position in the maze
def find_start(maze, start):
    for i, row in enumerate(maze):
        for j, value in enumerate(row):
            if value == start:
                return i, j
    return None

# DFS algorithm to find the path from start to end
def dfs(maze, stdscr):
    start = "O"
    end = "X"
    
    start_pos = find_start(maze, start)  # Find the start position
    stack = [(start_pos, [start_pos])]  # Use a stack for DFS (LIFO)
    visited = set()

    while stack:
        current_pos, path = stack.pop()  # LIFO: Pop the last added position
        row, col = current_pos

        stdscr.clear()
        print_maze(maze, stdscr, path)  # Print the current path
        time.sleep(0.2)  # Pause for visualization
        stdscr.refresh()

        if maze[row][col] == end:
            return path  # Return path if the end is reached
        
        neighbors = find_neighbors(maze, row, col)
        for neighbor in neighbors:
            if neighbor in visited:
                continue
            
            r, c = neighbor
            if maze[r][c] == "#":  # Ignore walls
                continue

            new_path = path + [neighbor]  # Add neighbor to path
            stack.append((neighbor, new_path))  # Push to stack
            visited.add(neighbor)  # Mark as visited

# Function to find valid neighboring cells
def find_neighbors(maze, row, col):
    neighbors = []
    
    if row > 0:  # UP
        neighbors.append((row - 1, col))
    if row + 1 < len(maze):  # DOWN
        neighbors.append((row + 1, col))
    if col > 0:  # LEFT
        neighbors.append((row, col - 1))
    if col + 1 < len(maze[0]):  # RIGHT
        neighbors.append((row, col + 1))
    
    return neighbors[::-1]  # Reverse for correct DFS order

# Main function to initialize colors and run DFS
def main(stdscr):
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)  # Maze color
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)  # Path color
    
    dfs(maze, stdscr)  # Run DFS
    stdscr.getch()  # Wait for user input before exiting

# Run the program using curses wrapper
wrapper(main)
