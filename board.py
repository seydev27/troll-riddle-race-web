# Author: Margaret Seymour
# GitHub username: seydev27
# Game board utilities for Troll Riddle Race.
# Includes functions for creating, displaying, and interacting with a 2D grid.

import random

def create_board(size=7):
    """
    Creates and returns a 2D list (size x size) filled with empty strings
    representing the game board.
    """
    return [[" " for _ in range(size)] for _ in range(size)]

def display_board(board, player_pos, troll_pos, treasure_pos):
    """
    Displays the current game board with positions of player, troll, and treasure.
    (Only used for debugging or terminal version.)
    """
    size = len(board)
    for row in range(size):
        for col in range(size):
            if (row, col) == player_pos:
                print("🧍", end=" ")
            elif (row, col) == troll_pos:
                print("👹", end=" ")
            elif (row, col) == treasure_pos:
                print("💰", end=" ")
            else:
                print("⬜", end=" ")
        print()

def move_entity(position, direction, board_size):
    """
    Moves an entity one step in the given direction ('N', 'S', 'E', 'W'),
    constrained by the board boundaries.
    """
    row, col = position
    if direction == 'N' and row > 0:
        row -= 1
    elif direction == 'S' and row < board_size - 1:
        row += 1
    elif direction == 'E' and col < board_size - 1:
        col += 1
    elif direction == 'W' and col > 0:
        col -= 1
    return (row, col)

def get_random_empty_position(board):
    """
    Returns a random (row, col) tuple within the board size.
    """
    size = len(board)
    return (random.randint(0, size - 1), random.randint(0, size - 1))

def distance(pos1, pos2):
    """
    Returns the Manhattan distance between two positions.
    """
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])
