from window import Window
from maze import Maze

def main():
    width = 400
    height = 300

    win = Window(width, height)

    m = Maze(
        x1 = 0,
        y1 = 0,
        num_rows = 8,
        num_cols = 12,
        cell_size_x = 50,
        cell_size_y = 50,
        window = win)

    win.wait_for_close()

if __name__ == "__main__":
    main()
