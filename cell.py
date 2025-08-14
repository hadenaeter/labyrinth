from line import Line
from point import Point

class Cell:
    def __init__(self, window = None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.__x1 = -1
        self.__y1 = -1
        self.__x2 = -1
        self.__y2 = -1
        self.__win = window
        self.visited = False

    def draw(self, x1, y1, x2, y2):
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2
        if self.__win:
            if self.has_left_wall:
                self.__win.draw_line(Line(Point(x1, y1), Point(x1, y2)), "black")
            else:
                self.__win.draw_line(Line(Point(x1, y1), Point(x1, y2)), "#d9d9d9")
            if self.has_top_wall:
                self.__win.draw_line(Line(Point(x1, y1), Point(x2, y1)), "black")
            else:
                self.__win.draw_line(Line(Point(x1, y1), Point(x2, y1)), "#d9d9d9")
            if self.has_right_wall:
                self.__win.draw_line(Line(Point(x2, y1), Point(x2, y2)), "black")
            else:
                self.__win.draw_line(Line(Point(x2, y1), Point(x2, y2)), "#d9d9d9")
            if self.has_bottom_wall:
                self.__win.draw_line(Line(Point(x2, y2), Point(x1, y2)), "black")
            else:
                self.__win.draw_line(Line(Point(x2, y2), Point(x1, y2)), "#d9d9d9")

    def draw_move(self, to_cell, undo=False):
        if undo:
            line_color = "gray"
        else:
            line_color = "red"

        self_middle_x = ((self.__x1 + self.__x2) / 2)
        self_middle_y = ((self.__y1 + self.__y2) / 2)

        to_middle_x = ((to_cell.__x1 + to_cell.__x2) / 2)
        to_middle_y = ((to_cell.__y1 + to_cell.__y2) / 2)

        self_middle = Point(self_middle_x, self_middle_y)
        to_middle = Point(to_middle_x, to_middle_y)

        if self.__win:
            self.__win.draw_line(Line(self_middle, to_middle), line_color)
