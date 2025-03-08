from modules import Window, Maze

def main():
    window = Window(1500,1500)
    rows, cols = 20, 20
    maze = Maze(0,0,rows,cols,30,30,window, 5)
    maze.break_entrance_and_exit()
    maze.break_walls(0,0)
    maze.break_walls(3,3)
    maze.break_walls(6,6)
    maze.break_walls(9,9)
    maze.break_walls(12,12)
    maze.break_walls(15,15)
    maze.break_walls(18,18)
    for i in range(rows):
        for j in range(cols):
            maze.draw_cell(i,j)
    maze.reset_cells_visited()
    print('start solve')
    solved = maze.solve(0,0)
    print('solved' if solved else 'failed solve')
    window.wait_for_close()

if __name__ == "__main__":
    main()

'''
Add other solving algorithms, like breadth-first search or A*
Make the visuals prettier, change the colors, etc
Mess with the animation settings to make it faster/slower. Maybe make backtracking slow and blazing new paths faster?
Add configurations in the app itself using Tkinter buttons and inputs to allow users to change maze size, speed, etc
Make much larger mazes to solve
Make it a game where the user chooses directions
If you made it a game, allow the user to race an algorithm
Make it 3 dimensional
Time the various algorithms and see which ones are the fastest
'''