from window import Window
from maze import Maze

def main():
    width = 800
    height = 600

    win = Window(width, height)

    m = Maze(
        x1 = 0,
        y1 = 0,
        num_rows = 8,
        num_cols = 12,
        cell_size_x = 64,
        cell_size_y = 64,
        window = win,)

    m.solve()

    win.wait_for_close()

if __name__ == "__main__":
    main()
