# MRS Hackathon
GitHub repository - https://github.com/YaelBenShalom/Python_a-Maze-ing_Challenge

## Overview
In this project, me and my team created a maze exploration software.
A simulated robotic agent takes discrete steps on a grid in the maze, while trying to navigate to a goal.

## Maze Generation Pseudo Code:
1. A Grid consists of a 2 dimensional array of cells.
2. A Cell has 2 states: Blocked or Passage.
3. Start with a Grid full of Cells in state Blocked.
4. Pick a random Cell, set it to state Passage and Compute its frontier cells. A frontier cell of a Cell is a cell with distance 2 in state Blocked and within the grid.
5. While the list of frontier cells is not empty:
    - Pick a random frontier cell from the list of frontier cells.
    - Let neighbors(frontierCell) = All cells in distance 2 in state Passage. 
    - Pick a random neighbor and connect the frontier cell with the neighbor by setting the neighbor & the cell in-between to state Passage. 
    - Compute the frontier cells of the chosen frontier cell and add them to the frontier list. 
    - Remove the chosen frontier cell from the list of frontier cells.

## Usage and Configuration Instructions
1. First, you'll need to install `pygame` on your platform:

    `pip install pygame`

    You can verify the install by loading one of the examples that comes with the library:
    
    `python3 -m pygame.examples.aliens`

2. To run the software, run `maze_game.py`

Maze generation for 31x11 grid:
![Maze generation 31x11](https://github.com/YaelBenShalom/Python_a-Maze-ing_Challenge/blob/master/videos/maze.gif)

3. To cange the grid, change the hight and weight parameters on `maze_game.py` file:

Maze generation for 20x13 grid:
![Maze generation 20x13](https://github.com/YaelBenShalom/Python_a-Maze-ing_Challenge/blob/master/videos/maze2.gif)
