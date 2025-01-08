from src.class_window import Line, Point


class Cell:
    def __init__(self, window):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = 0
        self._y1 = 0
        self._x2 = 0
        self._y2 = 0
        self._win = window

    def draw(self, x1, y1, x2, y2):
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2

        top_left = Point(x1, y1)
        top_right = Point(x2, y1)
        bottom_left = Point(x1, y2)
        bottom_right = Point(x2, y2)

        if self.has_left_wall:
            self._win.draw_line(Line(top_left, bottom_left))
        if self.has_right_wall:
            self._win.draw_line(Line(top_right, bottom_right))
        if self.has_top_wall:
            self._win.draw_line(Line(top_left, top_right))
        if self.has_bottom_wall:
            self._win.draw_line(Line(bottom_left, bottom_right))

    def draw_move(self, to_cell, undo=False):
        self_x = self._x1 + (abs(self._x2 - self._x1) // 2)
        self_y = self._y1 + (abs(self._y2 - self._y1) // 2)
        target_x = to_cell._x1 + (abs(to_cell._x2 - to_cell._x1) // 2)
        target_y = to_cell._y1 + (abs(to_cell._y2 - to_cell._y1) // 2)

        line_color = "#908caa" if undo else "#eb6f92"

        self._win.draw_line(
            Line(Point(self_x, self_y), Point(target_x, target_y)), line_color
        )
