from __future__ import annotations
from src.class_window import Window
from src.class_cell import Cell
import time
import random


class Maze:
    def __init__(
        self,
        x1: int,
        y1: int,
        num_rows: int,
        num_cols: int,
        cell_size_x: int,
        cell_size_y: int,
        window: Window | None = None,
        seed: int | None = None,
    ):
        self._x1: int = x1
        self._y1: int = y1
        self._num_rows: int = num_rows
        self._num_cols: int = num_cols
        self._cells: list[list[Cell]] = []
        self._cell_size_x: int = cell_size_x
        self._cell_size_y: int = cell_size_y
        self._win: Window | None = window

        if seed:
            random.seed(seed)
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)

    def _create_cells(self) -> None:
        for _ in range(self._num_cols):
            col: list[Cell] = []
            for _ in range(self._num_rows):
                col.append(Cell(self._win))
            self._cells.append(col)
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i: int, j: int) -> None:
        x1: int = (self._cell_size_x * i) + self._x1
        y1: int = (self._cell_size_y * j) + self._y1
        x2: int = x1 + self._cell_size_x
        y2: int = y1 + self._cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()

    def _animate(self) -> None:
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self) -> None:
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        exit_col: int = self._num_cols - 1
        exit_row: int = self._num_rows - 1
        exit_cell: Cell = self._cells[exit_col][exit_row]
        exit_cell.has_bottom_wall = False
        self._draw_cell(exit_col, exit_row)

    def _break_walls_r(self, i: int, j: int) -> None:
        self._cells[i][j].visited = True
        while True:
            to_visit: list[tuple[int, int]] = []
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

    def _check_cell_breakability(self, i: int, j: int) -> bool:
        if (0 <= i < self._num_cols) and (0 <= j < self._num_rows):
            return self._cells[i][j].visited == False
        return False
