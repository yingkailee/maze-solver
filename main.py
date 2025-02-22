from modules import Window, Point, Line

def main():
    window = Window(800,800)
    pt1, pt2 = Point(5, 5), Point(100, 100)
    line = Line(pt1, pt2)
    window.draw_line(line, "red")
    window.wait_for_close()

if __name__ == "__main__":
    main()