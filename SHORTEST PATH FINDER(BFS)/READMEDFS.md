# Maze Solver using Depth-First Search (DFS)

## Introduction
This project is a **maze-solving visualization** using **Depth-First Search (DFS)** in Python. The program uses the `curses` library to display a maze and highlights the path taken by the DFS algorithm in real time.

## How It Works
- The maze is represented as a **2D list**, where:
  - `#` represents walls.
  - `O` represents the **starting position**.
  - `X` represents the **goal position**.
  - Spaces (`" "`) represent walkable paths.
- The DFS algorithm explores all possible paths to find a way from `O` (start) to `X` (goal).
- The visualization uses **colors**:
  - **Blue** (`curses.COLOR_BLUE`) for the maze structure.
  - **Red** (`curses.COLOR_RED`) to highlight the path taken by DFS.
- The program runs in a **terminal** and updates the visualization dynamically.

## Features
✔️ Uses **DFS** for pathfinding.
✔️ **Real-time visualization** of the search process.
✔️ Highlights the **path from start to goal**.
✔️ Uses **Python's `curses` module** for dynamic terminal rendering.

## Installation & Requirements
### Prerequisites
- **Python 3.x** installed.
- A terminal that supports `curses` (works on Linux, macOS, and Windows via WSL or Python curses support).

### Installation Steps
1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/maze-dfs-visualizer.git
   cd maze-dfs-visualizer
   ```
2. **Run the script**
   ```bash
   python maze_dfs.py
   ```

## Code Explanation
### 1. **Maze Representation**
The maze is stored as a **2D list** where each element represents a different part of the maze:
```python
maze = [
    ["#", "#", "#", "#", "O", "#", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", " ", "#", "#", " ", "#", "#", " ", "#"],
    ...
]
```

### 2. **DFS Algorithm**
DFS explores the maze using a **stack (LIFO)**:
```python
stack = [(start_pos, [start_pos])]
```
- The algorithm **pops** positions from the stack and explores their **neighbors**.
- If a position is valid (not visited and not a wall `#`), it's added to the stack.
- The **path is stored and updated** dynamically.

### 3. **Finding Neighbors**
The function `find_neighbors()` finds **valid moves** (up, down, left, right):
```python
if row > 0:
    neighbors.append((row - 1, col))  # UP
if row + 1 < len(maze):
    neighbors.append((row + 1, col))  # DOWN
if col > 0:
    neighbors.append((row, col - 1))  # LEFT
if col + 1 < len(maze[0]):
    neighbors.append((row, col + 1))  # RIGHT
```

### 4. **Printing the Maze in Terminal**
Using `curses`, the maze is **dynamically updated** in the terminal:
```python
stdscr.clear()
print_maze(maze, stdscr, path)
time.sleep(0.2)  # Delay for visualization
stdscr.refresh()
```

### 5. **Colors & Visualization**
- **Walls & empty spaces** are printed in **blue**.
- **Path taken by DFS** is printed in **red**.

## Expected Output
When you run the program, you'll see the DFS **exploring the maze** step-by-step, marking the path taken. Once the `X` (goal) is reached, the path is displayed.

## Possible Improvements
🔹 Add **Breadth-First Search (BFS)** for comparison.
🔹 Allow **user input** for defining custom mazes.
🔹 Optimize the rendering for **faster performance**.

## Conclusion
This project demonstrates how DFS can be used to **solve mazes visually**. It provides an interactive way to **understand pathfinding algorithms** using real-time updates in the terminal.