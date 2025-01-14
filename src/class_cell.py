from __future__ import annotations
from src.class_window import Window, Line, Point
from src.theme import Theme

theme = Theme()


class Cell:
    def __init__(self, window: Window | None = None):
        self.has_left_wall: bool = True
        self.has_right_wall: bool = True
        self.has_top_wall: bool = True
        self.has_bottom_wall: bool = True
        self.visited: bool = False
        self._x1: float = 0.0
        self._y1: float = 0.0
        self._x2: float = 0.0
        self._y2: float = 0.0
        self._win: Window | None = window

    def draw(self, x1: float, y1: float, x2: float, y2: float) -> None:
        """Draws a Cell (typically square, but could be a rectangle or parallelogram) between two sets of coordinates"""
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        top_left: Point = Point(x1, y1)
        top_right: Point = Point(x2, y1)
        bottom_left: Point = Point(x1, y2)
        bottom_right: Point = Point(x2, y2)

        if self._win is not None:
            if self.has_left_wall:
                self._win.draw_line(Line(top_left, bottom_left))
            else:
                self._win.draw_line(Line(top_left, bottom_left), theme.Base)
            if self.has_right_wall:
                self._win.draw_line(Line(top_right, bottom_right))
            else:
                self._win.draw_line(Line(top_right, bottom_right), theme.Base)
            if self.has_top_wall:
                self._win.draw_line(Line(top_left, top_right))
            else:
                self._win.draw_line(Line(top_left, top_right), theme.Base)
            if self.has_bottom_wall:
                self._win.draw_line(Line(bottom_left, bottom_right))
            else:
                self._win.draw_line(Line(bottom_left, bottom_right), theme.Base)

    def draw_move(self, to_cell: Cell, undo: bool = False) -> None:
        """Draws a line between two Cells. If `undo == True`, the line will be a lighter color"""
        self_x: float = self._x1 + (abs(self._x2 - self._x1) // 2)
        self_y: float = self._y1 + (abs(self._y2 - self._y1) // 2)
        target_x: float = to_cell._x1 + (abs(to_cell._x2 - to_cell._x1) // 2)
        target_y: float = to_cell._y1 + (abs(to_cell._y2 - to_cell._y1) // 2)

        line_color: str = theme.Subtle if undo else theme.Love

        if self._win is not None:
            self._win.draw_line(
                Line(Point(self_x, self_y), Point(target_x, target_y)), line_color
            )
