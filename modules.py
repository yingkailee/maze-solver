from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.root = Tk()
        self.root.title("hello window")
        self.canvas = Canvas(self.root, height=height, width=width)
        self.canvas.pack()
        self.open = False
        self.root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.root.update_idletasks()
        self.root.update()
    
    def wait_for_close(self):
        self.open = True
        while (self.open):
            self.redraw()
        print('window closed')
    
    def close(self):
        self.open = False
    
    def draw_line(self, line, fill_color):
        line.draw(self.canvas, fill_color)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, pt1, pt2):
        self.pt1 = pt1
        self.pt2 = pt2
    
    def draw(self, canvas, fill_color):
        canvas.create_line(self.pt1.x, self.pt1.y, self.pt2.x, self.pt2.y, fill=fill_color, width=2)