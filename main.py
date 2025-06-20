from window import Window
from maze import Maze

def main():
    width = 800
    height = 600

    win = Window(width, height)

    m = Maze(0, 0, 20, 30, 25, 25, win)

    win.wait_for_close()

if __name__ == "__main__":
    main()
