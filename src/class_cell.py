from __future__ import annotations
from src.class_window import Window, Line, Point


class Cell:
    def __init__(self, window: Window | None = None):
        self.has_left_wall: bool = True
        self.has_right_wall: bool = True
        self.has_top_wall: bool = True
        self.has_bottom_wall: bool = True
        self.visited: bool = False
        self._x1: int = 0
        self._y1: int = 0
        self._x2: int = 0
        self._y2: int = 0
        self._win: Window | None = window

    def draw(self, x1: int, y1: int, x2: int, y2: int) -> None:
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
                self._win.draw_line(Line(top_left, bottom_left), "#191724")
            if self.has_right_wall:
                self._win.draw_line(Line(top_right, bottom_right))
            else:
                self._win.draw_line(Line(top_right, bottom_right), "#191724")
            if self.has_top_wall:
                self._win.draw_line(Line(top_left, top_right))
            else:
                self._win.draw_line(Line(top_left, top_right), "#191724")
            if self.has_bottom_wall:
                self._win.draw_line(Line(bottom_left, bottom_right))
            else:
                self._win.draw_line(Line(bottom_left, bottom_right), "#191724")

    def draw_move(self, to_cell: Cell, undo: bool = False) -> None:
        """Draws a line between two Cells. If `undo == True`, the line will be a lighter color"""
        self_x: int = self._x1 + (abs(self._x2 - self._x1) // 2)
        self_y: int = self._y1 + (abs(self._y2 - self._y1) // 2)
        target_x: int = to_cell._x1 + (abs(to_cell._x2 - to_cell._x1) // 2)
        target_y: int = to_cell._y1 + (abs(to_cell._y2 - to_cell._y1) // 2)

        line_color: str = "#908caa" if undo else "#eb6f92"

        if self._win is not None:
            self._win.draw_line(
                Line(Point(self_x, self_y), Point(target_x, target_y)), line_color
            )
