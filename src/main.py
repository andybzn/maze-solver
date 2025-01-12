from src.class_window import Window
from src.class_maze import Maze
import sys


def main():

    padding = 50
    cell_size = 50
    window_height, window_width = 600, 800
    maze_width = (window_width - (padding * 2)) // cell_size
    maze_height = (window_height - (padding * 2)) // cell_size

    sys.setrecursionlimit(10000)

    win = Window(window_width, window_height)
    maze = Maze(50, 50, maze_height, maze_width, cell_size, cell_size, win)
    if maze.solve():
        print("Maze solved!")
    else:
        print("Maze cannot be solved :(")
    win.wait_for_close()


if __name__ == "__main__":
    main()
