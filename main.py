from window import Window
from line import Line
from point import Point

def main():
    win = Window(800, 600)
    win.wait_for_close()

    l1 = Line(Point(0, 0), Point(100,100))
    l2 = Line(Point(300, 300), Point(150, 150))

    window.draw_line(l1, "blue")
    window.draw_line(l2, "red")

if __name__ == "__main__":
    main()
