from __future__ import annotations
from tkinter import Tk, BOTH, Canvas


class Window:
    def __init__(self, width: int, height: int):
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.__canvas = Canvas(self.__root, bg="#191724", width=width, height=height)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__window_running = False

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__window_running = True
        while self.__window_running:
            self.redraw()

    def close(self):
        self.__window_running = False

    def draw_line(self, line: Line, fill_color: str = "#524f67"):
        line.draw(self.__canvas, fill_color)


class Point:
    def __init__(self, x: int = 0, y: int = 0):
        self.x: int = x
        self.y: int = y


class Line:
    def __init__(self, p1: Point, p2: Point):
        self.p1: Point = p1
        self.p2: Point = p2

    def draw(self, canvas: Canvas, fill_color: str = "#524f67"):
        _ = canvas.create_line(
            self.p1.x,
            self.p1.y,
            self.p2.x,
            self.p2.y,
            fill=fill_color,
            width=2,
        )
