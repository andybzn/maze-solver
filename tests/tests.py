# pyright: strict, reportPrivateUsage=false
import unittest
from src.class_maze import Maze


class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(len(m1._cells), num_cols)
        self.assertEqual(len(m1._cells[0]), num_rows)

    def test_maze_create_wide(self):
        num_cols = 50
        num_rows = 3
        maze = Maze(0, 0, num_rows, num_cols, 1, 1)
        self.assertEqual(len(maze._cells), num_cols)
        self.assertEqual(len(maze._cells[0]), num_rows)

    def test_maze_create_tall(self):
        num_cols = 2
        num_rows = 50
        maze = Maze(0, 0, num_rows, num_cols, 1, 1)
        self.assertEqual(len(maze._cells), num_cols)
        self.assertEqual(len(maze._cells[0]), num_rows)

    def test_maze_entrance_removal(self):
        num_cols = 2
        num_rows = 2
        maze = Maze(0, 0, num_rows, num_cols, 1, 1)
        self.assertEqual(maze._cells[0][0].has_top_wall, False)

    def test_maze_exit_removal(self):
        num_cols = 2
        num_rows = 2
        maze = Maze(0, 0, num_rows, num_cols, 1, 1)
        self.assertEqual(maze._cells[num_cols - 1][num_rows - 1].has_bottom_wall, False)


if __name__ == "__main__":
    unittest.main()  # pyright:ignore[reportUnusedCallResult]
