from __future__ import annotations
from src.class_window import Window
from src.class_cell import Cell
import time
import random


class Maze:
    def __init__(
        self,
        x1: float,
        y1: float,
        num_rows: int,
        num_cols: int,
        cell_size_x: int,
        cell_size_y: int,
        window: Window | None = None,
        seed: int | None = None,
    ):
        self._x1: float = x1
        self._y1: float = y1
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
        self._reset_cells_visited()

    def _create_cells(self) -> None:
        """Creates a grid of Cells. Maze width `self._num_cols` and height `self._num_rows`"""
        for _ in range(self._num_cols):
            col: list[Cell] = []
            for _ in range(self._num_rows):
                col.append(Cell(self._win))
            self._cells.append(col)
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i: int, j: int) -> None:
        """Draws a Cell to the screen"""
        x1: float = (self._cell_size_x * i) + self._x1
        y1: float = (self._cell_size_y * j) + self._y1
        x2: float = x1 + self._cell_size_x
        y2: float = y1 + self._cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate(True)

    def _animate(self, fast: bool = False) -> None:
        """Redraws the window if it exists"""
        if self._win is None:
            return
        self._win.redraw()
        if fast:
            time.sleep(0.01)
        else:
            time.sleep(0.05)

    def _break_entrance_and_exit(self) -> None:
        """Removes the top wall from the top left Cell, and the bottom wall from the bottom right Cell"""
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        exit_col: int = self._num_cols - 1
        exit_row: int = self._num_rows - 1
        exit_cell: Cell = self._cells[exit_col][exit_row]
        exit_cell.has_bottom_wall = False
        self._draw_cell(exit_col, exit_row)

    def _break_walls_r(self, i: int, j: int) -> None:
        """Recursively randomly breaks Cell walls between walls, starting at the provided col `i` & row `j` numbers"""
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
        """Helper function to determine if the Cell is valid & unvisited"""
        if (0 <= i < self._num_cols) and (0 <= j < self._num_rows):
            return self._cells[i][j].visited == False
        return False

    def _reset_cells_visited(self) -> None:
        """Resets the `.visited` status of all Cells in the Maze"""
        for col in self._cells:
            for row in col:
                row.visited = False

    def solve(self) -> bool:
        """Triggers the Maze solver. Returns `False` if the Maze cannot be solved"""
        return self._solve_r(i=0, j=0)

    def _solve_r(self, i: int, j: int) -> bool:
        """Recursively solves the Maze (if possible) using a DFS. If the cell is not the exit, and there is no-where to go, the function will attempt a different direction. Returns `False` if the route cannot be solved"""
        self._animate()
        self._cells[i][j].visited = True
        if i == (self._num_cols - 1) and j == (self._num_rows - 1):
            return True
        # check directions
        for k, l in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
            if self._check_cell_visitability(i, j, k, l):
                self._cells[i][j].draw_move(self._cells[k][l])
                if self._solve_r(k, l):
                    return True
                else:
                    self._cells[i][j].draw_move(self._cells[k][l], undo=True)
        return False

    def _check_cell_visitability(self, i: int, j: int, k: int, l: int) -> bool:
        """Helper function to determine if the next Cell (`k`,`l`) is valid, unvisited, and there are no walls between the current Cell (`i`,`j`) and the next"""
        if not (0 <= k < self._num_cols) or not (0 <= l < self._num_rows):
            return False
        current_cell = self._cells[i][j]
        target_cell = self._cells[k][l]
        if target_cell.visited:
            return False
        # determine if there is a wall
        if k < i and (current_cell.has_left_wall or target_cell.has_right_wall):
            return False
        if k > i and (current_cell.has_right_wall or target_cell.has_left_wall):
            return False
        if l < j and (current_cell.has_top_wall or target_cell.has_bottom_wall):
            return False
        if l > j and (current_cell.has_bottom_wall or target_cell.has_top_wall):
            return False
        return True
