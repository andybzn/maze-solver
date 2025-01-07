from src.class_window import Window
from src.class_cell import Cell


def main():
    win = Window(800, 600)

    cell_0 = Cell(win)
    cell_0.has_bottom_wall = False
    cell_0.draw(00, 00, 50, 50)

    cell_1 = Cell(win)
    cell_1.has_top_wall = False
    cell_1.has_right_wall = False
    cell_1.draw(00, 50, 50, 100)

    cell_2 = Cell(win)
    cell_2.has_left_wall = False
    cell_2.has_bottom_wall = False
    cell_2.draw(50, 50, 100, 100)

    cell_3 = Cell(win)
    cell_3.has_top_wall = False
    cell_3.has_left_wall = False
    cell_3.draw(50, 100, 100, 150)

    cell_4 = Cell(win)
    cell_4.has_right_wall = False
    cell_4.draw(00, 100, 50, 150)

    cell_0.draw_move(cell_1)
    cell_1.draw_move(cell_2)
    cell_2.draw_move(cell_3)
    cell_3.draw_move(cell_4, True)

    win.wait_for_close()


if __name__ == "__main__":
    main()
