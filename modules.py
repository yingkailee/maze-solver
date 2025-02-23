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

class Cell:
    def __init__(self, window, x1, y1, x2, y2, has_left=True, has_right=True, has_top=True, has_bot=True):
        self.window = window
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.has_left = has_left
        self.has_right = has_right
        self.has_top = has_top
        self.has_bot = has_bot
    
    # (x1,y1) is top left
    # (x2,y2) is bottom right
    def draw(self):
        top_left = Point(self.x1, self.y1)
        bottom_left = Point(self.x1, self.y2)
        top_right = Point(self.x2, self.y1)
        bottom_right = Point(self.x2, self.y2)
        if (self.has_left):
            self.window.draw_line(Line(top_left, bottom_left), "black")
        if (self.has_right):
            self.window.draw_line(Line(top_right, bottom_right), "black")
        if (self.has_top):
            self.window.draw_line(Line(top_left, top_right), "black")
        if (self.has_bot):
            self.window.draw_line(Line(bottom_left, bottom_right), "black")
    
    def draw_move(self, to_cell, undo=False):
        fill_color = 'gray' if undo else 'red'
        from_center = Point((self.x1+self.x2)//2, (self.y1+self.y2)//2)
        to_center = Point((to_cell.x1+to_cell.x2)//2, (to_cell.y1+to_cell.y2)//2)
        self.window.draw_line(Line(from_center, to_center), fill_color)
