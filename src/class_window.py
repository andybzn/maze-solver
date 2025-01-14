from __future__ import annotations
from src.theme import Theme
from tkinter import Tk, BOTH, Canvas

theme = Theme()

welcome_text = r"""
███╗   ███╗ █████╗ ███████╗███████╗    ███████╗ ██████╗ ██╗    ██╗   ██╗███████╗██████╗ 
████╗ ████║██╔══██╗╚══███╔╝██╔════╝    ██╔════╝██╔═══██╗██║    ██║   ██║██╔════╝██╔══██╗
██╔████╔██║███████║  ███╔╝ █████╗      ███████╗██║   ██║██║    ██║   ██║█████╗  ██████╔╝
██║╚██╔╝██║██╔══██║ ███╔╝  ██╔══╝      ╚════██║██║   ██║██║    ╚██╗ ██╔╝██╔══╝  ██╔══██╗
██║ ╚═╝ ██║██║  ██║███████╗███████╗    ███████║╚██████╔╝███████╗╚████╔╝ ███████╗██║  ██║
╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝╚══════╝    ╚══════╝ ╚═════╝ ╚══════╝ ╚═══╝  ╚══════╝╚═╝  ╚═╝
"""


class Window:
    def __init__(self, width: int, height: int):
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.__root.configure(
            background=theme.Surface
        )  # pyright:ignore[reportUnusedCallResult]
        self.__canvas = Canvas(
            self.__root,
            bg=theme.Base,
            width=width,
            height=height,
            bd=0,
            highlightthickness=0,
        )
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

    def draw_line(self, line: Line, fill_color: str = theme.HighlightHigh):
        line.draw(self.__canvas, fill_color)

    def clear_canvas(self):
        self.__canvas.delete("all")

    def get_canvas_dimensions(self) -> tuple[int, int]:
        return self.__canvas.winfo_height(), self.__canvas.winfo_width()

    def welcome_message(self):
        _ = self.__canvas.create_text(
            400,
            300,
            anchor="center",
            text=welcome_text,
            fill=theme.Text,
            font="TkFixedFont",
        )
        self.__canvas.update()


class Point:
    def __init__(self, x: float = 0.0, y: float = 0.0):
        self.x: float = x
        self.y: float = y


class Line:
    def __init__(self, p1: Point, p2: Point):
        self.p1: Point = p1
        self.p2: Point = p2

    def draw(self, canvas: Canvas, fill_color: str = theme.HighlightHigh):
        _ = canvas.create_line(
            self.p1.x,
            self.p1.y,
            self.p2.x,
            self.p2.y,
            fill=fill_color,
            width=2,
        )
