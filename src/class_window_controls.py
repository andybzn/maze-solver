from __future__ import annotations
from src.class_window import Window
from src.class_maze import Maze
from src.theme import Theme
from tkinter import Button, Event, FLAT, Frame, font, Label
from typing import Callable, TypedDict, Unpack
import time


theme = Theme()


class WindowControls:
    def __init__(self, window: Window):
        self._win: Window = window
        self._maze: Maze | None = None
        self._generating: bool = False
        self._generated: bool = False
        self._solving: bool = False
        self._solved: bool = False
        self._status: str = ""
        self.__frame = Frame(bg=theme.Surface)
        self.__frame.pack(pady=15)
        self.__generate_maze = CustomButton(
            self.__frame, text="Generate Maze", command=self._draw_maze
        ).pack(side="left", padx=10)
        self.__solve_maze = CustomButton(
            self.__frame, text="Solve Maze", command=self._solve_maze
        ).pack(side="left", padx=10)
        self.__clear_maze = CustomButton(
            self.__frame, text="Clear", command=self._clear_maze
        ).pack(side="left", padx=10)
        self.__status_msg: CustomLabel = CustomLabel(None, text=self._status)
        self.__status_msg.pack(side="left", padx=10, pady=5)
        self._win.welcome_message()

    def _clear_maze(self):
        if not self._generating and not self._solving:
            self._win.clear_canvas()
            self._solved = False
            self._generated = False
            self._update_status("")

    def _draw_maze(self):
        if not self._generating and not self._solving:
            self._clear_maze()
            self._generating = True
            self._update_status("Generating...")

            padding, cell_size = 50, 50
            window_height, window_width = self._win.get_canvas_dimensions()
            maze_width = (window_width - (padding * 2)) // cell_size
            maze_height = (window_height - (padding + (padding // 2))) // cell_size
            padding_x = (window_width - (maze_width * cell_size)) / 2
            padding_y = (window_height - (maze_height * cell_size)) / 2
            self._maze = Maze(
                padding_x,
                padding_y,
                maze_height,
                maze_width,
                cell_size,
                cell_size,
                self._win,
            )
            self._update_status("Generated!")
            self._generating = False
            self._generated = True
            time.sleep(0.5)
            self._update_status("")

    def _solve_maze(self):
        if self._maze and self._generated and not (self._solving or self._solved):
            self._solving = True
            self._update_status("Solving...")
            if self._maze.solve():
                self._update_status("Maze Solved!")
                self._solved = True
            else:
                self._update_status("This one is no good :(")
            self._solving = False
            time.sleep(0.5)
            self._update_status("")

    def _update_status(self, text: str):
        self._status = text
        _ = self.__status_msg.configure(text=self._status)
        self._win.redraw()


class LabelArgs(TypedDict):
    text: str


class CustomLabel(Label):
    def __init__(self, master: Frame | None = None, **kwargs: Unpack[LabelArgs]):
        super().__init__(master, **kwargs)
        _ = self.config(
            background=theme.Surface, foreground=theme.Iris, font=font.Font(size=10)
        )


class ButtonArgs(TypedDict):
    text: str
    command: Callable[[], None]


class CustomButton(Button):
    def __init__(self, master: Frame | None = None, **kwargs: Unpack[ButtonArgs]):
        super().__init__(master, **kwargs)
        _ = self.config(
            relief=FLAT,
            bd=0,
            highlightthickness=0,
            padx=10,
            pady=5,
            activebackground=theme.Base,
            activeforeground=theme.Text,
            background=theme.Overlay,
            foreground=theme.Subtle,
            font=font.Font(size=12),
        )
        _ = self.bind("<Enter>", self.on_hover)
        _ = self.bind("<Leave>", self.on_leave)

    def on_hover(self, _event: Event[CustomButton]):
        _ = self.config(
            background=theme.Base,
            foreground=theme.Text,
        )

    def on_leave(self, _event: Event[CustomButton]):
        _ = self.config(
            background=theme.Overlay,
            foreground=theme.Subtle,
        )
