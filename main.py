from modules import Window, Point, Line, Cell

def main():
    window = Window(800,800)
    #window.draw_line(Line(Point(5, 5), Point(100, 100)), "red")
    full_cell = Cell(window,5,5,100,100)
    full_cell.draw()
    vert_cell = Cell(window,500,500,600,600,True, True, False, False)
    vert_cell.draw()
    hori_cell = Cell(window,100,600,200,700,False, False)
    hori_cell.draw()
    vert_cell.draw_move(hori_cell)
    window.wait_for_close()

if __name__ == "__main__":
    main()