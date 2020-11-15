import recursive_backtracking
import visualization
import wavefrontp
import maze_gen

M = 10
N = 8
# maze = [[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
#         [-1, 0, 0, 0, 0, 0, 0, 0, 0,-1],
#         [-1, 0, 0, 0, 0, 0, 0, 0, 0,-1],
#         [-1, 0,-1,-1,-1,-1,-1,-1, 0,-1],
#         [-1, 0,-1, 0, 0, 0, 0,-1, 0,-1],
#         [-1, 0,-1, 0,-1,-1,-1,-1, 0,-1],
#         [-1, 0, 0, 0, 0, 0, 0,-1, 0,-1],
#         [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]]
# start = (1,1)
# goal = (6,4)
# maze = [[0, 0, 0, 0, 0, -1, 0, 0, 0, -1, 0, -1, 0, 0, 0, -1, 0, 0, 0, 0, 0, -1, 0, -1, 0, 0, 0, 0, 0, 0, 0],
#  [-1, -1, -1, -1, 0, -1, -1, -1, 0, -1, 0, -1, 0, -1, -1, -1, -1, -1, 0, -1, -1, -1, 0, -1, 0, -1, -1, -1, -1, -1, 0],
#  [0, -1, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, -1, 0, -1, 0, 0, 0, -1, 0, 0, 0],
#  [0, -1, -1, -1, -1, -1, -1, -1, 0, -1, -1, -1, 0, -1, -1, -1, -1, -1, 0, -1, -1, -1, 0, -1, 0, -1, -1, -1, -1, -1, 0],
#  [0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, -1, 0, -1, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, -1, 0],
#  [0, -1, -1, -1, 0, -1, 0, -1, 0, -1, -1, -1, 0, -1, -1, -1, 0, -1, -1, -1, 0, -1, -1, -1, -1, -1, 0, -1, -1, -1, -1],
#  [0, -1, 0, 0, 0, -1, 0, -1, 0, -1, 0, 0, 0, 0, 0, -1, 0, 0, 0, -1, 0, -1, 0, -1, 0, -1, 0, 0, 0, 0, 0],
#  [-1, -1, 0, -1, -1, -1, 0, -1, 0, -1, -1, -1, 0, -1, -1, -1, 0, -1, -1, -1, 0, -1, 0, -1, 0, -1, 0, -1, -1, -1, -1],
#  [0, 0, 0, -1, 0, 0, 0, -1, 0, -1, 0, 0, 0, 0, 0, -1, 0, 0, 0, -1, 0, 0, 0, 0, 0, -1, 0, -1, 0, -1, 0],
#  [0, -1, -1, -1, 0, -1, 0, -1, 0, -1, -1, -1, -1, -1, 0, -1, 0, -1, -1, -1, 0, -1, -1, -1, -1, -1, 0, -1, 0, -1, 0],
#  [0, -1, 0, 0, 0, -1, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
# M = len(maze[0])
# N = len(maze)
# start = (0,0)
# goal = (30,10)

# hight = 15
# weight = 21
# maze = maze_gen.Maze(hight, weight)
# maze = maze.maze_generator()
# print(maze)
# M = len(maze[0])
# N = len(maze)
# start = (0, 0)
# if maze[start[1]][start[0]] == 1:
#     start = (0, 1)
# goal = (weight-1, hight-1)
# if maze[goal[1]][goal[0]] == 1:
#     goal = (weight-1, hight-2)


def main():
    hight = 11
    weight = 20
    maze = maze_gen.Maze(hight, weight)
    maze = maze.maze_generator()
    print(maze)
    M = len(maze[0])
    N = len(maze)
    start = (0, 0)
    if maze[start[1]][start[0]] == -1:
        start = (0, 1)
    goal = (weight-1, hight-1)
    if maze[goal[1]][goal[0]] == -1:
        goal = (weight-1, hight-2)
    print(start, goal)
    theWFP = wavefrontp.WFP(M, N, maze, start, goal)
    theWFP.execute()

    theApp = visualization.App(M, N, start, goal, maze, theWFP.solution, theWFP.nos)
    theApp.on_execute()


if __name__ == "__main__":
    main()

    # hight = 11
    # weight = 31
    # maze = maze_gen.Maze(hight, weight)
    # maze.maze_generator()
    # theRBT = recursive_backtracking.RBT(M, N, maze, start, goal)
    # theRBT.execute()

    # theApp = visualization.App(M, N, start, goal, maze, theRBT.solution, theRBT.nos)
    # theApp.on_execute()



    # theWFP = wavefrontp.WFP(M, N, maze, start, goal)
    # theWFP.execute()

    # theApp = visualization.App(M, N, start, goal, maze, theWFP.solution, theWFP.nos)
    # theApp.on_execute()