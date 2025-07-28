# Author: Margaret Seymour
# GitHub username: seydev27
# Defines the Troll class for Troll Riddle Race.
# Handles autonomous troll movement and proximity behavior.

import random

class Troll:
    """
    Represents the troll character in the Troll Riddle Race game.
    Moves autonomously, either toward the player or the treasure.
    """

    def __init__(self, start_pos):
        """
        Initializes the troll with a starting position.
        
        Parameters:
        - start_pos (tuple): A (row, col) tuple for the troll's initial location
        """
        self.position = start_pos

    def move_toward(self, target_pos, board_size):
        """
        Moves the troll one step closer to a given target (player or treasure).
        Uses Manhattan distance logic to choose direction.

        Parameters:
        - target_pos (tuple): The (row, col) target to move toward
        - board_size (int): The size of the square game board
        """
        row, col = self.position
        target_row, target_col = target_pos

        # Prioritize vertical movement if farther away
        if abs(target_row - row) >= abs(target_col - col):
            if target_row < row:
                row -= 1
            elif target_row > row and row < board_size - 1:
                row += 1
        else:
            if target_col < col:
                col -= 1
            elif target_col > col and col < board_size - 1:
                col += 1

        self.position = (row, col)

    def move_randomly(self, board_size):
        """
        Moves the troll randomly one step in any valid direction.

        Parameters:
        - board_size (int): The size of the square game board
        """
        row, col = self.position
        directions = []

        if row > 0:
            directions.append((-1, 0))
        if row < board_size - 1:
            directions.append((1, 0))
        if col > 0:
            directions.append((0, -1))
        if col < board_size - 1:
            directions.append((0, 1))

        if directions:
            dr, dc = random.choice(directions)
            self.position = (row + dr, col + dc)
