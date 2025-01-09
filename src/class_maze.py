from src.class_cell import Cell
import time
import random


class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        window=None,
        seed=None,
    ):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cells = []
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = window

        if seed:
            random.seed(seed)
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)

    def _create_cells(self):
        for c in range(self._num_cols):
            col = []
            for r in range(self._num_rows):
                col.append(Cell(self._win))
            self._cells.append(col)
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        x1 = (self._cell_size_x * i) + self._x1
        y1 = (self._cell_size_y * j) + self._y1
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()

    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        entrance = self._cells[0][0]
        entrance.has_top_wall = False
        self._draw_cell(0, 0)
        exit_col = self._num_cols - 1
        exit_row = self._num_rows - 1
        exit_cell = self._cells[exit_col][exit_row]
        exit_cell.has_bottom_wall = False
        self._draw_cell(exit_col, exit_row)

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            to_visit = []
            for a, b in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if self._check_cell_breakability(a, b):
                    to_visit.append((a, b))
            if not to_visit:
                self._draw_cell(i, j)
                return
            r_col, r_row = to_visit[random.randrange(len(to_visit))]
            if r_col < i:
                self._cells[i][j].has_left_wall = False
                self._cells[r_col][r_row].has_right_wall = False
            if r_col > i:
                self._cells[i][j].has_right_wall = False
                self._cells[r_col][r_row].has_left_wall = False
            if r_row < j:
                self._cells[i][j].has_top_wall = False
                self._cells[r_col][r_row].has_bottom_wall = False
            if r_row > j:
                self._cells[i][j].has_bottom_wall = False
                self._cells[r_col][r_row].has_top_wall = False
            self._break_walls_r(r_col, r_row)

    def _check_cell_breakability(self, i, j):
        if (0 <= i < self._num_cols) and (0 <= j < self._num_rows):
            return self._cells[i][j].visited == False
        return False
