import recursive_backtracking
import visualization
import wavefrontp
import maze_gen


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

    theApp = visualization.App(
        M, N, start, goal, maze, theWFP.solution, theWFP.nos)
    theApp.on_execute()


if __name__ == "__main__":
    main()
