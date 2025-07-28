# Author: Margaret Seymour
# GitHub username: seydev27
# Coordinates the Troll Riddle Race game logic.
# Imports and integrates player movement, troll behavior, board display, and riddle challenges.

from board import create_board, display_board, move_entity, get_random_empty_position, distance
from riddles import ask_riddle, final_riddle_challenge
from player.player import get_player_move
from troll.troll import get_troll_move

BOARD_SIZE = 7

def game_loop():
    """
    Main gameplay loop. Alternates turns between player and troll based on riddle answers.
    """
    board = create_board(BOARD_SIZE)

    # Initialize random positions
    player_pos = get_random_empty_position(board)
    troll_pos = get_random_empty_position(board)
    treasure_pos = get_random_empty_position(board)

    # Ensure no overlaps
    while player_pos in [troll_pos, treasure_pos] or troll_pos == treasure_pos:
        player_pos = get_random_empty_position(board)
        troll_pos = get_random_empty_position(board)
        treasure_pos = get_random_empty_position(board)

    print("🎮 Welcome to Troll Riddle Race!")
    print("Solve riddles to move. If you fail, the troll moves instead!")
    print("Reach the treasure before the troll catches you!")

    while True:
        display_board(board, player_pos, troll_pos, treasure_pos)

        if player_pos == treasure_pos:
            print("💰 You've reached the treasure!")
            if final_riddle_challenge():
                print("🏆 You WIN!")
            else:
                print("💀 You couldn't solve the final challenge. The troll wins!")
            break

        if player_pos == troll_pos:
            print("👹 The troll caught you!")
            print("💀 Game Over.")
            break

        # Ask a riddle
        if ask_riddle():
            direction = get_player_move()
            player_pos = move_entity(player_pos, direction, BOARD_SIZE)
        else:
            troll_target = treasure_pos if distance(troll_pos, treasure_pos) < distance(troll_pos, player_pos) else player_pos
            troll_pos = get_troll_move(troll_pos, troll_target, BOARD_SIZE)
            # Hint to the player
            if troll_target == player_pos:
                print("👣 You hear heavy footsteps... they might be coming for you!")
            else:
                print("💬 The troll bellows in the distance — maybe it's after the treasure?")

if __name__ == "__main__":
    game_loop()
