from cell import Cell
import time

class Maze():
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win = None,
    ):
        self.__x1 = x1
        self.__y1 = y1
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__win = win
        self.__cells = []
        self.__create_cells()

    def __create_cells(self):
        for i in range(self.__num_rows):
            self.__cells.append([])
            for j in range(self.__num_cols):
                self.__cells[i].append(Cell(self.__win))
                if self.__win:
                    self.__draw_cell(i, j)

    def get_cells(self):
        return self.__cells

    def __draw_cell(self, i, j):
        y1 = i * self.__cell_size_y
        x1 = j * self.__cell_size_x
        y2 = y1 + self.__cell_size_y
        x2 = x1 + self.__cell_size_x

        self.__cells[i][j].draw(x1, y1, x2, y2)
        self._animate()

    def _animate(self):
        if self.__win:
            self.__win.redraw()
            time.sleep(0.05)
