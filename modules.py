from tkinter import Tk, Canvas
import random
import time

class Window:
    """Window with canvas"""
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
    def __init__(self, x1, y1, x2, y2, window=None, has_left=True, has_right=True, has_top=True, has_bot=True):
        self.window = window
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.has_left = has_left
        self.has_right = has_right
        self.has_top = has_top
        self.has_bot = has_bot
        self.visited = False
    
    # (x1,y1) is top left
    # (x2,y2) is bottom right
    def draw(self):
        top_left = Point(self.x1, self.y1)
        bottom_left = Point(self.x1, self.y2)
        top_right = Point(self.x2, self.y1)
        bottom_right = Point(self.x2, self.y2)
        color = "black" if self.has_left else "white"
        self.window.draw_line(Line(top_left, bottom_left), color)
        color = "black" if self.has_right else "white"
        self.window.draw_line(Line(top_right, bottom_right), color)
        color = "black" if self.has_top else "white"
        self.window.draw_line(Line(top_left, top_right), color)
        color = "black" if self.has_bot else "white"
        self.window.draw_line(Line(bottom_left, bottom_right), color)
    
    def draw_move(self, to_cell, undo=False):
        fill_color = 'gray' if undo else 'red'
        from_center = Point((self.x1+self.x2)//2, (self.y1+self.y2)//2)
        to_center = Point((to_cell.x1+to_cell.x2)//2, (to_cell.y1+to_cell.y2)//2)
        self.window.draw_line(Line(from_center, to_center), fill_color)

class Maze:
    def __init__(self, xi, yi, rows, cols, cell_x, cell_y, window=None, seed=None):
        self.xi = xi
        self.yi = yi
        self.rows = rows
        self.cols = cols
        self.cell_x = cell_x
        self.cell_y = cell_y
        self.window = window
        self.create_cells()
        if seed is not None:
            random.seed(seed)
    
    def create_cells(self):
        self.cells = []
        for rind in range(self.rows):
            cell_row = []
            for cind in range(self.cols):
                pos_x = self.xi+self.cell_x*cind
                pos_y = self.yi+self.cell_y*rind
                new_cell = Cell(pos_x, pos_y, pos_x+self.cell_x, pos_y+self.cell_y, self.window)
                cell_row.append(new_cell)
            self.cells.append(cell_row)

    def draw_cell(self, i, j):
        self.cells[i][j].draw()
    
    def animate(self):
        self.window.redraw()
        time.sleep(0.1)

    def break_entrance_and_exit(self):
        self.cells[0][0].has_top = False
        self.cells[self.rows-1][self.cols-1].has_bot = False

    def break_walls(self, i, j):
        if self.cells[i][j].visited:
            return
        self.cells[i][j].visited = True
        next_pos = []
        for i_off, j_off in [(0,-1), (0,1), (-1,0), (1,0)]:
            i_next, j_next = i+i_off, j+j_off
            if i_next < 0 or i_next >= len(self.cells) or j_next < 0 or j_next >= len(self.cells[0]):
                continue
            if self.cells[i_next][j_next].visited:
                continue
            next_pos.append((i_next, j_next))
        if len(next_pos) == 0:
            self.draw_cell(i, j)
            return
        next_i, next_j = random.choice(next_pos)
        self.break_wall(i, j, next_i, next_j)

        self.break_walls(next_i, next_j)
    
    def break_wall(self, i, j, next_i, next_j):
        off_i, off_j = next_i-i, next_j-j
        if off_j == -1:
            self.cells[i][j].has_left = False
            self.cells[next_i][next_j].has_right = False
        if off_j == 1:
            self.cells[i][j].has_right = False
            self.cells[next_i][next_j].has_left = False
        if off_i == -1:
            self.cells[i][j].has_top = False
            self.cells[next_i][next_j].has_bot = False
        if off_i == 1:
            self.cells[i][j].has_bot = False
            self.cells[next_i][next_j].has_top = False
    
    def reset_cells_visited(self):
        for i in range(len(self.cells)):
            for j in range(len(self.cells[0])):
                self.cells[i][j].visited = False
    
    def can_pass(self, i, j, next_i, next_j):
        off_i, off_j = next_i-i, next_j-j
        valid = True
        if off_j == -1:
            valid = not self.cells[i][j].has_left and not self.cells[next_i][next_j].has_right
        if off_j == 1:
            valid = not self.cells[i][j].has_right and not self.cells[next_i][next_j].has_left
        if off_i == -1:
            valid = not self.cells[i][j].has_top and not self.cells[next_i][next_j].has_bot
        if off_i == 1:
            valid = not self.cells[i][j].has_bot and not self.cells[next_i][next_j].has_top
        return valid

    def solve(self, i, j):
        if i == len(self.cells)-1 and j == len(self.cells[0])-1:
            return True
        self.animate()
        self.cells[i][j].visited = True
        for i_off, j_off in [(0,-1), (0,1), (-1,0), (1,0)]:
            i_next, j_next = i+i_off, j+j_off
            if i_next < 0 or i_next >= len(self.cells) or j_next < 0 or j_next >= len(self.cells[0]):
                continue
            if self.cells[i_next][j_next].visited:
                continue
            if self.can_pass(i, j, i_next, j_next):
                self.cells[i][j].draw_move(self.cells[i_next][j_next])
                if self.solve(i_next, j_next):
                    return True
                self.cells[i][j].draw_move(self.cells[i_next][j_next], True)
        return False

            
