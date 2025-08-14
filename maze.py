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
        window = None,
    ):
        self.__x1 = x1
        self.__y1 = y1
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__window = window
        self.__cells = []
        self.__create_cells()

        self.__break_entrance_and_exit()

    def __create_cells(self):
        for i in range(self.__num_rows):
            self.__cells.append([])
            for j in range(self.__num_cols):
                self.__cells[i].append(Cell(self.__window))
                if self.__window:
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
        if self.__window:
            self.__window.redraw()
            time.sleep(0.01)

    def __break_entrance_and_exit(self):
        self.__cells[0][0].has_top_wall = False
        self.__draw_cell(0, 0)
        self.__cells[-1][-1].has_bottom_wall = False
        last_row = len(self.__cells) - 1
        last_col = len(self.__cells[last_row]) - 1
        self.__draw_cell(last_row, last_col)
