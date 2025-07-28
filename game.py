# Author: Margaret Seymour
# GitHub username: seydev27
# Main game logic for Troll Riddle Race (web-adapted version).
# Coordinates board creation, player and troll movement, riddle logic, and win/loss conditions.

from board import create_board, display_board, move_entity, get_random_empty_position, distance
from riddles import ask_riddle, final_riddle_challenge
from player import get_player_move
from troll import troll_decide_move

BOARD_SIZE = 7

def initialize_positions():
    """
    Randomly assigns non-overlapping positions for player, troll, and treasure.
    Returns tuple of positions.
    """
    player = get_random_empty_position(None)
    troll = get_random_empty_position(None)
    treasure = get_random_empty_position(None)
    # Ensure all three are unique
    while troll == player or treasure == player or treasure == troll:
        troll = get_random_empty_position(None)
        treasure = get_random_empty_position(None)
    return player, troll, treasure

def game_loop():
    """
    Main loop for Troll Riddle Race.
    Alternates between player and troll movement based on riddle results.
    """
    player_pos, troll_pos, treasure_pos = initialize_positions()
    board = create_board(BOARD_SIZE)

    print("\n🎮 Welcome to Troll Riddle Race!")
    print("🧠 Solve riddles to move. ❌ Fail, and the troll moves instead!")
    print("🏆 Reach the treasure before the troll catches you!\n")

    while True:
        display_board(board, player_pos, troll_pos, treasure_pos)

        if player_pos == treasure_pos:
            print("\n💰 You've reached the treasure!")
            if final_riddle_challenge():
                print("🏆 You win!")
            else:
                print("😓 You failed the final challenge. The troll claims the treasure.")
            break

        if player_pos == troll_pos:
            print("\n💀 The troll caught you! Game over.")
            break

        # Present riddle
        if ask_riddle():
            print("✅ Correct! Choose a direction: (N, S, E, W)")
            direction = get_player_move()
            player_pos = move_entity(player_pos, direction, BOARD_SIZE)
        else:
            print("👹 Wrong! The troll gets a turn.")
            troll_direction = troll_decide_move(troll_pos, player_pos, treasure_pos)
            troll_pos = move_entity(troll_pos, troll_direction, BOARD_SIZE)

        # Proximity warning
        if distance(player_pos, troll_pos) <= 2:
            print("⚠️ You hear heavy footsteps nearby...")
        elif distance(troll_pos, treasure_pos) <= 2:
            print("⚠️ The troll bellows near the treasure...")

if __name__ == "__main__":
    game_loop()
