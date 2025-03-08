import unittest
from modules import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        cols, rows = 12, 10
        m1 = Maze(0, 0, rows, cols, 10, 10)
        self.assertEqual(len(m1.cells), rows)
        self.assertEqual(len(m1.cells[0]), cols)

if __name__ == "__main__":
    unittest.main()
