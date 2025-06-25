from window import Window
from maze import Maze

def main():
    width = 400
    height = 300

    win = Window(width, height)

    m = Maze(
        x1 = 0,
        y1 = 0,
        num_rows = 5,
        num_cols = 5,
        cell_size_x = 50,
        cell_size_y = 50,
        window = win)

    m.break_entrance_and_exit()

    win.wait_for_close()

if __name__ == "__main__":
    main()
