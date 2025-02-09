# Maze Solver Using BFS in Python (Curses Library)

## Overview
This Python program solves a maze using the **Breadth-First Search (BFS)** algorithm. It visualizes the pathfinding process using the **curses** library, which enables colored terminal-based UI updates. The algorithm finds the shortest path from the start (`O`) to the exit (`X`).

## How It Works
1. **Maze Representation:**
   - The maze is a 2D list where:
     - `#` represents walls.
     - `O` represents the starting position.
     - `X` represents the goal position.
     - ` ` (space) represents open paths.

2. **BFS Algorithm:**
   - It uses a queue to explore the shortest path from `O` to `X`.
   - Keeps track of visited positions to avoid looping.
   - Adds valid neighboring positions to the queue and constructs the path dynamically.

3. **Curses Library for Visualization:**
   - The curses library enables dynamic updates to the terminal screen.
   - Colors are used to distinguish the maze structure and the path taken by the algorithm.
   - A `time.sleep(0.2)` delay makes the visualization clear and smooth.

## Code Explanation

### **1. Maze Representation**
```python
maze = [
    ["#", "O", "#", "#", "#", "#", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", " ", "#", "#", " ", "#", "#", " ", "#"],
    ["#", " ", "#", " ", " ", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "X", "#"]
]
```

### **2. Print Maze with Colors**
- Uses `curses` to display the maze with colors for paths (`X`) and walls (`#`).
```python
def print_maze(maze, stdscr, path=[]):
    BLUE = curses.color_pair(1)
    RED = curses.color_pair(2)
    
    for i, row in enumerate(maze):
        for j, value in enumerate(row):
            if (i, j) in path:
                stdscr.addstr(i, j * 2, "X", RED)
            else:
                stdscr.addstr(i, j * 2, value, BLUE)
```

### **3. Finding the Start Position**
```python
def find_start(maze, start):
    for i, row in enumerate(maze):
        for j, value in enumerate(row):
            if value == start:
                return i, j
    return None
```

### **4. BFS Pathfinding Algorithm**
```python
def find_path(maze, stdscr):
    start = "O"
    end = "X"
    start_pos = find_start(maze, start)
    
    q = queue.Queue()
    q.put((start_pos, [start_pos]))
    visited = set()
    
    while not q.empty():
        current_pos, path = q.get()
        row, col = current_pos

        stdscr.clear()
        print_maze(maze, stdscr, path)
        time.sleep(0.2)
        stdscr.refresh()

        if maze[row][col] == end:
            return path

        neighbors = find_neighbors(maze, row, col)
        for neighbor in neighbors:
            if neighbor in visited:
                continue

            r, c = neighbor
            if maze[r][c] == "#":
                continue

            new_path = path + [neighbor]
            q.put((neighbor, new_path))
            visited.add(neighbor)
```

### **5. Finding Valid Neighboring Positions**
```python
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

    return neighbors
```

### **6. Main Function for Execution**
```python
def main(stdscr):
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)

    find_path(maze, stdscr)
    stdscr.getch()

wrapper(main)
```

## Installation and Execution
### **1. Install Dependencies**
```sh
pip install windows-curses  # Required for Windows (Linux/macOS has built-in curses)
```

### **2. Run the Script**
```sh
python maze_solver.py
```

## Features
✅ **Uses BFS for shortest pathfinding**  
✅ **Real-time visualization with colors**  
✅ **Avoids infinite loops with visited set**  
✅ **Handles obstacles (`#`) and open paths (` `)**  
✅ **Adjustable delay (`time.sleep(0.2)`) for better visualization**  

## Troubleshooting
1. **Curses Not Found Error (Windows Users)**
   - Run: `pip install windows-curses`

2. **Terminal Not Updating Properly**
   - Ensure the script is run in a **proper terminal (cmd, PowerShell, or Linux/macOS terminal).**

3. **Maze Not Displaying Properly**
   - Increase terminal width to ensure characters align correctly.

## Customization
- **Change the Maze:** Modify the `maze` list to create custom puzzles.
- **Adjust Delay:** Modify `time.sleep(0.2)` for faster/slower animation.
- **Change Colors:** Modify `curses.init_pair()` for different colors.

## Conclusion
This project demonstrates **BFS-based pathfinding** with real-time visualization using `curses`. It is a great starting point for understanding **graph traversal, terminal UI, and real-time algorithms.** 🚀

Feel free to modify and experiment with different maze structures! 🎉

