# Author: Margaret Seymour
# GitHub username: seydev27
# Defines the Player class for Troll Riddle Race.
# Handles player movement and input validation.

class Player:
    """
    Represents the player in the Troll Riddle Race game.
    Responsible for managing position and movement input.
    """

    def __init__(self, start_pos):
        """
        Initializes the player with a starting position.
        
        Parameters:
        - start_pos (tuple): A (row, col) tuple for the player's starting location
        """
        self.position = start_pos

    def move(self, direction, board_size):
        """
        Updates the player's position based on the direction,
        ensuring they stay within the board boundaries.

        Parameters:
        - direction (str): One of 'N', 'S', 'E', 'W'
        - board_size (int): The length/width of the square game board
        """
        row, col = self.position

        if direction == 'N' and row > 0:
            row -= 1
        elif direction == 'S' and row < board_size - 1:
            row += 1
        elif direction == 'E' and col < board_size - 1:
            col += 1
        elif direction == 'W' and col > 0:
            col -= 1

        self.position = (row, col)

    def get_move_input(self):
        """
        Prompts the player for a movement direction.
        Returns a validated uppercase direction (N/S/E/W).
        """
        valid_directions = ['N', 'S', 'E', 'W']
        while True:
            direction = input("Which direction do you want to move? (N/S/E/W): ").strip().upper()
            if direction in valid_directions:
                return direction
            print("🚫 Invalid direction. Please enter N, S, E, or W.")
