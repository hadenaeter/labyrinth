import unittest
from maze import Maze
from cell import Cell

class SimpleTests(unittest.TestCase):

    def test_cell_has_all_walls_initially(self):
        """Test that a new cell has all 4 walls"""
        cell = Cell()
        self.assertTrue(cell.has_left_wall)
        self.assertTrue(cell.has_right_wall)
        self.assertTrue(cell.has_top_wall)
        self.assertTrue(cell.has_bottom_wall)

    def test_cell_walls_can_be_removed(self):
        """Test that we can remove walls from a cell"""
        cell = Cell()
        cell.has_left_wall = False
        cell.has_top_wall = False

        self.assertFalse(cell.has_left_wall)
        self.assertFalse(cell.has_top_wall)
        self.assertTrue(cell.has_right_wall)  # These should still be True
        self.assertTrue(cell.has_bottom_wall)

    def test_maze_creates_correct_number_of_cells(self):
        """Test that maze creates the right grid size"""
        rows = 5
        cols = 8
        maze = Maze(0, 0, rows, cols, 10, 10)
        cells = maze.get_cells()

        self.assertEqual(len(cells), rows)
        self.assertEqual(len(cells[0]), cols)

    def test_maze_cells_are_cell_objects(self):
        """Test that maze is filled with Cell objects"""
        maze = Maze(0, 0, 3, 3, 10, 10)
        cells = maze.get_cells()

        # Check that each cell is actually a Cell object
        for row in cells:
            for cell in row:
                self.assertIsInstance(cell, Cell)

    def test_cell_draw_move_doesnt_crash(self):
        """Test that drawing moves between cells works"""
        cell1 = Cell()
        cell2 = Cell()

        # Set up coordinates first
        cell1.draw(0, 0, 10, 10)
        cell2.draw(20, 0, 30, 10)

        # These should not crash
        cell1.draw_move(cell2)
        cell1.draw_move(cell2, undo=True)

    def test_break_entrance_and_exit(self):
        """Test that the maze is creating an entrance and exit"""
        rows = 5
        cols = 8
        maze = Maze(0, 0, rows, cols, 10, 10)
        maze.break_entrance_and_exit()
        cells = maze.get_cells()

        first = cells[0][0]
        last = cells[-1][-1]

        self.assertEqual(first.has_top_wall, False)
        self.assertEqual(last.has_bottom_wall, False)

if __name__ == "__main__":
    unittest.main()
