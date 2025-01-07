from src.class_window import Line, Point


class Cell:
    def __init__(
        self,
        window,
    ):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._y1 = None
        self._x2 = None
        self._y2 = None
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
