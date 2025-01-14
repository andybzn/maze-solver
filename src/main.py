from src.class_window import Window
from src.class_window_controls import WindowControls

# from src.class_maze import Maze
import sys


def main():
    sys.setrecursionlimit(10000)

    win = Window(800, 600)
    _ = WindowControls(win)
    win.wait_for_close()


if __name__ == "__main__":
    main()
