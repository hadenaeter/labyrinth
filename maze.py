from cell import Cell
import time
import random

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
        seed = None
    ):
        self.__x1 = x1
        self.__y1 = y1
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__window = window
        self.__cells = []
        if seed:
            random.seed(seed)
        self.__create_cells()
        self.__break_entrance_and_exit()
        self.__break_walls_r(0, 0)
        self.__reset_cells_visited()

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
        if self.__window is None:
            return

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
        # entrance
        self.__cells[0][0].has_top_wall = False
        self.__draw_cell(0, 0)

        # exit
        last_row = len(self.__cells) - 1
        last_col = len(self.__cells[0]) - 1
        self.__cells[last_row][last_col].has_bottom_wall = False
        self.__draw_cell(last_row, last_col)

    def __break_walls_r(self, i, j):
        self.__cells[i][j].visited = True

        while True:
            to_visit = []

            # pick what to visit next
            # left
            if j > 0 and not self.__cells[i][j - 1].visited:
                to_visit.append((i, j - 1))
            # top
            if i > 0 and not self.__cells[i - 1][j].visited:
                to_visit.append((i - 1, j))
            # right
            if j < self.__num_cols - 1 and not self.__cells[i][j + 1].visited:
                to_visit.append((i, j + 1))
            # bottom
            if i < self.__num_rows - 1 and not self.__cells[i + 1][j].visited:
                to_visit.append((i + 1, j))

            # nowhere to go, break
            if len(to_visit) == 0:
                self.__draw_cell(i, j)
                return

            # random next step
            direction_i = random.randrange(len(to_visit))
            next_visit = to_visit[direction_i]

            # break walls between this cell and next cell
            # left
            if next_visit[1] == j - 1:
                self.__cells[i][j].has_left_wall = False
                self.__cells[i][j - 1].has_right_wall = False
            # top
            if next_visit[0] == i - 1:
                self.__cells[i][j].has_top_wall = False
                self.__cells[i - 1][j].has_bottom_wall = False
            # right
            if next_visit[1] == j + 1:
                self.__cells[i][j].has_right_wall = False
                self.__cells[i][j + 1].has_left_wall = False
            # bottom
            if next_visit[0] == i + 1:
                self.__cells[i][j].has_bottom_wall = False
                self.__cells[i + 1][j].has_top_wall = False

            # recurse, next cell
            self.__break_walls_r(next_visit[0], next_visit[1])

    def __reset_cells_visited(self):
        for row in self.__cells:
            for cell in row:
                cell.visited = False

    def solve(self):
        solved = self._solve_r(0, 0)
        return solved

    def _solve_r(self, i, j):
        cell = self.__cells[i][j]

        self._animate()
        cell.visited = True

        if cell == self.__cells[-1][-1]: # goal/exit cell
            return True

        left_cell = self.__cells[i][j - 1] if j > 0 else None
        top_cell = self.__cells[i - 1][j] if i > 0 else None
        right_cell = self.__cells[i][j + 1] if j < self.__num_cols - 1 else None
        bottom_cell = self.__cells[i + 1][j] if i < self.__num_rows - 1 else None

        # left
        if left_cell and not cell.has_left_wall and not left_cell.visited:
            cell.draw_move(left_cell)
            if self._solve_r(i, j - 1) == True:
                return True
            else:
                cell.draw_move(left_cell, undo=True)
        # top
        if top_cell and not cell.has_top_wall and not top_cell.visited:
            cell.draw_move(top_cell)
            if self._solve_r(i - 1, j) == True:
                return True
            else:
                cell.draw_move(top_cell, undo=True)
        # right
        if right_cell and not cell.has_right_wall and not right_cell.visited:
            cell.draw_move(right_cell)
            if self._solve_r(i, j + 1) == True:
                return True
            else:
                cell.draw_move(right_cell, undo=True)
        # bottom
        if bottom_cell and not cell.has_bottom_wall and not bottom_cell.visited:
            cell.draw_move(bottom_cell)
            if self._solve_r(i + 1, j) == True:
                return True
            else:
                cell.draw_move(bottom_cell, undo=True)

        return False
